import os
import pandas as pd
from typing import List, Tuple, Dict, Set, Any

from fbpyutils.debug import debug_info
from .utils import hash_string

# Need get_expression_and_converters for the logic in get_cvm_updated_headers
# This creates a potential circular dependency if processing also imports headers.
# Consider refactoring if this becomes an issue. Maybe move get_expression_and_converters to utils?
# For now, keep it here as it was in the original structure implicitly.

# --- Constantes ---
# Header file paths are typically loaded from the main __init__.py
# and passed to functions or classes that need them.

# --- Funções de Cabeçalho ---


def get_cvm_file_metadata(cvm_file_path: str) -> Tuple[str, str, str, str]:
    """
    Analyzes a CVM file path to extract metadata: kind, sub-kind, header line, and header hash.

    Args:
        cvm_file_path (str): The full path to the CVM file.

    Returns:
        Tuple[str, str, str, str]: A tuple containing:
            - kind (str): The main category (e.g., 'IF_REGISTER', 'IF_POSITION'). Uppercase.
            - sub_kind (str): The specific type within the kind (e.g., 'CAD_FI', 'DIARIO_FI'). Uppercase.
            - header_line (str): The first line of the file (header).
            - header_hash (str): SHA-256 hash of the combined kind, sub-kind, and header line.

    Raises:
        FileNotFoundError: If the cvm_file_path does not exist.
        IOError: If the file cannot be read.
        ValueError: If the filename format is unexpected and kind/sub-kind cannot be determined.
        UnicodeDecodeError: If the file cannot be decoded using UTF-8.
    """
    if not os.path.exists(cvm_file_path):
        raise FileNotFoundError(f"CVM file not found: {cvm_file_path}")

    try:
        # Attempt to read with utf-8 first, fallback to iso-8859-1 if needed
        try:
            with open(cvm_file_path, "r", encoding="utf-8") as f:
                header_line = (
                    f.readline().strip()
                )  # Read first line and remove trailing newline
        except UnicodeDecodeError:
            print(
                f"Warning: Decoding {cvm_file_path} as utf-8 failed, trying iso-8859-1."
            )
            with open(cvm_file_path, "r", encoding="iso-8859-1") as f:
                header_line = f.readline().strip()

    except IOError as e:
        raise IOError(f"Could not read CVM file: {cvm_file_path} - {e}")
    except Exception as e:  # Catch other potential file reading errors
        raise IOError(f"Unexpected error reading CVM file: {cvm_file_path} - {e}")

    file_name = os.path.basename(cvm_file_path)
    file_name_parts = file_name.split(".")

    # Example filename format: if_register.inf_cadastral_fi_20231231.csv
    # Or: if_position.inf_diario_fi_202312.csv
    # Or: if_register.cad_fi.csv (current register)
    if len(file_name_parts) < 3:
        # Handle cases like 'if_register.cad_fi.zip' -> parts = ['if_register', 'cad_fi', 'zip']
        # Or 'if_register.cad_fi.csv' -> parts = ['if_register', 'cad_fi', 'csv']
        # Allow 2 parts only if it's like 'if_register.cad_fi' (unlikely from CVM)
        # Let's assume at least kind.subkind.ext
        raise ValueError(f"Unexpected filename format (too few parts): {file_name}")

    kind = file_name_parts[0].upper()  # e.g., IF_REGISTER
    metadata_part = file_name_parts[
        1
    ].lower()  # e.g., inf_cadastral_fi_20231231 or cad_fi

    # Determine sub_kind based on patterns
    if metadata_part == "cad_fi" or metadata_part.startswith("inf_cadastral_fi"):
        sub_kind = "CAD_FI"
    elif metadata_part.startswith("inf_diario_fi"):
        sub_kind = "DIARIO_FI"
    # Add more rules here if other sub_kinds exist based on filename patterns
    else:
        # Fallback or raise error if pattern is unknown
        print(
            f"Warning: Unknown sub_kind pattern in filename: {file_name}. Using '{metadata_part.upper()}' as sub_kind."
        )
        sub_kind = metadata_part.upper()
        # Alternatively: raise ValueError(f"Cannot determine sub_kind from filename part: {metadata_part}")

    # Generate hash based on determined kind, sub_kind, and the actual header line content
    hash_input = ";".join([kind, sub_kind, header_line])
    header_hash = hash_string(hash_input)

    return kind, sub_kind, header_line, header_hash


