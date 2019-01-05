from edgar_utils import EdgarLookup
from company import Company
from bs4 import BeautifulSoup
import csv
import re

def funda_test():
    with open('funda_20181025_updated_backup.csv', 'r') as csv_file:
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
        #new_rows_list = []

        for row in csv_reader:
            # Print header
            print(row[5] + " " + row[2] + " to " + row[3] + ":")

            # Get all the files for this company
            c = Company(row[5], row[4])
            files, urls = c.getFilingsFromURL("10-K", row[2], row[3])

            '''
            # Update columnDir section to get easy access to file
            if row[8] == 'Dir':
                new_row = [row[8], urls[0]]
                new_rows_list.append(new_row)

            if c.name == 'ADC TELECOMMUNICATIONS INC':
                exit()
            '''

            # Process each file
            print("\t[found " + str(len(files)) + " files]")
            for i in range(len(files)):
                print("\t[" + urls[i] + ":", end='\t')
                #
                soup = BeautifulSoup(files[i], "html.parser")
                the_risk_factors = soup.select('p b i')
                the_risk_factors_tbl = soup.select('td b i')
                print(str(len(the_risk_factors)) + ', ' + str(len(the_risk_factors_tbl)) + "]")
            print()

    '''
    # Write to file
    updated_file = open('funda_20181025_updated_backup.csv', 'w')
    writer = csv.writer(updated_file)
    writer.writerows(new_rows_list)
    updated_file.close()
    '''

if __name__ == "__main__":
    funda_test()
