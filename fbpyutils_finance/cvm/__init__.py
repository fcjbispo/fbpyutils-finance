'''
InfoBR Data Providers: CVM Update Package
Provides updating data modules, functions and classes for CVM (Comissão de Valores Imobiliários) provider.
'''

import os, io
import pandas as pd
import re, requests, bs4

import infobr_core as core
import infobr_data as data

from zipfile import ZipFile
from datetime import datetime
from time import sleep
from urllib import request
from fbpyutils import string as sutl, file as futl
from infobr_data.cvm.converters import *

from bs4 import BeautifulSoup

import csv

from multiprocessing import Pool

import sqlite3

from typing import Union, Dict, Optional


HEADERS_FILE = os.path.sep.join([data.APP_DATA_FOLDER, 'cvm', 'data', 'if_headers_v3.xlsx'])

if not os.path.exists(HEADERS_FILE):
    raise FileNotFoundError('CVM Headers File not found.')

HEADERS = pd.read_excel(HEADERS_FILE, sheet_name='IF_HEADERS')

HEADER_MAPPINGS_FILE = os.path.sep.join([data.APP_DATA_FOLDER, 'cvm', 'data', 'if_header_mappings.xlsx'])

if not os.path.exists(HEADER_MAPPINGS_FILE):
    raise FileNotFoundError('CVM Headers Mappings File not found.')

HEADER_MAPPINGS = pd.read_excel(HEADER_MAPPINGS_FILE, sheet_name='IF_HEADERS')

STORAGE_PATH = 'data/cvm'

CATALOG_JOURNAL = 'cvm_if_catalog_journal'

HISTORY_FOLDER = os.path.sep.join([core.SETTINGS['history_folder'], 'cvm'])

DATA_FOLDER = os.path.sep.join([core.SETTINGS['data_folder'], 'cvm'])

URL_IF_REGISTER = "http://dados.cvm.gov.br/dados/FI/CAD/DADOS"
URL_IF_REGISTER_HIST = "http://dados.cvm.gov.br/dados/FI/CAD/DADOS/HIST"
URL_IF_DAILY = "http://dados.cvm.gov.br/dados/FI/DOC/INF_DIARIO/DADOS"
URL_IF_DAILY_HIST = "http://dados.cvm.gov.br/dados/FI/DOC/INF_DIARIO/DADOS/HIST"

SOURCE_ENCODING, TARGET_ENCODING = 'iso-8859-1', 'utf-8'

_get_value_by_index_if_exists = lambda x, y, z=None: x[y] if len(x) > y else z or None

_make_number_type = lambda x, y=int: None if x is None or x == '-' else int(re.sub(r'[a-zA-Z]', '', x))

_timelapse = lambda x: round((datetime.now() - x).seconds / 60, 4)


def _resolve_storage_path(root_path: str, kind: str, sub_kind: str, sep: str = os.path.sep) -> str:
    """
    Resolve the storage path for a given root path, kind, and sub-kind.

    Parameters:
    - root_path (str): The root path to the storage location.
    - kind (str): The kind of data to be stored.
    - sub_kind (str): The sub-kind of data to be stored.
    - sep (str, optional): The separator to use in the path. Defaults to os.path.sep.

    Returns:
    - str: The resolved storage path.

    Example:
    ```
    root_path = '/data'
    kind = 'images'
    sub_kind = 'JPEG'
    sep = '/'
    print(_resolve_storage_path(root_path, kind, sub_kind, sep))
    # Output: '/data/images/JPEG'
    ```
    """
    return sep.join(
        [root_path, kind.lower()] + next(
            (m[2] for m in STORAGE_MAPPINGS if (m[0], m[1]) == (kind, sub_kind)), []
        )
    )


def _replace_all(x: str, old: str, new: str) -> str:
    """
    Replace all occurrences of `old` with `new` in `x`.

    Parameters:
    - x (str): The input string.
    - old (str): The string to be replaced.
    - new (str): The replacement string.

    Returns:
    - str: The input string with all occurrences of `old` replaced by `new`.

    Example:
    ```
    x = 'hello, world'
    old = 'o'
    new = '0'
    print(_replace_all(x, old, new))
    # Output: 'hell0, w0rld'
    ```
    """
    while old in x:
        x = x.replace(old, new)
    return x