def get_cvm_updated_headers(
    cvm_files: List[str],
    header_mappings_df: pd.DataFrame,
    current_headers_df: pd.DataFrame,
) -> List[Dict[str, Any]]:
    """
    Compares headers from CVM files against existing mappings and identifies new/changed headers.

    Generates a consolidated list of header mapping dictionaries, marking new ones.

    Args:
        cvm_files (List[str]): List of paths to CVM files to analyze.
        header_mappings_df (pd.DataFrame): DataFrame loaded from HEADER_MAPPINGS_FILE.
        current_headers_df (pd.DataFrame): DataFrame loaded from HEADERS_FILE (current state).

    Returns:
        List[Dict[str, Any]]: A list of dictionaries, each representing a complete header mapping row
                              (similar to the structure in HEADERS_FILE), including an 'Is_New' flag.

    Raises:
        ValueError: If input lists/DataFrames are invalid or essential data is missing.
        Exception: For unexpected errors during processing.
    """
    step = "SETTING UP COMPONENTS"
    # No need for SQLite stage here, using pandas directly
    try:
        step = "VALIDATING INPUTS"
        if cvm_files is None or not isinstance(cvm_files, list):
            # Allow empty list, just return current headers
            if not cvm_files:
                print(
                    "Warning: Empty cvm_files list provided to get_cvm_updated_headers."
                )
                return (
                    current_headers_df.to_dict("records")
                    if not current_headers_df.empty
                    else []
                )
            else:
                raise ValueError("cvm_files must be a list.")

        if header_mappings_df is None or header_mappings_df.empty:
            raise ValueError("Header Mappings DataFrame cannot be empty.")
        # current_headers_df can be None or empty if it's the first run
        if current_headers_df is None:
            current_headers_df = pd.DataFrame()  # Treat as empty

        step = "LOADING HEADER MAPPINGS TEMPLATES"
        # Create a dictionary mapping Kind -> list of mapping templates
        header_template_map: Dict[str, List[Dict[str, Any]]] = {}
        required_mapping_cols = [
            "Kind",
            "Order",
            "Target_Field",
            "Source_Field",
            "Transformation1",
            "Transformation2",
            "Transformation3",
            "Converter",
        ]
        if not all(col in header_mappings_df.columns for col in required_mapping_cols):
            # Check for case variations too
            cols_lower = [c.lower() for c in header_mappings_df.columns]
            if not all(col.lower() in cols_lower for col in required_mapping_cols):
                raise ValueError(
                    f"Header Mappings DataFrame is missing required columns (case-insensitive check failed): {required_mapping_cols}"
                )
            else:
                # Normalize column names in the mapping df if needed
                header_mappings_df.columns = [
                    c.lower() for c in header_mappings_df.columns
                ]

        # Group mappings by 'Kind' directly from the DataFrame
        # Ensure 'Kind' column exists and handle potential case issues
        kind_col = next(
            (col for col in header_mappings_df.columns if col.lower() == "kind"), None
        )
        order_col = next(
            (col for col in header_mappings_df.columns if col.lower() == "order"), None
        )
        if not kind_col or not order_col:
            raise ValueError(
                "Header Mappings DataFrame must contain 'Kind' and 'Order' columns."
            )

        for kind, group in header_mappings_df.groupby(kind_col):
            # Sort by order within each group and convert to dict
            header_template_map[kind] = group.sort_values(order_col).to_dict("records")

        step = "EXTRACTING HEADERS FROM SOURCE FILES"
        if_source_headers: Set[Tuple[str, str, str, str]] = set()
        processed_files_count = 0
        for cvm_file_path in cvm_files:
            try:
                kind, sub_kind, header, header_hash = get_cvm_file_metadata(
                    cvm_file_path
                )
                if_source_headers.add((kind, sub_kind, header, header_hash))
                processed_files_count += 1
            except FileNotFoundError:
                print(f"Warning: File not found, skipping: {cvm_file_path}")
            except (ValueError, IOError, UnicodeDecodeError) as e:
                print(
                    f"Warning: Skipping file due to metadata extraction error: {cvm_file_path} - {e}"
                )
            except Exception as e:
                print(
                    f"Warning: Unexpected error processing file, skipping: {cvm_file_path} - {e}"
                )

        if not if_source_headers:
            print("Warning: No valid headers extracted from the provided CVM files.")
            # Return current mappings if no new headers found
            return (
                current_headers_df.to_dict("records")
                if not current_headers_df.empty
                else []
            )

        step = "PREPARING CURRENT MAPPINGS"
        # Use current_headers_df directly
        existing_mappings_list = (
            current_headers_df.to_dict("records")
            if not current_headers_df.empty
            else []
        )
        # Add 'Is_New' flag = False to existing mappings
        hash_col_current = (
            next(
                (col for col in current_headers_df.columns if col.lower() == "hash"),
                None,
            )
            if not current_headers_df.empty
            else None
        )
        existing_hashes = (
            set(m.get(hash_col_current) for m in existing_mappings_list)
            if hash_col_current
            else set()
        )

        for mapping in existing_mappings_list:
            mapping["Is_New"] = False

        step = "COMPUTING NEW/CHANGED HEADERS"
        consolidated_mappings = list(existing_mappings_list)  # Start with existing ones

        for kind, sub_kind, header, header_hash in if_source_headers:
            if header_hash not in existing_hashes:
                print(
                    f"New header hash detected: {header_hash} for Kind={kind}, SubKind={sub_kind}"
                )
                # Find the appropriate template mapping based on Kind
                if kind not in header_template_map:
                    print(
                        f"Warning: No header mapping template found for Kind='{kind}'. Cannot process hash {header_hash}."
                    )
                    continue

                header_template = header_template_map[kind]
                source_fields_in_file = header.split(";")

                # Generate new mapping entries based on the template
                max_order_in_template = 0
                mapped_source_fields_for_this_hash = set()

                # Find correct case for columns in template dicts
                template_keys = header_template[0].keys() if header_template else []
                t_order_col = next(
                    (k for k in template_keys if k.lower() == "order"), "Order"
                )
                t_target_col = next(
                    (k for k in template_keys if k.lower() == "target_field"),
                    "Target_Field",
                )
                t_source_col = next(
                    (k for k in template_keys if k.lower() == "source_field"),
                    "Source_Field",
                )
                t_trans1_col = next(
                    (k for k in template_keys if k.lower() == "transformation1"),
                    "Transformation1",
                )
                t_trans2_col = next(
                    (k for k in template_keys if k.lower() == "transformation2"),
                    "Transformation2",
                )
                t_trans3_col = next(
                    (k for k in template_keys if k.lower() == "transformation3"),
                    "Transformation3",
                )
                t_conv_col = next(
                    (k for k in template_keys if k.lower() == "converter"), "Converter"
                )

                for template_map in header_template:
                    target_field = template_map.get(t_target_col)
                    source_field = template_map.get(t_source_col)
                    order = int(template_map.get(t_order_col, 0))
                    max_order_in_template = max(max_order_in_template, order)

                    # Check if the source field from the template exists in the actual file header
                    found = (
                        source_field is not None
                        and source_field in source_fields_in_file
                    )

                    new_map_entry = {
                        "Kind": kind,
                        "Sub_Kind": sub_kind,
                        "Header": header,  # The actual header string from the file
                        "Hash": header_hash,
                        "Order": order,
                        "Target_Field": target_field,
                        "Source_Field": source_field if found else None,
                        "Transformation1": template_map.get(t_trans1_col)
                        if found
                        else None,
                        "Transformation2": template_map.get(t_trans2_col)
                        if found
                        else None,
                        "Transformation3": template_map.get(t_trans3_col)
                        if found
                        else None,
                        "Converter": template_map.get(t_conv_col) if found else None,
                        "Is_New": True,
                    }
                    consolidated_mappings.append(new_map_entry)
                    if found:
                        mapped_source_fields_for_this_hash.add(source_field)

                # Add any fields present in the file but not mapped by the template
                current_order = max_order_in_template
                for field_in_file in source_fields_in_file:
                    if field_in_file not in mapped_source_fields_for_this_hash:
                        current_order += 1
                        print(
                            f"  -> Found unmapped source field: '{field_in_file}' in hash {header_hash}. Adding with Order={current_order}."
                        )
                        unmapped_entry = {
                            "Kind": kind,
                            "Sub_Kind": sub_kind,
                            "Header": header,
                            "Hash": header_hash,
                            "Order": current_order,
                            "Target_Field": None,  # No target defined in template
                            "Source_Field": field_in_file,
                            "Transformation1": None,
                            "Transformation2": None,
                            "Transformation3": None,
                            "Converter": None,
                            "Is_New": True,
                        }
                        consolidated_mappings.append(unmapped_entry)

                # Add the new hash to existing hashes to avoid processing duplicates if it appears multiple times
                existing_hashes.add(header_hash)

        # Sort the final list primarily by Hash, then by Order for consistency
        consolidated_mappings.sort(
            key=lambda x: (x.get("Hash", ""), int(x.get("Order", 0)))
        )

        return consolidated_mappings

    except Exception as E:
        info = debug_info(E)
        raise ValueError(
            f"Failed to get updated CVM headers at step {step}: {E} ({info})"
        )


