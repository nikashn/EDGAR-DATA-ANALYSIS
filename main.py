from edgar_utils import EdgarLookup
from company import Company
from bs4 import BeautifulSoup
import csv

def funda_test():
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
                    print(soup.find_all("html"))

            line_count += 1

if __name__ == "__main__":

    c = Company("AAR CORP", "0000001750")
    files = c.getFilingsFromURL("10-K", "5/31/06", "9/5/06")

    # Find all the 10-K's in the range
    for file in files:
       c = Company("AAR CORP", "0000001750")
    files = c.getFilingsFromURL("10-K", "5/31/06", "9/5/06")

    # Find all the 10-K's in the range
    for file in files:
        soup = BeautifulSoup(file, "html.parser")
        the_risk_factors = soup.select('p b i font')
        print(len(the_risk_factors))
        #i = 1
        #for risk_factor in the_risk_factors:
        #    print('\n\n' + str(i) + '.\t' + risk_factor.text + '\n\n')
        #    i += 1