def _make_datetime(x: str, y: str) -> Union[datetime, None]:
    """
    Convert a string representation of a date and time into a datetime object.

    Parameters:
    - x (str): The string representation of the date.
    - y (str): The string representation of the time.

    Returns:
    - datetime: The resulting datetime object, or None if either `x` or `y` are None.

    Example:
    ```
    x = '29-Jan-2023'
    y = '08:30'
    print(_make_datetime(x, y))
    # Output: datetime.datetime(2023, 1, 29, 8, 30)
    ```
    """
    sep = ' '
    if not all([x, y]):
        return None
    else:
        dt = sep.join([x, y])
        return datetime.strptime(dt, "%d-%b-%Y %H:%M")


def _get_url_paths(url: str, params: Optional[Dict] = {}) -> pd.DataFrame:
    """
    Get the URL paths of the given URL with the given parameters.

    Args:
    - url: URL to get the paths from
    - params: query parameters to include in the request, if any (default: {})

    Returns:
    - DataFrame of the extracted URL paths information, with columns:
        - 'sequence': index of the path in the extracted list
        - 'href': the URL of the path
        - 'name': name of the path
        - 'last_modified': last modification date of the path
        - 'size': size of the path in bytes
    
    """
    response = requests.get(url, params=params)
    if response.ok:
        response_text = response.text
    else:
        return response.raise_for_status()
    soup = BeautifulSoup(response_text, 'html.parser')
    pre = soup.find_all('pre')

    pre = pre[0] if len(pre) > 0 else None

    sep = pre.text[3:5]

    hrefs = [a.get('href') for a in [p for p in pre] if type(a) if type(a) == bs4.element.Tag]

    contents = [_replace_all(p, '  ', ' ').split(' ') for p in pre.text.split(sep)]

    directory = set()

    for i, href in enumerate(hrefs):
        directory.add((
            i,
            href,
            _get_value_by_index_if_exists(contents[i], 0),
            _make_datetime(
                _get_value_by_index_if_exists(contents[i], 1), 
                _get_value_by_index_if_exists(contents[i], 2)
            ),
            _make_number_type(_get_value_by_index_if_exists(contents[i], 3))
        ))

    headers = ['sequence', 'href', 'name', 'last_modified', 'size']
    directory = pd.DataFrame(directory, columns=headers).sort_values(by='sequence', ascending=True)

    return directory


def _get_remote_files_list(kind: str, current_url: str, history_url: str) -> pd.DataFrame:
    """
    Get a DataFrame containing information of files in remote locations.

    Args:
    - kind (str): Kind of files to retrieve.
    - current_url (str): URL string of the current location.
    - history_url (str): URL string of the history location.

    Returns:
    - pd.DataFrame: DataFrame containing information of the remote files, including `kind`, `url`, `history` and other information extracted from the URL paths.
    """
    current_dir = _get_url_paths(current_url)
    current_dir['history'] = False
    current_dir['url'] = current_url

    history_dir = _get_url_paths(history_url)
    history_dir['history'] = True
    history_dir['url'] = history_url

    files_dir = pd.concat([
        current_dir[~pd.isnull(current_dir['size'])],
        history_dir[~pd.isnull(history_dir['size'])]
    ]).copy()

    files_dir['kind'] = kind

    return files_dir


def _build_target_file_name(metadata, target_folder, index=None, file=None):
    preffix = metadata['name'].split('.')[0]
    if file:
        index = str(int('0' if index is None else index)).zfill(4)
        target_file_name = '.'.join([preffix, index, file])
    else:
        target_file_name = metadata['name']
    target_file_name = '.'.join([metadata['kind'].lower(), target_file_name])

    return os.path.sep.join([target_folder, target_file_name])


def _write_target_file(data, metadata, target_folder, index=None, file=None, encoding=TARGET_ENCODING):

    target_file = _build_target_file_name(metadata, target_folder, index, file)

    with open(target_file, 'wb') as f:
        f.write(data.encode(encoding))
        f.close()

    return target_file

