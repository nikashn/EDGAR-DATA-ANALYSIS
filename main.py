from edgar_utils import EdgarLookup
from company import Company
from bs4 import BeautifulSoup
import csv

def funda_test():
    with open('funda_20181025_updated.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        '''
        0 = gvkey,
        1 = fyear,
        2 = datadate,
        3 = LatestPosible,
        4 = CIK,
        5 = Name
        '''
        next(csv_reader, None)
        #count = 0
        for row in csv_reader:
        #    if count > 20:
        #        return
        #    else:
        #        count += 1
            # Print header
            print(row[5] + " " + row[2] + " to " + row[3] + ":")

            # Get all the files for this company
            c = Company(row[5], row[4])
            files, urls = c.getFilingsFromURL("10-K", row[2], row[3])

            # Process each file
            print("\t[found " + str(len(files)) + " files]")
            num_zeroes = 0
            for i in range(len(files)):
                print("\t[" + urls[i] + ":", end='\t')
                soup = BeautifulSoup(files[i], "html.parser")
                the_risk_factors = soup.select('p b i font')
                if len(the_risk_factors) == 0:
                    num_zeroes += 1
                print(str(len(the_risk_factors)) + "]")
            print()

        percent_zeroes = num_zeroes/len(files) * 100
        print(percent_zeroes, '%') 


if __name__ == "__main__":
    funda_test()
