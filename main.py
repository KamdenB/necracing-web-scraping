from bs4 import BeautifulSoup
import requests
import re

url = 'http://www.necaracing.com/' # Website
extension = 'html' # File extnesion to find

def ListFiles(url, ext=''):
    page = requests.get(url).text # Get page
    soup = BeautifulSoup(page, 'html.parser') # Parse html
    return [
        url + '/' + node.get('href') 
        for node in soup.find_all('a') 
        if node.get('href').endswith(ext)
    ] # Return all files with extion extension

urls = [file.replace('///', '/') for file in ListFiles(url, extension)]
filtered = [x.split(url)[1] for x in urls] 

filter_res = []
for href in filtered:
    if re.match(r"^(?!((\w+)\.html)$)", href):
        if re.match(r"^(\w+)(-*)(\d*)(-*)(\d*)\.html", href): #word-number-number.html
            filter_res.append(href)
        elif re.match(r"^(\w+)(-*)(\w+)(-*)(\d*)(-*)(\d*)\.html", href): #word-word-number-number-number.html
            filter_res.append(href) 
        elif re.match(r"^(\w+)(-*)(\w+)(-*)(\w+)(-*)(\d*)\.html", href): #word-word---date-number.html
            filter_res.append(href)

print("Filter pt2: %s" % filter_res)