def _get_expression_and_converters(mappings):
    expressions, converters = [], {}
    for m in mappings:
        expression = 'NULL'
        if not is_nan_or_empty(m['Source_Field']):
            
            expression = m['Source_Field']

            if not is_nan_or_empty(m['Transformation1']):
                expression = m['Transformation1'].replace('$X', expression)

                if not is_nan_or_empty(m['Transformation2']):
                    expression = m['Transformation2'].replace('$X', expression)

                    if not is_nan_or_empty(m['Transformation3']):
                        expression = m['Transformation3'].replace('$X', expression)

        if not is_nan_or_empty(m['Converter']):
            converters[m['Target_Field']] = eval(m['Converter'].replace('_as_', 'as_'))
        else:
            converters[m['Target_Field']] = lambda x: None
        expressions.append(f"{expression.lower()} AS {m['Target_Field'].lower()}")
    return expressions, converters


def _apply_converters(data, converters):
    try:
        for k, v in converters.items():
            if k in data.columns:
                data[k] = data[k].apply(v)
        return data.where(pd.notnull(data), None)
    except Exception as E:
        raise ValueError(f"Conversion error: {E} on {k}:{v}")
        
        
def _apply_expressions(data, expressions, in_memory=True):
    try:
        db = sqlite3.connect(':memory:') if in_memory else core.STAGE
        data.to_sql('if_data', con=db, if_exists='replace')

        return pd.read_sql(f'SELECT {", ".join(expressions)} FROM if_data', con=db)
    finally:
        db.close()


def _update_cvm_history_file(if_metadata):
    result = []
    if is_nan_or_empty(if_metadata['last_download']) \
        or (if_metadata['last_modified'] > if_metadata['last_download']):

        response = request.urlopen(if_metadata['url'])

        data = response.read()

        mime_type = futl.magic.from_buffer(data)
        mime_type = mime_type.split(';')[0]

        text_mime_types = ('Non-ISO extended-ASCII text', 'ISO-8859 text', )
        zip_mime_types = ('Zip archive data, at least v2.0 to extract', )

        if any([a for a in zip_mime_types if a in mime_type]):
            zip_file = ZipFile(io.BytesIO(data))
            for k, v in enumerate(zip_file.namelist()):
                response_data = zip_file.open(v).read().decode(SOURCE_ENCODING)
                r = _write_target_file(response_data, if_metadata, HISTORY_FOLDER, index=k, file=v, encoding=TARGET_ENCODING)
                
                result.append(['SUCCESS',if_metadata,f'{r} written from {if_metadata["url"]}'])
        elif any([a for a in text_mime_types if a in mime_type]):
            response_data = data.decode(SOURCE_ENCODING)

            r = _write_target_file(response_data, if_metadata, HISTORY_FOLDER, encoding=TARGET_ENCODING)

            result.append(['SUCCESS',if_metadata, f'{r} written from {if_metadata["url"]}'])
        else:
            result.append(['ERROR',if_metadata,'Unknown mime type:{} for url:{}'.format(mime_type, if_metadata['url'])])
    else:
        result.append(['SKIP','Already updated data for url:{}'.format(if_metadata['url'])])
    
    return result


def _process_cvm_history_file(cvm_file_info):
    result = []
    start_time = datetime.now()
    try:
        step = 'INITIALIZING PARAMETERS'
        name, cvm_file, update_time = cvm_file_info

        step = 'READING CVM FILE METADATA'
        kind, sub_kind, cvm_if_data, partition_cols = read_cvm_history_file(
            source_file=cvm_file, 
            apply_converters=True,
            check_header=False
        )
        try:
            target_table = f'cvm_{kind}_{sub_kind}_history_stg'.lower()

            cvm_if_data['source'] = '.'.join(cvm_file.split(os.path.sep)[-1].split('.')[0:-1])
            cvm_if_data['timestamp'] = update_time.isoformat()

            step = 'WRITING CVM DATA STAGE'
            core.to_table(cvm_if_data, target_table, index=False, if_exists='append', con=core.STAGE)

            result.append([
                name, kind, sub_kind, cvm_file, update_time, len(cvm_if_data), partition_cols, 
                _timelapse(start_time), step, 'SUCCESS', None
            ])
        except Exception as E:
            result.append([
                name, kind, sub_kind, cvm_file, update_time, len(cvm_if_data), partition_cols, 
                _timelapse(start_time), step, 'ERROR', f'ERROR: {E}'
            ])
    except Exception as E:
        if len(cvm_file_info) == 3:
            name, cvm_file, update_time = cvm_file_info
        else:
            name, cvm_file, update_time = None, None, None
        result.append([
            name, None, None, cvm_file, update_time, None, None, 
            _timelapse(start_time), step, 'ERROR', f'ERROR {E}: WITH info={cvm_file_info}'
        ])

    return result


