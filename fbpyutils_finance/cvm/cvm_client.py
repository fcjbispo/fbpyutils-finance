import os
import sqlite3
import pandas as pd
from datetime import datetime
from typing import Optional, List, Dict, Tuple, Any

# Import necessary components from the project structure
import fbpyutils_finance as FI
import fbpyutils.file as FU
from fbpyutils.debug import debug_info

# Import functions from the new submodules within the cvm package
from .remote import get_remote_files_list, update_cvm_history_file
from .file_io import read_cvm_history_file
# headers.py functions are usually used *before* initializing CVM or passed in,
# but check_cvm_headers_changed might be useful internally if needed.
from .headers import check_cvm_headers_changed

# --- Constantes Globais (Podem ser movidas para um config.py se crescerem) ---
# Defined here for clarity, but could be imported from __init__ or config
URL_IF_REGISTER = "http://dados.cvm.gov.br/dados/FI/CAD/DADOS"
URL_IF_REGISTER_HIST = "http://dados.cvm.gov.br/dados/FI/CAD/DADOS/HIST"
URL_IF_DAILY = "http://dados.cvm.gov.br/dados/FI/DOC/INF_DIARIO/DADOS"
URL_IF_DAILY_HIST = "http://dados.cvm.gov.br/dados/FI/DOC/INF_DIARIO/DADOS/HIST"

# --- Classe Principal CVM ---

