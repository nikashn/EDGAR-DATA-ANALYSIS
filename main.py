from edgar_utils import EdgarLookup
from company import Company
from bs4 import BeautifulSoup
import csv

if __name__ == "__main__":

    with open('funda.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0

        # 0 = gvkey, 1 = fyear, 2 = datadate, 3 = LatestPosible, 4 = CIK, 5 = Name
        for row in csv_reader:
            if line_count != 0:

                # Print header
                print("Considering " + row[5] + " from " + row[1])

                # Get all the files for this company
                c = Company(row[5], row[4])
                files = c.getFilingsFromFile(filingType="10-K", fyear=row[1])

                # Process each file
                factors = []
                for file in files:
                    soup = BeautifulSoup(file, 'html.parser')
                    print(soup.title)

            line_count += 1

    print("Completed!")