def update_cvm_history_files(parallelize=True):
    PARALLELIZE = parallelize and os.cpu_count()>1
    step = None
    
    try:
        step = 'SETTING UP COMPONENTS'

        step = "SETTING UP CATALOG JOURNAL"

        if_register_files = _get_remote_files_list(
            'IF_REGISTER', URL_IF_REGISTER, URL_IF_REGISTER_HIST
        )

        if_position_files = _get_remote_files_list(
            'IF_POSITION', URL_IF_DAILY, URL_IF_DAILY_HIST
        )

        if_remote_files = pd.concat([
            if_register_files,
            if_position_files
        ]).copy()

        catalog_journal = pd.read_sql(
            f'select * from {CATALOG_JOURNAL}', con=core.DB
        ).to_dict('records')

        for if_metadata in [f for f in if_remote_files.to_dict('records')]:
            if_metadata['url'] = '/'.join([if_metadata['url'], if_metadata['name']])

            catalog_metadata = next((m for m in catalog_journal if m['url'] == if_metadata['url']), None)
            
            if catalog_metadata is None:
                catalog_metadata = if_metadata
                catalog_metadata['history'] = (if_metadata['name'] != 'cad_fi.csv')
                catalog_metadata['last_download'] = None
                catalog_metadata['last_updated'] = None
                catalog_metadata['process'] = True
                catalog_metadata['active'] = True
                catalog_journal.append(catalog_metadata)
            else:
                catalog_metadata['process'] = False
                catalog_metadata['history'] = (catalog_metadata['history'] == True or if_metadata['name'] != 'cad_fi.csv')
                if is_nan_or_empty(catalog_metadata['last_modified']) \
                    or if_metadata['last_modified'] > catalog_metadata['last_modified']:
                    catalog_metadata['last_modified'] = if_metadata['last_modified']
                    catalog_metadata['process'] = True
                elif is_nan_or_empty(catalog_metadata['last_updated']) \
                    or if_metadata['last_modified'] > catalog_metadata['last_updated']:
                    catalog_metadata['process'] = True

        catalog_journal_df = pd.DataFrame.from_dict(catalog_journal, orient='columns')

        for c in ['last_modified', 'last_download', 'last_updated']:
            catalog_journal_df[c] = pd.to_datetime(c, errors='coerce')

        catalog_journal_df.to_sql(CATALOG_JOURNAL, con=core.DB, if_exists='replace', index=False)

        results = []
        metadata_to_process = [m for m in catalog_journal if m['process']]

        if PARALLELIZE:
            with Pool(os.cpu_count()) as p:
                results = p.map(_update_cvm_history_file, metadata_to_process)
        else:
            for if_metadata in metadata_to_process:
                result = _update_cvm_history_file(if_metadata)
                results.append(result)

        step = 'UPDATE CVM CATALOG JOURNAL: CONSOLIDATING INFO'
        result_cols = [
            'name', 'kind', 'status', 'message'
        ]
        result_data = pd.DataFrame(
            [(r[0][1]['name'], r[0][1]['kind'], r[0][0], r[0][-1]) for r in results if r[0][0] != 'SKIP'], columns=result_cols
        )
        result_table = 'cvm_update_history_file_results_stg'
        core.to_table(result_data, result_table, con=core.STAGE, index=False, if_exists='replace')

        download_time = datetime.now().isoformat()

        step = 'UPDATE CVM CATALOG JOURNAL: UPDATING DATA'
        for name, kind in pd.read_sql(f'''
            with t as (
                select name, kind,
                        sum(case when status='ERROR' then 1 else 0 end) errors, 
                        sum(case when status='SUCCESS' then 1 else 0 end) successes, 
                        sum(case when status='SKIP' then 1 else 0 end) skips
                    from {result_table}
                    group by name, kind
            )
            select name, kind
                from t
                where errors = 0
                and (successes > 0 or skips > 0)
        ''', con=core.STAGE).to_records(index=False):
            _ = core.DB.execute(f'''
                update {CATALOG_JOURNAL}
                    set last_download = '{download_time}'::timestamp,
                        process = TRUE
                    where name = '{name}'
                    and kind = '{kind}';
            ''')
            sleep(0.3)

        return results
    except Exception as E:
        raise ValueError('Fail to UPDATE history files on step {}: {}'.format(step, E))