def check_cvm_headers_changed(
    cvm_files: List[str], current_headers_df: pd.DataFrame
) -> Set[str]:
    """
    Checks if any headers in the provided CVM files are new compared to the current headers.

    Args:
        cvm_files (List[str]): List of paths to CVM files to check.
        current_headers_df (pd.DataFrame): DataFrame of the currently known headers (from HEADERS_FILE).
                                           Can be None or empty.

    Returns:
        Set[str]: A set containing the hashes of any new headers found. Empty set if no changes.

    Raises:
        ValueError: If processing fails.
    """
    step = "START"
    try:
        step = "READING CURRENT HEADERS INFO"
        if current_headers_df is None or current_headers_df.empty:
            existing_hashes = set()
        else:
            hash_col_current = next(
                (col for col in current_headers_df.columns if col.lower() == "hash"),
                None,
            )
            existing_hashes = (
                set(current_headers_df[hash_col_current]) if hash_col_current else set()
            )

        step = "EXTRACTING HEADERS FROM SOURCE FILES"
        source_header_hashes: Set[str] = set()
        processed_files_count = 0
        if not cvm_files:  # Handle empty input list
            print("Warning: Empty cvm_files list provided for header check.")
            return set()

        for cvm_file_path in cvm_files:
            try:
                _, _, _, header_hash = get_cvm_file_metadata(cvm_file_path)
                source_header_hashes.add(header_hash)
                processed_files_count += 1
            except FileNotFoundError:
                print(f"Warning: File not found, skipping check: {cvm_file_path}")
            except (ValueError, IOError, UnicodeDecodeError) as e:
                print(
                    f"Warning: Skipping file check due to metadata error: {cvm_file_path} - {e}"
                )
            except Exception as e:
                print(
                    f"Warning: Unexpected error processing file, skipping check: {cvm_file_path} - {e}"
                )

        if processed_files_count == 0:
            print("Warning: No CVM files could be processed for header check.")
            return set()

        step = "COMPARING HASHES"
        new_hashes = source_header_hashes - existing_hashes
        if new_hashes:
            print(f"Detected new header hashes: {new_hashes}")

        return new_hashes

    except Exception as E:
        info = debug_info(E)
        raise ValueError(
            f"Failed to check CVM headers changed at step {step}: {E} ({info})"
        )


