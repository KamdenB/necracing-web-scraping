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
    if re.match(r"^(?!((\w+)\.html)$)", href): # Removes the single word links
        if re.match(r"^(\w+)(-*)(\d*)(-*)(\d*)\.html", href): #word-number-number.html
            filter_res.append(href)
        elif re.match(r"^(\w+)(-*)(\w+)(-*)(\d*)(-*)(\d*)\.html", href): #word-word-number-number-number.html
            filter_res.append(href)
        elif re.match(r"^(\w+)(-*)(\w+)(-*)(\w+)(-*)(\d*)\.html", href): #word-word---date-number.html
            filter_res.append(href)

with open("data.txt", "w+", encoding='utf-8') as file:
    for f in filter_res:
        u = "{0}{1}".format(url, f)
        print(u)
        data = requests.get(u)
        print(data)
        soup = BeautifulSoup(data.text, 'html.parser')
        results = []
        for p in soup.find_all('div', class_="paragraph"): # Not even getting this far for some reason
            r = str(" ".join(p.text.split()).replace('#', '').replace('Rank School Car  Laps Best Lap Time', ''))
            file.write("{0}\n".format(r))
    file.close()