def get_cvm_file_metadata(cvm_file):
    with open(cvm_file, 'r') as f:
        line = f.readline()
        f.close()
    file_name_parts = cvm_file.split(os.path.sep)[-1].split('.')
    kind = file_name_parts[0].upper()
    metadata_file = file_name_parts[-2]
    sub_kind = 'CAD_FI' if 'cad_fi' == metadata_file.lower() or metadata_file.lower().startswith('inf_cadastral_fi') \
        else 'DIARIO_FI' if metadata_file.lower().startswith('inf_diario_fi') else metadata_file.upper()
    line = line.split('\n')[0]
    return kind, sub_kind, line, sutl.hash_string(';'.join([kind, sub_kind, line]))


def check_cvm_headers_changed(cvm_files=None) -> bool:
    step = None

    try:
        step = 'SETTING UP COMPONENTS'

        step = 'READING HEADERS MAPPINGS INFO'
        if not os.path.exists(HEADER_MAPPINGS_FILE):
            raise FileNotFoundError(f"Header Mappings not found.")

        _ = pd.read_excel(
            HEADER_MAPPINGS_FILE, sheet_name='IF_HEADERS'
        ).to_sql('cvm_if_headers_stg', core.STAGE, index=False, if_exists='replace')

        header_mappings = {}

        for header in pd.read_sql("""
            select distinct "Header"
            from cvm_if_headers_stg
        """, con=core.STAGE).to_dict('records'):
            mappings = pd.read_sql("""
            select "Order", "Target_Field", "Source_Field", "Transformation1", "Transformation2", "Transformation3", "Converter"
                from cvm_if_headers_stg 
                where "Header" = %(header)s
                order by "Order"
            """, con=core.STAGE, params={'header': header['Header']}).to_dict('records')
            header_mappings[header['Header']] = mappings

        step = 'READING IF HISTORY FILES'
        if cvm_files is not None and type(cvm_files) == list:
            if_source_files = cvm_files
        else:
            file_mask = 'if_*.csv'
            if_source_files = futl.find(HISTORY_FOLDER, mask=file_mask)

        if_source_headers = set()

        for if_register_file in if_source_files:
            try:
                kind, sub_kind, header, header_hash = get_cvm_file_metadata(if_register_file)
            except Exception as e:
                print(f'Ouch! {e} on {if_register_file}')
                raise e
            if_source_headers.add((kind, sub_kind, header, header_hash))

        _ = pd.DataFrame(
            if_source_headers, columns=['Kind', 'Sub_Kind', 'Header', 'Hash']
        ).to_sql('cvm_if_source_headers_stg', core.STAGE, index=False, if_exists='replace')


        step = 'READING CURRENT HEADERS INFO'
        if os.path.exists(HEADERS_FILE):
            mappings = pd.read_excel(HEADERS_FILE, sheet_name='IF_HEADERS').to_dict('records')
        else:
            mappings = []

        existing_mappings = set([m.get('Hash') for m in mappings])

        if len(if_source_files) == 0 and len(existing_mappings) == 0:
            raise ValueError("Mappend Headers and/or History Files Not Found.")

        step = 'COMPUTING NEW HEADERS INFO'
        for header_group in pd.read_sql("""
            select distinct "Kind", "Sub_Kind"
            from cvm_if_source_headers_stg
        """, con=core.STAGE).to_dict('records'):
            kind, sub_kind = header_group['Kind'], header_group['Sub_Kind']
            header_mapping = header_mappings[kind]

            for source_header in pd.read_sql("""
                select * 
                from cvm_if_source_headers_stg
                where "Kind" = %(kind)s and "Sub_Kind" = %(sub_kind)s
            """, con=core.STAGE, params={'kind': kind, 'sub_kind': sub_kind}).to_dict('records'):
                header = source_header['Header']
                header_hash = source_header['Hash']

                if header_hash not in existing_mappings:
                    fields = header.split(';')
                    for m in header_mapping[:]:
                        found = m['Source_Field'] in fields
                        mappings.append({
                            'Kind': kind,
                            'Sub_Kind': sub_kind,
                            'Header': header,
                            'Hash': header_hash,
                            'Order': int(m['Order']),
                            'Target_Field': m['Target_Field'],
                            'Source_Field': m['Source_Field'] if found else None,
                            'Transformation1': m['Transformation1'] if found else None,
                            'Transformation2': m['Transformation2'] if found else None,
                            'Transformation3': m['Transformation3'] if found else None,
                            'Converter': m['Converter'] if found else None,
                            'Is_New': True
                        })

                        if sub_kind in ['CAD_FI', 'DIARIO_FI']:
                            max_order = max([
                                h['Order'] for h in header_mapping if h['Source_Field'] is not None])
                            source_fields = [
                                h['Source_Field'] for h in header_mapping if h['Source_Field'] is not None]
                            mapped_fields = [
                                m['Source_Field'] for m in mappings if m['Target_Field'] is not None] + [
                                    m['Source_Field'] for m in mappings if m['Transformation1'] is not None] + [
                                        m['Source_Field'] for m in mappings if m['Transformation2'] is not None] + [
                                            m['Source_Field'] for m in mappings if m['Transformation3'] is not None] 
                            for f in fields:
                                if not f in source_fields and not f in mapped_fields:
                                    max_order += 1
                                    mappings.append({
                                        'Kind': kind,
                                        'Sub_Kind': sub_kind,
                                        'Header': header,
                                        'Hash': header_hash,
                                        'Order': max_order,
                                        'Target_Field': None,
                                        'Source_Field': f,
                                        'Transformation1': None,
                                        'Transformation2': None,
                                        'Transformation3': None,
                                        'Converter': None,
                                        'Is_New': True
                                    })

        step = 'WRITING NEW HEADERS MAPPINGS INFO'
        new_mappings = set(m['Hash'] for m in mappings) - existing_mappings
        if new_mappings:
            _ = pd.DataFrame.from_dict(mappings).to_sql('cvm_if_headers_final_stg', core.STAGE, index=False, if_exists='replace')

            if_headers_final = pd.read_sql("""
                select distinct 
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
                    "Is_New"
                from cvm_if_headers_final_stg
                order by "Hash",
                        "Order"
            """, con=core.STAGE)
         
            if_headers_final.to_excel(
                HEADERS_FILE, sheet_name='IF_HEADERS', index=False,  encoding=TARGET_ENCODING, freeze_panes=(1, 0), header=True)

            step = 'REMOVING STAGE TABLES'
            for t in ['cvm_if_headers_stg', 'cvm_if_source_headers_stg', 'cvm_if_headers_final_stg']:
                _ = core.STAGE.execute(f'drop table if exists {t}')

            return True
        else:
            return False
    except Exception as E:
        raise ValueError('Fail to UPDATE HEADERS CHANGE CHECK on step {}: {}'.format(step, E))


