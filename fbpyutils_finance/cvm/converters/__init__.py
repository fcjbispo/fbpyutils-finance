'''
    Converters for the CVM data.
'''
import pandas as pd
from datetime import datetime

def is_nan_or_empty(x):
  return not x or pd.isna(x) or len(str(x)) == 0

def as_boolean(x):
  if is_nan_or_empty(x):
    return False
  else:
    return str(x).upper() in ('S','Y','1')

def as_date(x):
  if is_nan_or_empty(x):
    return None
  else:
    return datetime.strptime(x, '%Y-%m-%d').date()

def as_float(x):
  if is_nan_or_empty(x):
    return None
  else:
    try:
      return float(str(x))
    except ValueError:
      return None

def as_integer(x):
  if is_nan_or_empty(x):
    return 0
  else:
    try:
      return int(float(x))
    except ValueError:
      return None

def as_string(x):
  if is_nan_or_empty(x):
    return None
  else:
    return str(x)

def as_string_id(x):
    if is_nan_or_empty(x):
      return None
    else:
      return str(x).replace('/','').replace('-','').replace('.','')