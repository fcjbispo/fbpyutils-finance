import os
import re
import io
import requests
import bs4
import pandas as pd
from zipfile import ZipFile, BadZipFile  # Import BadZipFile for specific error handling
from datetime import datetime
from urllib import request, error as urllib_error  # Import specific error
from typing import Optional, Dict, List, Tuple, Any

# Assuming fbpyutils.file has magic attribute correctly configured
# If not, python-magic needs to be installed and imported directly
try:
    import magic
except ImportError:
    magic = None  # type: ignore
    print(
        "Warning: 'python-magic' library not found. MIME type detection will be limited."
    )


from fbpyutils.debug import debug_info

# Import necessary functions from other modules
from .utils import (
    make_number_type,
    make_datetime,
    make_str_datetime,
    is_nan_or_empty,
)
from .file_io import write_target_file  # write_target_file moved to file_io.py

# --- Constantes ---
SOURCE_ENCODING, TARGET_ENCODING = "iso-8859-1", "utf-8"

# --- Funções de Interação Remota ---


def get_url_paths(url: str, params: Optional[Dict] = None) -> pd.DataFrame:
    """
    Fetches and parses a directory listing page from a CVM URL (typically Apache format).

    Extracts file/directory information like name, last modified date, and size.

    Args:
        url (str): The URL of the directory listing page.
        params (Optional[Dict], optional): Query parameters for the request. Defaults to None.

    Returns:
        pd.DataFrame: DataFrame containing the extracted information with columns:
                      'sequence', 'href', 'name', 'last_modified', 'size'.
                      Returns an empty DataFrame if the request fails or parsing is unsuccessful.

    Raises:
        requests.exceptions.RequestException: If the HTTP request fails.
    """
    params = params or {}
    print(f"Fetching directory listing from: {url}")
    try:
        response = requests.get(url, params=params, timeout=60)  # Added timeout
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL {url}: {e}")
        # Decide whether to raise or return empty DataFrame
        # Raising might be better to signal failure clearly
        raise

    soup = bs4.BeautifulSoup(response.text, "html.parser")
    # Find the main table or preformatted text block containing the listing
    # CVM pages often use <pre> tags
    pre_tags = soup.find_all("pre")
    links = []
    if pre_tags:
        # Assume the first <pre> tag contains the relevant links
        links = pre_tags[0].find_all("a")
    else:
        # Fallback: look for links directly within the body if no <pre> found
        print(f"Warning: No <pre> tag found at {url}. Searching body for links.")
        links = soup.body.find_all("a") if soup.body else []

    directory_data = []
    sequence = 0
    for link in links:
        href = link.get("href")
        link_text = link.text.strip()

        # Basic filtering: ignore query string links, parent directory, etc.
        if (
            not href
            or href.startswith("?")
            or href.startswith("#")
            or link_text == "[To Parent Directory]"
        ):
            continue
        # Ignore links that are likely directories themselves if needed (often end with '/')
        is_directory = href.endswith("/")
        # if is_directory: continue # Uncomment to skip directories

        # Try to extract metadata from the surrounding text (this is fragile)
        # Apache format often has: [ICON] NAME LAST_MODIFIED SIZE DESCRIPTION
        # We primarily rely on the link and its text. Size/Date might be in adjacent text nodes.
        parent = link.parent
        line_text = (
            parent.text.strip() if parent else ""
        )  # Get text of the line containing the link

        name = (
            href.split("/")[-1].replace("/", "") if href else link_text
        )  # Use href for name if possible
        base_name = name.split(".")[0] if "." in name else name

        last_modified_str = None
        size_str = None

        # Attempt to parse date/time/size from the line text (highly dependent on format)
        # Example regex for Apache format: (\d{2}-\w{3}-\d{4}\s+\d{2}:\d{2})\s+([\d.]+[KMG]?)
        # This is complex and prone to errors. Let's extract basic info first.
        # A simpler approach might be needed if the format varies.
        # For now, we'll extract from the link and potentially add date/size later if parsing is reliable.

        # Placeholder for size/date extraction logic - requires inspecting actual HTML structure
        size = None
        last_modified_dt = None

        # Example: Try finding date/time near the link text within the line
        match_dt = re.search(r"(\d{2}-\w{3}-\d{4}\s+\d{2}:\d{2})", line_text)
        if match_dt:
            last_modified_str = match_dt.group(1)
            last_modified_dt = make_datetime(
                last_modified_str.split()[0], last_modified_str.split()[1]
            )

        # Example: Try finding size (digits, possibly with K/M/G)
        match_size = re.search(
            r"\s([\d,.-]+[KMG]?)\s*$", line_text
        )  # Look near the end
        if match_size:
            size_str = match_size.group(1).strip()
            # Convert K/M/G? For now, just store the string or try basic conversion
            size = make_number_type(size_str)  # Basic attempt

        directory_data.append(
            (
                sequence,
                href,
                base_name,  # Use base name without extension
                make_str_datetime(last_modified_dt) if last_modified_dt else None,
                size if not is_directory else None,  # Size is None for directories
            )
        )
        sequence += 1

    headers = ["sequence", "href", "name", "last_modified", "size"]
    if not directory_data:
        print(f"Warning: No valid file/directory links extracted from {url}")
        return pd.DataFrame(
            columns=headers
        )  # Return empty DataFrame with correct columns

    directory_df = pd.DataFrame(directory_data, columns=headers)
    return directory_df.sort_values(by="sequence", ascending=True)