def read_cvm_history_file(
    source_file, apply_converters=True, check_header=False
):
    try:
        step = 'CHECK FILE HEADER'
        if check_header:
            if check_cvm_headers_changed([source_file]):
                raise ValueError('Header changed!!')

        step = 'DATA INFO FROM SOURCE FILE'
        kind, sub_kind, _, header_hash = get_cvm_file_metadata(source_file)

        if not header_hash:
            raise ValueError("Header hash not found!")

        step = 'READING CURRENT HEADERS INFO'
        if not os.path.exists(HEADERS_FILE):
            raise Exception('Headers Mappings file not found!')
        
        header_mappings = pd.read_excel(HEADERS_FILE, sheet_name='IF_HEADERS')

        mappings = header_mappings[header_mappings.Hash == header_hash].to_dict('records')

        expressions, data_converters = _get_expression_and_converters(mappings)

        step = 'READING DATA FROM SOURCE FILE'
        if_data = pd.read_csv(source_file, sep=';', encoding=TARGET_ENCODING, dtype=str, quoting=csv.QUOTE_NONE)
        if_data.columns = [c.lower() for c in if_data.columns]

        step = 'APPLYING DATA EXPRESSIONS'
        cvm_if_data = _apply_expressions(if_data, expressions=expressions, in_memory=True)

        if apply_converters:
            step = 'APPLYING DATA TYPES CONVERSIONS'
            cvm_if_data = _apply_converters(cvm_if_data.copy(), data_converters)

        cvm_if_data_cols = list(cvm_if_data.columns)
        cvm_if_data['kind'] = kind
        cvm_if_data['sub_kind'] = sub_kind

        step = 'COMPUTING PERIOD INFO'
        if kind == 'IF_POSITION':
            cvm_if_data['year'] = cvm_if_data['position_date'].apply(lambda x: datetime.fromisoformat(str(x)).strftime('%Y'))
            cvm_if_data['period'] = cvm_if_data['position_date'].apply(lambda x: datetime.fromisoformat(str(x)).strftime('%Y-%m'))
        elif kind == 'IF_REGISTER':
            if sub_kind == 'CAD_FI':
                file_name = source_file.split(os.path.sep)[-1]
                date_part = file_name.split('.')[-2].split('_')[-1]

                if date_part == 'fi':
                    date_part = datetime.now().strftime("%Y-%m-%d")

                cvm_if_data['year'] = pd.to_datetime(date_part, format='%Y-%m-%d').strftime("%Y")
                cvm_if_data['period'] = pd.to_datetime(date_part, format='%Y-%m-%d').strftime("%Y-%m")
                cvm_if_data['period_date'] = pd.to_datetime(date_part, format='%Y-%m-%d').strftime('%Y-%m-%d')
            elif sub_kind.startswith('CAD_FI_HIST'):
                cvm_if_data['year'] = cvm_if_data['start_date'].apply(lambda x: datetime.fromisoformat(str(x)).strftime('%Y'))
                cvm_if_data['period'] = cvm_if_data['start_date'].apply(lambda x: datetime.fromisoformat(str(x)).strftime('%Y-%m'))
            else:
                raise ValueError(f'Invalid Sub Kind: {sub_kind} on {source_file}')
        else:
            raise ValueError(f'Invalid Kind: {kind} on {source_file}')

        step = 'SELECT DATA TO RETURN'
        partition_cols = ['kind', 'sub_kind']
        for c in ['year', 'period', 'period_date']:
            if c in cvm_if_data.columns:
                partition_cols += [c]

        return kind, sub_kind, cvm_if_data[partition_cols + cvm_if_data_cols], partition_cols
    except Exception as E:
        raise ValueError('Fail to get CVM IF HISTORY Data on step {}: {}'.format(step, E))


