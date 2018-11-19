from edgar_utils import EdgarLookup
from company import Company
import sys

if __name__ == "__main__":
    e = EdgarLookup()
    c = Company("ORACLE CORP", e.lookup["ORACLE CORP"])


    # GV Key, FYear, Data Date, CIK, Company Name
