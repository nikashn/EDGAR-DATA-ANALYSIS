import requests, zipfile, io
from math import ceil


# Represents a company in the EDGAR database
class Company():
    ARCHIVE_URL = "https://www.sec.gov/Archives/"

    def __init__(self, name, cik):
        self.name = name
        self.cik = cik

    # Returns a list of the URL for this filing type (e.g. 10-K, 8) in the given year
    def getFilingsURLs(self, filingType, fyear):

        # Find the index file that contains to this file in each quarter
        output = []
        for q in range(1, 5):
            fquarter = "QTR" + str(q)
            index_url = Company.ARCHIVE_URL + "edgar/full-index/" + fyear + "/" + fquarter + "/master.zip"

            # Download and extract the zip file
            index_zip = requests.get(index_url)
            tmp = zipfile.ZipFile(io.BytesIO(index_zip.content))
            index_file = tmp.read('master.idx').decode("utf-8")

            # Search index file for entry matching this
            for line in index_file.splitlines()[11:]:
                data = line.split("|")
                if int(self.cik) == int(data[0]) and (filingType in data[2]):
                    output.append(Company.ARCHIVE_URL + data[4])

        return output

    # Returns the HTML content of a filing for this company
    def getFilingsFromURL(self, filingType, fyear):
        # Get the files for this filingType on this fiscal year
        urls = self.getFilingsURLs(filingType, fyear)

        # Download all of the files
        files = []
        for url in urls:
            c = requests.get(url).content
            files.append(c)

        return files