def update_cvm_history_data(parallelize=True):
    PARALLELIZE = parallelize and os.cpu_count()>1
    try:
        step = 'LOAD CATALOG UPDATES'
        catalog_updates = pd.read_sql(f'''
            select * 
              from {CATALOG_JOURNAL} 
             where active 
               and last_updated is null 
                or last_download::timestamp > last_updated::timestamp
             order by kind, name
        ''', con=core.DB).to_dict(orient='records')

        results = []
        if len(catalog_updates) > 0:
            step = 'SELECTING FILES TO UPDATE'
            cvm_files = []
            for name, mask in [
                (u['name'], f"{u['kind'].lower()}.{u['name'].split('.')[0]}.*") for u in catalog_updates
            ]:
                for cvm_file in futl.find(HISTORY_FOLDER, mask):
                    cvm_files += [[name, cvm_file]]

            if len(cvm_files) == 0:
                return []

            step = 'CHECKING HEADERS'
            if check_cvm_headers_changed(cvm_files=[f[1] for f in cvm_files]):
                raise ValueError('Headers Changed! Update not possible.')

            step = 'UPDATE CVM HISTORY DATA'
            update_time = datetime.now()

            cvm_files = [[f[0], f[1], update_time] for f in cvm_files]

            if PARALLELIZE:
                with Pool(os.cpu_count()) as p:
                    results = p.map(_process_cvm_history_file, cvm_files)
            else:
                for cvm_file in cvm_files:
                    result = _process_cvm_history_file(cvm_file)
                    results.append(result)

            step = 'UPDATE CVM CATALOG JOURNAL: CONSOLIDATING INFO'
            result_cols = [
                'name', 'kind', 'sub_kind', 'cvm_file', 'update_time', 'records', 
                'partition_cols', 'timelapse', 'last_step', 'status', 'message'
            ]
            result_data = pd.DataFrame(
                [r for r in [r[0] for r in results]], columns=result_cols
            )
            result_table = 'cvm_update_history_results_stg'
            core.to_table(result_data, result_table, con=core.STAGE, index=False, if_exists='replace')

            step = 'UPDATE CVM CATALOG JOURNAL: UPDATING DATA'
            for name, kind, update_time in pd.read_sql(f'''
                with t as (
                    select name, kind,
                           sum(case when status='ERROR' then 1 else 0 end) errors, 
                           sum(case when status='SUCCESS' then 1 else 0 end) successes,
                           max(update_time) update_time
                      from {result_table}
                     group by name, kind
                )
                select name, kind, update_time
                  from t
                 where errors = 0
                   and successes > 0
            ''', con=core.STAGE).to_records(index=False):
                _ = core.DB.execute(f'''
                    update {CATALOG_JOURNAL}
                       set last_updated = '{update_time}'::timestamp,
                           process = FALSE
                     where name = '{name}'
                       and kind = '{kind}';
                ''')
                sleep(0.5)

        return results
    except Exception as E:
        raise ValueError('Fail to get CVM UPDATE HISTORY DATA Data on step {}: {} (name={}, file={})'.format(step, E, name, cvm_file))