def get_remote_files_list(
    kind: str, current_url: str, history_url: str
) -> pd.DataFrame:
    """
    Retrieves and combines file listings from current and historical CVM data URLs.

    Args:
        kind (str): A label for the type of data (e.g., 'IF_REGISTER', 'IF_POSITION').
        current_url (str): The URL for the current data directory.
        history_url (str): The URL for the historical data directory.

    Returns:
        pd.DataFrame: A combined DataFrame containing file information from both URLs,
                      with an added 'history' column (boolean) and 'kind' column.
                      Filters out entries without a 'size' (likely directories).
                      Constructs the full 'url' for each file.
    """
    current_dir = pd.DataFrame()
    history_dir = pd.DataFrame()

    try:
        current_dir = get_url_paths(current_url)
        if not current_dir.empty:
            current_dir["history"] = False
            current_dir["url_base"] = (
                current_url  # Store base URL for later construction
            )
    except requests.exceptions.RequestException as e:
        print(
            f"Warning: Failed to fetch current directory listing for {kind} from {current_url}: {e}"
        )
        # Continue, current_dir remains empty

    try:
        history_dir = get_url_paths(history_url)
        if not history_dir.empty:
            history_dir["history"] = True
            history_dir["url_base"] = history_url  # Store base URL
    except requests.exceptions.RequestException as e:
        print(
            f"Warning: Failed to fetch history directory listing for {kind} from {history_url}: {e}"
        )
        # Continue, history_dir remains empty

    if current_dir.empty and history_dir.empty:
        print(f"Warning: Could not fetch any file listings for kind '{kind}'.")
        return pd.DataFrame()  # Return empty if both failed

    # Concatenate, handling potential empty DataFrames
    files_dir = pd.concat([current_dir, history_dir], ignore_index=True)

    # Filter out entries without a size (likely directories or parsing errors)
    # Also filter out entries where last_modified is None, as these are often problematic
    files_dir = files_dir.dropna(subset=["size", "last_modified"]).copy()

    if files_dir.empty:
        print(
            f"Warning: No valid files with size and modification date found for kind '{kind}'."
        )
        return files_dir  # Return early if no valid files found

    files_dir["kind"] = kind
    # Construct full URL - ensure no double slashes
    files_dir["url"] = files_dir.apply(
        lambda x: f"{x['url_base'].rstrip('/')}/{x['href'].lstrip('/')}", axis=1
    )
    files_dir = files_dir.drop(columns=["url_base"])  # Remove temporary column

    return files_dir