def write_cvm_headers_mappings(mappings: List[Dict[str, Any]], file_path: str) -> bool:
    """
    Writes the consolidated header mappings list to an Excel file.

    Args:
        mappings (List[Dict[str, Any]]): The list of header mapping dictionaries to write.
        file_path (str): The full path to the output Excel file (e.g., HEADERS_FILE).

    Returns:
        bool: True if writing was successful, False otherwise.

    Raises:
        ValueError: If writing fails.
    """
    step = "VALIDATING INPUT"
    try:
        df_to_write = None
        if not mappings:
            print("No mappings provided to write.")
            # Decide if overwriting with empty is desired or should return False
            if os.path.exists(file_path):
                print(
                    f"Skipping write to {file_path} as mappings list is empty and file exists."
                )
                return False
            else:
                print(
                    f"Writing empty DataFrame to {file_path} as mappings list is empty and file does not exist."
                )
                # Create an empty DataFrame with expected columns
                expected_cols = [
                    "Hash",
                    "Kind",
                    "Sub_Kind",
                    "Order",
                    "Target_Field",
                    "Source_Field",
                    "Transformation1",
                    "Transformation2",
                    "Transformation3",
                    "Converter",
                    "Is_New",
                    "Header",
                ]
                df_to_write = pd.DataFrame(columns=expected_cols)

        else:
            step = "CONVERTING TO DATAFRAME"
            # Ensure consistent column order
            df_to_write = pd.DataFrame.from_dict(mappings)
            # Define desired column order - include 'Header' if present
            # Make column order robust to missing columns in the input dict list
            base_cols = [
                "Hash",
                "Kind",
                "Sub_Kind",
                "Order",
                "Target_Field",
                "Source_Field",
                "Transformation1",
                "Transformation2",
                "Transformation3",
                "Converter",
                "Is_New",
            ]
            optional_cols = ["Header"]  # Add other potential optional cols here
            present_cols = list(df_to_write.columns)

            final_col_order = [col for col in base_cols if col in present_cols] + [
                col for col in optional_cols if col in present_cols
            ]

            # Include any other columns that might be present but not explicitly ordered
            other_cols = [col for col in present_cols if col not in final_col_order]
            final_col_order.extend(other_cols)

            df_to_write = df_to_write[final_col_order]

        step = "WRITING TO EXCEL"
        if df_to_write is not None:  # Ensure DataFrame exists before writing
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            df_to_write.to_excel(
                file_path,
                sheet_name="IF_HEADERS",
                index=False,
                freeze_panes=(1, 0),  # Freeze header row
                header=True,
                engine="openpyxl",  # Explicitly specify engine
            )
            print(f"Successfully wrote header mappings to: {file_path}")
            return True
        else:
            # This case should only be hit if mappings was empty and file existed
            return False

    except Exception as E:
        info = debug_info(E)
        raise ValueError(
            f"Failed to write CVM header mappings to {file_path} at step {step}: {E} ({info})"
        )
