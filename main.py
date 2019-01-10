import requests, zipfile, io
import os
from edgar_utils import EdgarDownloader

# Represents a company in the EDGAR database
class Company():
    ARCHIVE_URL = "https://www.sec.gov/Archives/"

    def __init__(self, name, cik):
        self.name = name
        self.cik = cik

    # Returns a list of the URL for this filing type (e.g. 10-K, 8K) in the given year
    def getFilingsURLs(self, filingType, startDate, endDate):

        # Represents all the index files we need to search
        searchIndices = []

        # Calculate the start and end quarter
        start = startDate.split("/")
        end = endDate.split("/")
        sYear = int("20" + start[2])
        eYear = int("20" + start[2])
        sQuarter = (int(start[0]) - 1) // 3 + 1 # Calculate quarter
        eQuarter = (int(start[0]) - 1) // 3 + 1 # Calculate quarter

        # Do-while loop to generate all indices
        while True:
            # Add the current quarter (starting with our start date)
            file = "./index_files/master_index_" + str(sYear) + "_QTR" + str(sQuarter) + ".idx"
            searchIndices.append(file)

            # If I just added the last quarter, end
            if sQuarter != eQuarter or sYear != eYear:
                break

            # Move to the next quarter
            sQuarter = sQuarter + 1
            if sQuarter == 5:
                sYear = sYear + 1
                sQuarter = 1

        # Find the index file that contains to this file in each quarter
        output = []

        for f in searchIndices:
            print("\tsearching " + f)
            file = open(f, 'r')
            try:
                index_file = file.read()
                # Search index file for entry matching this
                for line in index_file.splitlines()[11:]:
                    data = line.split("|")
                    if int(self.cik) == int(data[0]) and (filingType in data[2]):
                        output.append(Company.ARCHIVE_URL + data[4]) # data[4] = txt file
            except UnicodeDecodeError as err:
                print("\t\tUnicodeDecodeError", err)

        return output # returns list of txt file urls corresponding to fyear and filing type

    # Returns the txt content of a filing for this company
    def getFilingsFromURL(self, filingType, startDate, endDate):

        # Get the files for this filingType on this fiscal year
        urls = self.getFilingsURLs(filingType, startDate, endDate)

        # Download all of the files
        txtFiles = []
        for url in urls:
            c = requests.get(url).content.decode("utf-8").splitlines()[9: -1];
            txtFiles.append(self.getHTMLFromText(c))

        return (txtFiles, urls) # returns list of txt files corresponding to fyear and filing type

    # Returns a single string representation of the given array
    def getHTMLFromText(self, text):
        # Remove all lines before <html>
        while "<html>" not in text[0].lower():
            del(text[0])

        # Remove all ending lines after <\html>
        while "</html>" not in text[len(text) - 1].lower():
            del(text[len(text) - 1])

        # Check if an html file
        if "html" in text[0].lower():
            print("HTML FOUND")
        else:
            print("HTML NOT FOUND")

        # Now we have html content, trim down to content between first "1a" and
        # first "1b"
        itemA_Count = 0
        for i in range(len(text)):
            if "1A" in text[i]:
                itemA_Count = itemA_Count + 1
            else:
                del(text[i])
            if itemA_Count == 1:
                break
            while "1b" not in text[len(text) - 1].lower() and "item" not in text[len(text) - 1].lower():
                if "1b" in text[len(text) - 1].lower() and "item" not in text[len(text) - 1].lower():
                    continue
                else:
                    del(text[len(text) - 1])

        # Return a single string (joined by a single space)
        return " ".join(x.strip() for x in text)
