import requests, zipfile, io
import os
from math import ceil
from edgar_utils import EdgarDownloader
from bs4 import BeautifulSoup

# Represents a company in the EDGAR database
class Company():
    ARCHIVE_URL = "https://www.sec.gov/Archives/"

    def __init__(self, name, cik):
        self.name = name
        self.cik = cik

    # Returns a list of the URL for this filing type (e.g. 10-K, 8K) in the given year
    def getFilingsURLs(self, filingType, fyear):
        
        # Find the index file that contains to this file in each quarter
        output = []
        
        dirpath = "index_files"
        for f in os.listdir(dirpath):
            file = open(f, 'r')
            index_file = file.read()
            
            # Search index file for entry matching this
            for line in index_file.splitlines()[11:]:
                data = line.split("|")
                if int(self.cik) == int(data[0]) and (filingType in data[2]):
                    output.append(Company.ARCHIVE_URL + data[4]) # data[4] = txt file
                    
        return output # returns list of txt file urls corresponding to fyear and filing type

    # Returns the txt content of a filing for this company
    def getFilingsFromURL(self, filingType, fyear):
        
        # Get the files for this filingType on this fiscal year
        urls = self.getFilingsURLs(filingType, fyear)
        
        # Download all of the files
        txtFiles = []
        for url in urls:
            c = requests.get(url).content # what does content do?
            files.append(c)

        return txtFiles # returns list of txt files corresponding to fyear and filing type

    def getHTML(self, filingType, fyear):

        # Get files for this filingType on this fiscal year 
        files = self.getFilingsFromURL(filingType, fyear)

        for f in files:
            with open(f, 'r') as file:
                start = False
                html_list = []
                for line in file: # traverse lines in txt file for html filename
                    if ("<HTML>" in line):
                        start = True
                    if (start):
                        html_list.append(line)
                del html_list[-1] # remove the last element in list--end of file message
                html_txt = "".join(html_list) # join into one string
                
                with open("10-K.html", 'w+') as html_file: # write html content to file, then examine
                    html_file.write(html_txt)
                    html_file.close()

                html_file = open('10-K.html', 'r')
                html_content = html_file.read()