STORAGE_MAPPINGS = (
    ('IF_POSITION', 'DIARIO_FI', [], []),
    ('IF_REGISTER', 'CAD_FI', ['all'], []),
    ('IF_REGISTER', 'CAD_FI_HIST_ADMIN', ['segmented', 'admin'], []),
    ('IF_REGISTER', 'CAD_FI_HIST_AUDITOR', ['segmented', 'controller'], []),
    ('IF_REGISTER', 'CAD_FI_HIST_CLASSE', ['segmented', 'class'], []),
    ('IF_REGISTER', 'CAD_FI_HIST_CONDOM', ['segmented', 'tenancy'], []),
    ('IF_REGISTER', 'CAD_FI_HIST_CONTROLADOR', ['segmented', 'supervisor'], []),
    ('IF_REGISTER', 'CAD_FI_HIST_CUSTODIANTE', ['segmented', 'custodian'], []),
    ('IF_REGISTER', 'CAD_FI_HIST_DENOM_COMERC', ['segmented', 'commercial_name'], []),
    ('IF_REGISTER', 'CAD_FI_HIST_DENOM_SOCIAL', ['segmented', 'business_name'], []),
    ('IF_REGISTER', 'CAD_FI_HIST_DIRETOR_RESP', ['segmented', 'director'], []),
    ('IF_REGISTER', 'CAD_FI_HIST_EXCLUSIVO', ['segmented', 'exclusiveness'], []),
    ('IF_REGISTER', 'CAD_FI_HIST_EXERC_SOCIAL', ['segmented', 'excercises'], []),
    ('IF_REGISTER', 'CAD_FI_HIST_FIC', ['segmented', 'quotas'], []),
    ('IF_REGISTER', 'CAD_FI_HIST_GESTOR', ['segmented', 'manager'], []),
    ('IF_REGISTER', 'CAD_FI_HIST_PUBLICO_ALVO', ['segmented', 'audience'], []),
    ('IF_REGISTER', 'CAD_FI_HIST_RENTAB', ['segmented', 'profitability'], []),
    ('IF_REGISTER', 'CAD_FI_HIST_SIT', ['segmented', 'situation'], []),
    ('IF_REGISTER', 'CAD_FI_HIST_TAXA_ADM', ['segmented', 'admin_rate'], []),
    ('IF_REGISTER', 'CAD_FI_HIST_TAXA_PERFM', ['segmented', 'performance_rate'], []),
    ('IF_REGISTER', 'CAD_FI_HIST_TRIB_LPRAZO', ['segmented', 'long_term_taxes'], []),
)

STORAGE_TABLESET = [
    (
        m[0], 
        m[1],
        'cvm', 
        f"{m[0].lower()}{'' if len(m[2]) == 0 else '_'+m[2][-1]}",
        _resolve_storage_path(
            STORAGE_PATH, m[0], m[1], '/'
        ),
        m[3]
        
    ) 
    for m in STORAGE_MAPPINGS
]


if not os.path.exists(HISTORY_FOLDER):
    os.makedirs(HISTORY_FOLDER)