class CVM:
    """
    Client class for interacting with CVM (Comissão de Valores Mobiliários) data.

    Provides methods to update a local catalog of CVM files, download new/updated files,
    and retrieve processed data from downloaded files.

    Requires pre-loaded header mappings (headers_df) during initialization.
    """

    CATALOG_JOURNAL_TABLE = 'cvm_if_catalog_journal'
    REMOTE_FILES_TABLE = 'cvm_if_remote_files_staging' # Use staging suffix

    @staticmethod
    def check_history_folder(history_folder: Optional[str] = None) -> str:
        """
        Checks if the history folder exists and creates it if it doesn't.

        Args:
            history_folder (Optional[str], optional): The path to the history folder.
                If None, defaults to a subfolder 'history' within USER_APP_FOLDER.
                Defaults to None.

        Returns:
            str: The validated or created history folder path.

        Raises:
            OSError: If the folder cannot be created.
        """
        # Use FI.USER_APP_FOLDER defined in fbpyutils_finance
        history_folder = history_folder or os.path.join(FI.USER_APP_FOLDER, 'history')
        if not os.path.exists(history_folder):
            try:
                os.makedirs(history_folder, exist_ok=True) # exist_ok=True avoids error if dir exists
                print(f"Ensured history folder exists: {history_folder}")
            except OSError as e:
                print(f"Error creating history folder {history_folder}: {e}")
                raise # Re-raise error if folder creation fails
        return history_folder

    def __init__(self, headers_df: pd.DataFrame, catalog_db_path: Optional[str] = None, history_folder: Optional[str] = None):
        """
        Initializes the CVM client.

        Args:
            headers_df (pd.DataFrame): Pre-loaded DataFrame containing header mappings. Must not be None or empty.
            catalog_db_path (Optional[str], optional): Path to the SQLite database file for the catalog.
                If None, defaults to 'catalog.db' within USER_APP_FOLDER. Defaults to None.
            history_folder (Optional[str], optional): Path to the folder for storing downloaded CVM files.
                If None, uses the default from check_history_folder. Defaults to None.

        Raises:
            ValueError: If the headers_df is None or empty.
            ConnectionError: If the database connection fails.
        """
        if headers_df is None or headers_df.empty:
             raise ValueError("headers_df (DataFrame with header mappings) must be provided and cannot be empty during CVM client initialization.")
        self.HEADERS_DF = headers_df # Store the pre-loaded headers DataFrame

        db_path_base = catalog_db_path or os.path.join(FI.USER_APP_FOLDER, 'catalog.db')
        # Ensure the directory for the database exists
        os.makedirs(os.path.dirname(db_path_base), exist_ok=True)
        self.catalog_db_path = db_path_base

        try:
            self.CATALOG = sqlite3.connect(self.catalog_db_path)
            # Enable Write-Ahead Logging for better concurrency, if appropriate
            # self.CATALOG.execute("PRAGMA journal_mode=WAL;")
            print(f"Connected to catalog database: {self.catalog_db_path}")
        except sqlite3.Error as e:
             print(f"FATAL: Failed to connect to catalog database at {self.catalog_db_path}: {e}")
             raise ConnectionError(f"Could not connect to database: {e}") from e


        self.HISTORY_FOLDER = CVM.check_history_folder(history_folder)
        print(f"Using history folder: {self.HISTORY_FOLDER}")

        # Initialize tables if they don't exist
        self._initialize_catalog_tables()


    def _initialize_catalog_tables(self):
        """Creates the necessary tables in the catalog database if they don't exist."""
        if not FI.is_valid_db_connection(self.CATALOG):
             print("Error: Cannot initialize tables, database connection is not valid.")
             return
        try:
            cursor = self.CATALOG.cursor()
            # Create journal table - use TEXT for dates for simplicity with SQLite
            cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {self.CATALOG_JOURNAL_TABLE} (
                sequence INTEGER,
                href TEXT,
                name TEXT,
                last_modified TEXT, -- Store as ISO format string (YYYY-MM-DD HH:MM:SS)
                size INTEGER,
                history INTEGER, -- Store boolean as INTEGER (0 or 1)
                url TEXT PRIMARY KEY NOT NULL, -- URL should be unique identifier
                kind TEXT,
                last_download TEXT, -- Store as ISO format string
                last_updated TEXT,  -- Store as ISO format string
                process INTEGER DEFAULT 1, -- Boolean as INTEGER
                active INTEGER DEFAULT 1   -- Boolean as INTEGER
            );
            """)
            # Create index for faster lookups
            cursor.execute(f"CREATE INDEX IF NOT EXISTS idx_journal_kind_name ON {self.CATALOG_JOURNAL_TABLE} (kind, name);")
            cursor.execute(f"CREATE INDEX IF NOT EXISTS idx_journal_process_active ON {self.CATALOG_JOURNAL_TABLE} (process, active);")
            cursor.execute(f"CREATE INDEX IF NOT EXISTS idx_journal_url ON {self.CATALOG_JOURNAL_TABLE} (url);") # Index on PK

            # Create remote files staging table (used temporarily during update)
            cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {self.REMOTE_FILES_TABLE} (
                sequence INTEGER,
                href TEXT,
                name TEXT,
                last_modified TEXT,
                size INTEGER,
                history INTEGER,
                url TEXT,
                kind TEXT
            );
            """)
            self.CATALOG.commit()
            print("Catalog tables initialized successfully.")
        except sqlite3.Error as e:
            print(f"Error initializing catalog tables: {e}")
            self.CATALOG.rollback() # Rollback changes on error
            # Decide if this should be fatal - probably yes
            raise RuntimeError(f"Failed to initialize database tables: {e}") from e


    def __del__(self):
        """Closes the database connection upon object destruction."""
        if hasattr(self, 'CATALOG') and self.CATALOG:
            try:
                # Optional: Commit any final changes? Usually done explicitly.
                # self.CATALOG.commit()
                self.CATALOG.close()
                print(f"Closed catalog database connection: {self.catalog_db_path}")
            except sqlite3.Error as e:
                # Avoid raising errors in __del__
                print(f"Error closing catalog database during object deletion: {e}")
        self.CATALOG = None


    def get_cvm_catalog(self) -> Optional[pd.DataFrame]:
        """
        Retrieves the current CVM catalog journal from the database.

        Returns:
            Optional[pd.DataFrame]: DataFrame containing the catalog data, or None if the table
                                    doesn't exist or an error occurs. Converts integer booleans back.
        """
        if not FI.is_valid_db_connection(self.CATALOG):
             print("Error: Catalog database connection is not valid.")
             return None
        try:
            # Check if table exists first
            cursor = self.CATALOG.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?;", (self.CATALOG_JOURNAL_TABLE,))
            if cursor.fetchone() is None:
                print(f"Catalog table '{self.CATALOG_JOURNAL_TABLE}' does not exist.")
                # Return empty DataFrame with expected columns?
                # Define expected columns based on _initialize_catalog_tables
                cols = ['sequence', 'href', 'name', 'last_modified', 'size', 'history', 'url', 'kind', 'last_download', 'last_updated', 'process', 'active']
                return pd.DataFrame(columns=cols)


            df = pd.read_sql(f"SELECT * FROM {self.CATALOG_JOURNAL_TABLE}", con=self.CATALOG)

            # Convert integer columns back to boolean if needed for consistency elsewhere
            for col in ['history', 'process', 'active']:
                 if col in df.columns:
                      df[col] = df[col].astype(bool)
            return df

        except (sqlite3.Error, pd.io.sql.DatabaseError) as e:
            print(f"Error retrieving CVM catalog: {e}")
            return None


    def update_cvm_catalog(self) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]], List[Tuple[str, int]]]:
        """
        Updates the local CVM catalog by comparing against remote file listings and downloading changes.

        1. Fetches current and historical file lists from CVM URLs.
        2. Compares with the local catalog journal using SQL merge logic.
        3. Identifies new, updated, or removed files and updates 'active'/'process' flags.
        4. Downloads files marked for processing.
        5. Updates 'last_download' and 'process' flags for processed files.

        Returns:
            Tuple[List[Dict[str, Any]], List[Dict[str, Any]], List[Tuple[str, int]]]: A tuple containing:
                - update_summary (List[Dict]): Summary of download results (errors, successes per URL).
                - processed_metadata (List[Dict]): List of metadata dictionaries for files attempted/processed.
                - db_operations (List[Tuple[str, int]]): List of SQL update operations performed and rows affected.
        """
        step = 'SETTING UP COMPONENTS'
        update_summary = []
        processed_metadata = []
        db_ops = [] # Store (sql_template, row_count)

        if not FI.is_valid_db_connection(self.CATALOG):
             raise ConnectionError("Catalog database connection is not valid.")

        try:
            step = "FETCHING REMOTE FILE LISTS"
            if_remote_files = pd.concat([
                get_remote_files_list('IF_REGISTER', URL_IF_REGISTER, URL_IF_REGISTER_HIST),
                get_remote_files_list('IF_POSITION', URL_IF_DAILY, URL_IF_DAILY_HIST)
            ], ignore_index=True)

            if if_remote_files.empty:
                print("Warning: No remote files found or fetched. Catalog update skipped.")
                return [], [], []

            # Convert boolean 'history' to integer for SQLite compatibility
            if 'history' in if_remote_files.columns:
                 if_remote_files['history'] = if_remote_files['history'].astype(int)

            # Store remote files temporarily for comparison (overwrite existing)
            if_remote_files.to_sql(self.REMOTE_FILES_TABLE, con=self.CATALOG, if_exists='replace', index=False)
            print(f"Stored {len(if_remote_files)} remote file entries in staging table.")

            step = "UPDATING CATALOG JOURNAL (MERGE LOGIC)"
            cursor = self.CATALOG.cursor()

            # 1. Deactivate entries in journal not present remotely anymore
            deactivate_sql = f"""
                UPDATE {self.CATALOG_JOURNAL_TABLE}
                SET active = 0, process = 0
                WHERE active = 1 AND url NOT IN (SELECT url FROM {self.REMOTE_FILES_TABLE});
            """
            cursor.execute(deactivate_sql)
            deactivated_count = cursor.rowcount
            if deactivated_count > 0:
                 print(f"Deactivated {deactivated_count} entries in catalog no longer present remotely.")
                 db_ops.append((deactivate_sql, deactivated_count))


            # 2. Insert new entries from remote list or update existing ones
            # Using INSERT OR REPLACE based on URL primary key simplifies the merge
            # Need to handle date comparison carefully in SQLite (use ISO strings)
            merge_sql = f"""
                INSERT OR REPLACE INTO {self.CATALOG_JOURNAL_TABLE} (
                    sequence, href, name, last_modified, size, history, url, kind,
                    last_download, last_updated, process, active
                )
                SELECT
                    r.sequence, r.href, r.name, r.last_modified, r.size, r.history, r.url, r.kind,
                    -- Keep existing download/update times if replacing
                    COALESCE(j.last_download, NULL),
                    COALESCE(j.last_updated, NULL),
                    -- Determine if processing is needed (compare ISO strings)
                    CASE
                        WHEN r.last_modified IS NULL THEN 0 -- Cannot compare if remote date missing
                        WHEN j.last_download IS NULL THEN 1 -- Never downloaded
                        WHEN r.last_modified > j.last_download THEN 1 -- Remote is newer (string comparison works for ISO format)
                        ELSE 0 -- Already downloaded and up-to-date
                    END,
                    1 -- Mark as active
                FROM {self.REMOTE_FILES_TABLE} r
                LEFT JOIN {self.CATALOG_JOURNAL_TABLE} j ON r.url = j.url;
            """
            cursor.execute(merge_sql)
            merged_count = cursor.rowcount # Note: INSERT OR REPLACE counts affected rows
            print(f"Merged/Updated catalog journal based on remote files (affected rows: {merged_count}).")
            # This count isn't super informative for INSERT OR REPLACE, skip adding to db_ops for now

            self.CATALOG.commit() # Commit merge changes


            step = "IDENTIFYING FILES TO DOWNLOAD"
            files_to_process_df = pd.read_sql(f"""
                SELECT * FROM {self.CATALOG_JOURNAL_TABLE}
                WHERE process = 1 AND active = 1
            """, con=self.CATALOG)

            # Convert integer booleans back for metadata dict
            for col in ['history', 'process', 'active']:
                 if col in files_to_process_df.columns:
                      files_to_process_df[col] = files_to_process_df[col].astype(bool)

            metadata_to_process = files_to_process_df.to_dict(orient='records')
            if not metadata_to_process:
                print("Catalog is up-to-date. No files need downloading.")
                # Clean up staging table
                cursor.execute(f"DROP TABLE IF EXISTS {self.REMOTE_FILES_TABLE};")
                self.CATALOG.commit()
                return [], [], db_ops

            print(f"Found {len(metadata_to_process)} files needing download/update.")


            step = "DOWNLOADING AND PROCESSING FILES"
            all_results = []
            # Consider parallel processing here if beneficial and safe (beware of DB writes)
            # For simplicity, processing sequentially first
            for meta in metadata_to_process:
                meta['history_folder'] = self.HISTORY_FOLDER # Ensure history folder is in metadata
                # Call the download function (from remote.py)
                download_results = update_cvm_history_file(meta)
                all_results.extend(download_results) # Collect results from download attempts
                processed_metadata.append(meta) # Track which metadata was processed


            step = 'CONSOLIDATING DOWNLOAD RESULTS'
            if not all_results:
                 print("No download results generated.")
                 # Clean up staging table
                 cursor.execute(f"DROP TABLE IF EXISTS {self.REMOTE_FILES_TABLE};")
                 self.CATALOG.commit()
                 return [], processed_metadata, db_ops # Return empty summary

            # Create DataFrame from results for easier aggregation
            result_cols = ['status', 'metadata', 'message']
            result_data = pd.DataFrame(all_results, columns=result_cols)

            # Extract key info from metadata for summary
            result_data['name'] = result_data['metadata'].apply(lambda x: x.get('name'))
            result_data['kind'] = result_data['metadata'].apply(lambda x: x.get('kind'))
            result_data['url'] = result_data['metadata'].apply(lambda x: x.get('url'))
            # Get the last_download time recorded *during* the successful download
            result_data['actual_last_download'] = result_data.apply(
                lambda row: row['metadata'].get('last_download') if row['status'] == 'SUCCESS' else None, axis=1
            )

            # Generate summary (errors, successes per original URL)
            summary = result_data.groupby('url').agg(
                 name=('name', 'first'),
                 kind=('kind', 'first'),
                 errors=('status', lambda x: (x == 'ERROR').sum()),
                 successes=('status', lambda x: (x == 'SUCCESS').sum()),
                 # Get the first successful download time for this URL group
                 successful_download_time=('actual_last_download', 'first')
            ).reset_index()

            update_summary = summary.to_dict(orient='records')


            step = 'UPDATING CATALOG JOURNAL WITH DOWNLOAD STATUS'
            successful_updates = []
            for record in summary.to_dict('records'):
                 if record['errors'] == 0 and record['successes'] > 0:
                      # Use the actual download time if available, else current time as fallback
                      dl_time = record['successful_download_time'] or datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                      successful_updates.append((dl_time, 0, record['url'])) # (last_download, process=0, url)

            if successful_updates:
                 update_sql = f"""
                     UPDATE {self.CATALOG_JOURNAL_TABLE}
                     SET last_download = ?,
                         process = ?
                     WHERE url = ? AND process = 1 AND active = 1;
                 """
                 cursor.executemany(update_sql, successful_updates)
                 updated_count = cursor.rowcount
                 print(f"Updated download status for {updated_count} successfully processed files in catalog.")
                 db_ops.append((update_sql + " (batch)", updated_count)) # Record operation (template)

            self.CATALOG.commit() # Commit final status updates

            # Clean up staging table
            cursor.execute(f"DROP TABLE IF EXISTS {self.REMOTE_FILES_TABLE};")
            self.CATALOG.commit()

            return update_summary, processed_metadata, db_ops

        except Exception as E:
            info = debug_info(E)
            if FI.is_valid_db_connection(self.CATALOG):
                 self.CATALOG.rollback() # Rollback any uncommitted changes on error
            raise ValueError(f'Failed to update CVM catalog at step {step}: {E} ({info})')
        finally:
            # Ensure staging table is dropped even if errors occurred mid-process
            try:
                if FI.is_valid_db_connection(self.CATALOG):
                    cursor = self.CATALOG.cursor()
                    cursor.execute(f"DROP TABLE IF EXISTS {self.REMOTE_FILES_TABLE};")
                    self.CATALOG.commit()
            except sqlite3.Error as drop_err:
                 print(f"Warning: Failed to drop staging table {self.REMOTE_FILES_TABLE}: {drop_err}")

            # Ensure main connection is still valid after potential errors
            if not FI.is_valid_db_connection(self.CATALOG):
                 print("Warning: Catalog DB connection became invalid during update.")


    def get_cvm_files_to_process(self, kind: Optional[str] = None, history: Optional[bool] = None) -> List[Tuple[str, str, bool, Tuple[str, ...]]]:
        """
        Retrieves a list of CVM file groups from the catalog that need data processing.

        Files are selected if they are active and their last_updated timestamp is null
        or older than their last_download timestamp. It then finds the corresponding
        downloaded files in the history folder.

        Args:
            kind (Optional[str], optional): Filter by data kind (e.g., 'IF_POSITION'). Defaults to None (all kinds).
            history (Optional[bool], optional): Filter by history flag. Defaults to None (both).

        Returns:
            List[Tuple[str, str, bool, Tuple[str, ...]]]: A list of tuples. Each tuple contains:
                - kind (str): The kind of CVM file group.
                - name (str): The base name of the CVM file group (e.g., 'inf_diario_fi_202312').
                - history (bool): Flag indicating if the file group is historical.
                - files (Tuple[str, ...]): A tuple of full paths to the actual downloaded file(s)
                                           in the history folder corresponding to this group.

        Raises:
            ValueError: If fetching from the catalog fails.
            ConnectionError: If the database connection is invalid.
        """
        step = 'QUERYING CATALOG FOR FILES TO PROCESS'
        if not FI.is_valid_db_connection(self.CATALOG):
             raise ConnectionError("Catalog database connection is not valid.")

        try:
            # Compare ISO date strings directly
            query = f"""
                SELECT kind, name, history -- Select distinct groups
                FROM {self.CATALOG_JOURNAL_TABLE}
                WHERE active = 1
                AND (last_updated IS NULL OR last_download > last_updated)
            """
            params: List[Any] = []
            if kind is not None:
                query += " AND kind = ?"
                params.append(kind)
            if history is not None:
                query += " AND history = ?"
                params.append(int(history)) # Convert bool to int for query

            # Ensure we only get one entry per logical file group (kind, name, history)
            query += " GROUP BY kind, name, history ORDER BY kind, name"

            files_to_process_df = pd.read_sql(query, con=self.CATALOG, params=params)

            if files_to_process_df.empty:
                print("No CVM files found in catalog needing data processing.")
                return []

            step = 'FINDING ACTUAL FILES IN HISTORY FOLDER'
            result = []
            for record in files_to_process_df.to_dict(orient='records'):
                file_kind = record['kind']
                file_name = record['name'] # This is the base name (e.g., inf_diario_fi_YYYYMM)
                file_history = bool(record['history']) # Convert back to bool

                # Construct search pattern based on how files are saved by write_target_file
                # Pattern: kind.name.* (or more specific if needed)
                # Ensure case-insensitivity if OS filesystem might be case-sensitive
                search_pattern = f"{file_kind.lower()}.{file_name.lower()}.*"
                try:
                    # Use fbpyutils find function
                    found_files = FU.find(self.HISTORY_FOLDER, search_pattern)
                    if found_files:
                        # Sort files for consistent order (e.g., if multiple parts from zip)
                        result.append((file_kind, file_name, file_history, tuple(sorted(found_files))))
                    else:
                        # This indicates an inconsistency: catalog says process, but file missing
                        print(f"CRITICAL WARNING: Catalog indicates file group '{file_name}' (Kind: {file_kind}, History: {file_history}) needs processing, but no files found in {self.HISTORY_FOLDER} matching pattern '{search_pattern}'. Check download integrity or catalog status.")
                        # Optionally: Mark this entry as errored in the catalog?
                except Exception as find_err:
                     print(f"Error searching for files for group {file_name} (Kind: {file_kind}): {find_err}")


            print(f"Found {len(result)} CVM file groups needing data processing.")
            return result

        except (sqlite3.Error, pd.io.sql.DatabaseError) as e:
            info = debug_info(e)
            raise ValueError(f'Failed to get CVM files to process from catalog at step {step}: {e} ({info})')


    def get_cvm_file_data(self, cvm_file_path: str, check_header: bool = False) -> Tuple[str, str, pd.DataFrame, List[str]]:
        """
        Reads and processes data from a single downloaded CVM file using stored header mappings.

        Args:
            cvm_file_path (str): The full path to the downloaded CVM file in the history folder.
            check_header (bool, optional): Verify if the file header matches known mappings before processing.
                                           Defaults to False.

        Returns:
            Tuple[str, str, pd.DataFrame, List[str]]: Result from file_io.read_cvm_history_file:
                (kind, sub_kind, processed_data_df, partition_columns)

        Raises:
            FileNotFoundError: If the cvm_file_path does not exist.
            ValueError: If header check fails or processing errors occur (propagated from read_cvm_history_file).
        """
        if not os.path.exists(cvm_file_path):
             raise FileNotFoundError(f"CVM file not found: {cvm_file_path}")

        # Pass the pre-loaded headers DataFrame to the reading function
        # This assumes self.HEADERS_DF was correctly initialized
        if self.HEADERS_DF is None or self.HEADERS_DF.empty:
             raise RuntimeError("CVM client was not properly initialized with headers_df.")

        return read_cvm_history_file(
            source_file=cvm_file_path,
            headers_df=self.HEADERS_DF,
            apply_conversions=True, # Typically want converted data
            check_header=check_header
        )


    def mark_cvm_files_updated(self, processed_files_info: List[Tuple[str, str]]) -> bool:
        """
        Updates the 'last_updated' timestamp in the catalog journal for successfully processed file groups.

        Args:
            processed_files_info (List[Tuple[str, str]]): A list of tuples, where each tuple
                contains (kind, name) of the file group that was successfully processed and loaded.

        Returns:
            bool: True if the update operations were successful, False otherwise.

        Raises:
            ValueError: If updating the catalog fails.
            ConnectionError: If the database connection is invalid.
        """
        step = 'MARKING FILES AS UPDATED IN CATALOG'
        if not FI.is_valid_db_connection(self.CATALOG):
             raise ConnectionError("Catalog database connection is not valid.")

        if not processed_files_info:
            print("No processed files provided to mark as updated.")
            return True # Nothing to do, considered successful

        try:
            update_time_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # Update based on kind and name, targeting active files
            update_sql = f"""
                UPDATE {self.CATALOG_JOURNAL_TABLE}
                SET last_updated = ?
                WHERE active = 1
                  AND kind = ?
                  AND name = ?
                  -- Only update if it was actually downloaded
                  AND last_download IS NOT NULL
                  -- Optional: Only update if last_updated was older?
                  -- AND (last_updated IS NULL OR last_updated < ?)
            """
            # Prepare data for executemany: list of (update_time_str, kind, name) tuples
            update_data = [(update_time_str, kind, name) for kind, name in processed_files_info]

            cursor = self.CATALOG.cursor()
            cursor.executemany(update_sql, update_data)
            updated_count = cursor.rowcount
            self.CATALOG.commit()

            print(f"Marked {updated_count} file groups as updated (data processed) in the catalog.")
            # Check if updated_count matches len(processed_files_info) for verification
            if updated_count != len(processed_files_info):
                 # This could happen if a file group had multiple entries (e.g. from zip) but only one needs update marker
                 # Or if the WHERE clause didn't match (e.g., active=0 or last_download is NULL)
                 print(f"Warning: Attempted to mark {len(processed_files_info)} groups, but updated {updated_count} rows in catalog. This might be expected or indicate an issue.")

            return True
        except sqlite3.Error as e:
            info = debug_info(e)
            self.CATALOG.rollback()
            raise ValueError(f'Failed to mark CVM files as updated in catalog at step {step}: {e} ({info})')
