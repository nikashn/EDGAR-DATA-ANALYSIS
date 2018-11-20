import requests
import urllib

# Represents an accessor to the EDGAR database
class EdgarLookup():

    def __init__(self):
        # Download the Lookup Database and store it locally
        lookup_data = requests.get("https://www.sec.gov/Archives/edgar/cik-lookup-data.txt")
        lookup_arr = lookup_data.content.decode("latin1").split("\n")
        del lookup_arr[-1] # Delete last element

        # Store a two-way lookup for the
        rev_lookup = []
        for i, item in enumerate(lookup_arr):
            if item != "":
                item_arr = item.split(":")

                # Store both of the lookups
                lookup_arr[i] = (item_arr[0], item_arr[1])
                rev_lookup.append((item_arr[1], item_arr[0]))

        # Store as fields
        self.lookup = dict(lookup_arr)
        self.rev_lookup = dict(rev_lookup)

    #  Get the CIK given Company Name
    def getCIK(self, name):
        return self.lookup[name]

    # Get the Company Name given the CIK
    def getCompanyName(self, cik):
        return self.rev_lookup[cik]


class EdgarDownloader:

    # Downloads all index files to the given folder Path
    def downloadIndexFiles(self, folderPath="./index_files/", fromYear=2005, toYear=2017)
        base_link = "https://www.sec.gov/Archives/edgar/full-index"
        while (fromYear <= toYear):
            qtrCount = 1
            while (qtrCount <= 4)
                web_link = base_link + "/fromYear" + "/QTR" + qtrCount + "/master.idx"
                urllib.urlretrieve(web_link, folderPath)
                qtrCount = qtrCount + 1
            fromYear = fromYear + 1
