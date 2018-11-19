from edgar_utils import EdgarLookup
from company import Company
import csv

if __name__ == "__main__":
    #e = EdgarLookup()
    """with open('funda.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count != 0:
                # Get company
                gvkey = row[0]
                fyear = row[1]
                datadate = row[2]
                LatestPossibleFilingDate = row[3]
                cik = row[4]
                conm = row[5]

                print("Considering " + row[5] + " on " + row[2])
                c = Company(row[5], row[4])
                c.getFilingsUrl(filingType="10-K", date=row[2], fyear=row[1])

            line_count += 1
    """
    c = Company("ALPHARMA -CL A", "0000730469")
    x = c.getFilingsUrl(filingType="10-K")
    print(x)

    # GV Key, FYear, Data Date, CIK, Company Name