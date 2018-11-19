import requests


# Represents a company in the EDGAR database
class Company():

    def __init__(self, name, cik):
        self.name = name
        self.cik = cik

    # Returns the URL for this filing
    def getFilingsUrl(self, filingType="10-K", date=""):
        return ""

    # Returns the HTML content of a filing for this company
    def getFilings(self, filingType="10-K", date=""):
        return 0
