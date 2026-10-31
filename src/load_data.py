"""Load the NHTSA recalls flat file (FLAT_RCL_POST_2010.txt)."""
import csv
from pathlib import Path

import pandas as pd

# Field names in order, from docs/RCL.txt (fields 1-29)
COLUMNS = [
    "RECORD_ID", "CAMPNO", "MAKETXT", "MODELTXT", "YEARTXT", "MFGCAMPNO",
    "COMPNAME", "MFGNAME", "BGMAN", "ENDMAN", "RCLTYPECD", "POTAFF",
    "ODATE", "INFLUENCED_BY", "MFGTXT", "RCDATE", "DATEA", "RPNO", "FMVSS",
    "DESC_DEFECT", "CONEQUENCE_DEFECT", "CORRECTIVE_ACTION", "NOTES",
    "RCL_CMPT_ID", "MFR_COMP_NAME", "MFR_COMP_DESC", "MFR_COMP_PTNO",
    "DO_NOT_DRIVE", "PARK_OUTSIDE",
]

# Project root = one level above src/
RAW_FILE = Path(__file__).resolve().parents[1] / "data" / "raw" / "FLAT_RCL_POST_2010.txt"


def load_recalls(path=RAW_FILE):
    """Read the tab-delimited flat file with every column as text."""
    return pd.read_csv(
        path,
        sep="\t",
        header=None,
        names=COLUMNS,
        dtype=str,
        encoding="latin-1",
        quoting=csv.QUOTE_NONE,
        on_bad_lines="warn",
    )