def update_cvm_history_file(
    if_metadata: Dict[str, Any],
) -> List[Tuple[str, Dict[str, Any], str]]:
    """
    Downloads and saves a CVM file if it's new or updated based on metadata.

    Handles both direct text files and zipped files containing text files.

    Args:
        if_metadata (Dict[str, Any]): A dictionary containing metadata for the file, including:
            'url': The URL to download from.
            'last_modified': The last modified timestamp from the remote server (as string).
            'last_download': The timestamp of the last successful download (as string or None).
            'history_folder': The local folder to save the downloaded file(s).
            'kind': The kind of data (used in the output filename).
            'href': The original filename from the listing (used in the output filename).

    Returns:
        List[Tuple[str, Dict[str, Any], str]]: A list containing status tuples for the operation.
            Each tuple: (status_code, updated_metadata, message).
            Status codes: 'SUCCESS', 'ERROR', 'SKIP'.
            updated_metadata includes 'last_download' and 'history_file' on success.
    """
    results = []
    should_download = False
    url = if_metadata.get("url")
    last_modified_str = if_metadata.get("last_modified")
    last_download_str = if_metadata.get("last_download")

    if not url:
        results.append(("ERROR", if_metadata, "Missing 'url' in metadata."))
        return results
    if not last_modified_str:
        # If remote last_modified is missing, we can't reliably check for updates.
        # Decide policy: always download, or skip? Let's skip for safety.
        results.append(
            (
                "SKIP",
                if_metadata,
                f"Skipping {url}: Missing remote 'last_modified' date.",
            )
        )
        return results

    # Convert string dates from metadata to datetime objects for comparison
    last_modified_dt = None
    last_download_dt = None
    try:
        # Use pandas to_datetime for robust parsing
        last_modified_dt = pd.to_datetime(last_modified_str, errors="coerce")
        if pd.isna(last_modified_dt):
            raise ValueError(f"Could not parse last_modified date: {last_modified_str}")

        if last_download_str and not is_nan_or_empty(last_download_str):
            last_download_dt = pd.to_datetime(last_download_str, errors="coerce")
            if pd.isna(last_download_dt):
                print(
                    f"Warning: Could not parse last_download date '{last_download_str}' for {url}. Will force download."
                )
                last_download_dt = None  # Treat as never downloaded if parse fails

    except Exception as e:
        print(f"Warning: Date parsing error for {url}: {e}. Proceeding cautiously.")
        # If dates can't be parsed, download if last_download is missing/invalid
        if last_download_dt is None:
            should_download = True

    # Determine if download is needed based on parsed dates
    if not should_download:  # Only check if not already forced by parse error
        if last_download_dt is None:
            should_download = True
            print(f"Scheduling download for {url}: Never downloaded.")
        elif last_modified_dt > last_download_dt:
            should_download = True
            print(
                f"Scheduling download for {url}: Remote is newer ({last_modified_dt} > {last_download_dt})."
            )
        else:
            print(
                f"Skipping download for {url}: Already up-to-date (Local: {last_download_dt}, Remote: {last_modified_dt})."
            )

    if not should_download:
        results.append(("SKIP", if_metadata, f"Already up-to-date: {url}"))
        return results

    # --- Proceed with download ---
    try:
        print(f"Attempting download: {url}")
        # Use urllib.request for potential compatibility, add user-agent
        headers = {"User-Agent": "Mozilla/5.0"}
        req = request.Request(url, headers=headers)
        with request.urlopen(req, timeout=180) as response:  # Increased timeout
            if response.status != 200:
                raise urllib_error.HTTPError(
                    url, response.status, "Failed to download", response.headers, None
                )
            data = response.read()
            content_type_header = response.info().get("Content-Type", "").lower()

        download_time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Downloaded {len(data)} bytes from {url}")

        # --- Identify file type ---
        mime_type_main = None
        if magic:
            try:
                mime_type = magic.from_buffer(data, mime=True)
                mime_type_main = mime_type.split(";")[0].strip()
                print(f"Detected MIME type (magic): {mime_type} for {url}")
            except Exception as magic_err:
                print(
                    f"Warning: python-magic failed for {url}: {magic_err}. Falling back on Content-Type/extension."
                )
                magic = None  # Disable magic if it errors once

        if mime_type_main is None:
            # Fallback using Content-Type header or file extension
            if "zip" in content_type_header or url.lower().endswith(".zip"):
                mime_type_main = "application/zip"
            elif "text" in content_type_header or content_type_header.startswith(
                "application/csv"
            ):
                mime_type_main = "text/plain"  # Treat as text
            else:
                # Assume text as a last resort, but warn
                print(
                    f"Warning: Could not determine MIME type for {url} (Content-Type: {content_type_header}). Assuming text."
                )
                mime_type_main = "text/plain"

        # --- Process based on type ---
        text_mime_patterns = (
            "text/",
            "application/csv",
            "application/json",
        )  # Add more text types if needed
        zip_mime_types = ("application/zip", "application/x-zip-compressed")

        if any(pattern in mime_type_main for pattern in zip_mime_types):
            print(f"Processing as ZIP file: {url}")
            try:
                with ZipFile(io.BytesIO(data)) as zip_file:
                    if not zip_file.namelist():
                        print(f"Warning: ZIP file is empty: {url}")
                        results.append(
                            (
                                "ERROR",
                                if_metadata,
                                f"Downloaded ZIP file is empty: {url}",
                            )
                        )
                        return results

                    for k, filename_in_zip in enumerate(zip_file.namelist()):
                        print(
                            f"Extracting {filename_in_zip} from {if_metadata['href']}"
                        )
                        try:
                            file_content = zip_file.read(filename_in_zip)
                        except Exception as read_zip_e:
                            print(
                                f"ERROR reading {filename_in_zip} from zip {url}: {read_zip_e}"
                            )
                            results.append(
                                (
                                    "ERROR",
                                    if_metadata,
                                    f"Failed reading {filename_in_zip} from {if_metadata['href']}: {read_zip_e}",
                                )
                            )
                            continue  # Skip this file within the zip

                        # Decode using source encoding, handle potential errors
                        decoded_content = None
                        try:
                            decoded_content = file_content.decode(SOURCE_ENCODING)
                        except UnicodeDecodeError:
                            print(
                                f"Warning: Failed to decode {filename_in_zip} with {SOURCE_ENCODING}, trying {TARGET_ENCODING}."
                            )
                            try:
                                decoded_content = file_content.decode(TARGET_ENCODING)
                            except UnicodeDecodeError as ude:
                                print(
                                    f"ERROR: Could not decode {filename_in_zip} with known encodings. Skipping file. Error: {ude}"
                                )
                                results.append(
                                    (
                                        "ERROR",
                                        if_metadata,
                                        f"Failed to decode {filename_in_zip} inside {if_metadata['href']}",
                                    )
                                )
                                continue  # Skip this file within the zip

                        # Write extracted file
                        try:
                            file_ext_in_zip = (
                                filename_in_zip.split(".")[-1]
                                if "." in filename_in_zip
                                else "txt"
                            )
                            target_file_path = write_target_file(
                                decoded_content,
                                if_metadata,
                                if_metadata["history_folder"],
                                index=k,
                                file_ext=file_ext_in_zip,
                                encoding=TARGET_ENCODING,
                            )
                            # Create a copy of metadata for each file in the zip
                            file_specific_metadata = if_metadata.copy()
                            file_specific_metadata["last_download"] = download_time_str
                            file_specific_metadata["history_file"] = os.path.basename(
                                target_file_path
                            )
                            # Add original filename from zip for context
                            file_specific_metadata["original_zip_filename"] = (
                                filename_in_zip
                            )
                            results.append(
                                (
                                    "SUCCESS",
                                    file_specific_metadata,
                                    f"{target_file_path} written from {filename_in_zip} in {url}",
                                )
                            )
                        except IOError as write_e:
                            print(
                                f"ERROR writing extracted file {filename_in_zip} from {url}: {write_e}"
                            )
                            results.append(
                                (
                                    "ERROR",
                                    if_metadata,
                                    f"Failed writing extracted file {filename_in_zip}: {write_e}",
                                )
                            )
                            # Continue to next file in zip

            except BadZipFile:
                print(f"ERROR: File downloaded from {url} is not a valid ZIP file.")
                results.append(
                    ("ERROR", if_metadata, f"Invalid ZIP file downloaded from {url}")
                )
            except Exception as zip_e:
                print(f"ERROR processing ZIP file {url}: {zip_e}")
                info = debug_info(zip_e)
                results.append(
                    (
                        "ERROR",
                        if_metadata,
                        f"Failure processing zip file: {zip_e} ({info}) for url:{url}",
                    )
                )

        # Check if it's likely a text file
        elif any(pattern in mime_type_main for pattern in text_mime_patterns):
            print(f"Processing as text file: {url}")
            decoded_content = None
            try:
                decoded_content = data.decode(SOURCE_ENCODING)
            except UnicodeDecodeError:
                print(
                    f"Warning: Failed to decode {if_metadata['href']} with {SOURCE_ENCODING}, trying {TARGET_ENCODING}."
                )
                try:
                    decoded_content = data.decode(TARGET_ENCODING)
                except UnicodeDecodeError as ude:
                    print(
                        f"ERROR: Could not decode {if_metadata['href']} with known encodings. Skipping file. Error: {ude}"
                    )
                    results.append(
                        (
                            "ERROR",
                            if_metadata,
                            f"Failed to decode {if_metadata['href']}",
                        )
                    )
                    return results  # Stop processing this URL if decoding fails

            try:
                target_file_path = write_target_file(
                    decoded_content,
                    if_metadata,
                    if_metadata["history_folder"],
                    encoding=TARGET_ENCODING,
                )
                if_metadata["last_download"] = download_time_str
                if_metadata["history_file"] = os.path.basename(target_file_path)
                results.append(
                    ("SUCCESS", if_metadata, f"{target_file_path} written from {url}")
                )
            except IOError as write_e:
                print(f"ERROR writing text file from {url}: {write_e}")
                results.append(
                    ("ERROR", if_metadata, f"Failed writing text file: {write_e}")
                )

        else:
            # Handle unknown/unsupported types - maybe save raw bytes?
            print(
                f"ERROR: Unknown or unsupported MIME type: {mime_type_main} for url: {url}"
            )
            # Option: Save raw bytes with a generic extension like .bin
            # try:
            #     target_file = build_target_file_name(if_metadata, if_metadata['history_folder'], file_ext='bin')
            #     with open(target_file, 'wb') as f:
            #         f.write(data)
            #     results.append(('ERROR', if_metadata, f'Saved raw unsupported file ({mime_type_main}) to {target_file} from {url}'))
            # except IOError as write_e:
            #      results.append(('ERROR', if_metadata, f'Failed saving raw unsupported file ({mime_type_main}) from {url}: {write_e}'))
            results.append(
                (
                    "ERROR",
                    if_metadata,
                    f"Unknown/unsupported mime type: {mime_type_main} for url:{url}",
                )
            )

    except (urllib_error.URLError, urllib_error.HTTPError) as e:
        print(f"ERROR: Network/HTTP error downloading {url}: {e}")
        info = debug_info(e)
        results.append(
            ("ERROR", if_metadata, f"Network/HTTP error: {e} ({info}) for url:{url}")
        )
    except Exception as e:
        print(f"ERROR: Unexpected error processing {url}: {e}")
        info = debug_info(e)
        results.append(
            (
                "ERROR",
                if_metadata,
                f"Failure processing remote data: {e} ({info}) for url:{url}",
            )
        )

    # Ensure results list is never empty if processing was attempted
    if not results:
        results.append(
            ("ERROR", if_metadata, f"Unknown error occurred during processing of {url}")
        )

    return results
