from edgar_utils import EdgarLookup
from company import Company
import csv

if __name__ == "__main__":

    # e = EdgarLookup()
    with open('funda.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0

        for row in csv_reader:
            if line_count != 0:

                # 0 = gvkey, 1 = fyear, 2 = datadate, 3 = LatestPosible, 4 = CIK, 5 = Name
                print("Considering " + row[5] + " from " + row[1])
                c = Company(row[5], row[4])
                files = c.getFilingsURLs(filingType="10-K", fyear=row[1])
                print("\t" + str(files))

            line_count += 1


    # GV Key, FYear, Data Date, CIK, Company Name