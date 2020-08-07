import requests
import re
import numbers
from bs4 import BeautifulSoup

def chunk(l, n):
  for i in range(0, len(l), n):
    yield l[i:i + n]

# a must be 2 dimensional array
def shift_up(a):
  for i in range(len(a)):
    try:
      a[i][i] = a[i][i+1]
    except:
      print('failed')

url = 'http://www.necaracing.com/april-27-2018.html'
data = requests.get(url)
soup = BeautifulSoup(data.text, 'html.parser')
results = [];
for p in soup.find_all('div', {'class':'paragraph'}):
  res = " ".join(p.text.split()).replace('#', '').replace('Rank School Car  Laps Best Lap Time', '')
  print(res)
  # res = re.findall("[a-zA-Z", res)
  # print(res)


  #   rank      school      car           laps            best-lap-time
  #   num       text        num           float           float
  #   [0-9][.]  [a-zA-Z]    [0-9]{3}    [\d\d]{0-2}    [\d\d.\d\d\d]
  #   1.        CLTC        021           69              41.863
  #   "^[0-9][.][a-zA-Z][0-9]{3}[0-9]{0-3}[\d\d.\d\d\d]$"

  txt = "1.CLTC0216941.863";
  
  result = re.findall(r"^[0-9][.][a-zA-Z][0-9]{3}[0-9]{0-3}[\d\d.\d\d\d]$", txt)
  print(result)








  # res[4:7] = [' '.join(res[4:7])]
  # res = list(chunk(res, 5))
  # print('\n\n', res)

  # for i in range(len(res)):
  # for i in range(len(res)-1):
  #   if res[i][2].isalpha():
  #     print("%s is alpha" % (res[i][2]))
  #   else:
  #     print("%s is not alpha" % (res[i][2]))
    # try:
    #   intg = int(round(res[i][2])))
    # except:
    #   print(str(res[i][2]) + " is not a integer")
      # if res[i][2].isdigit():
      #   print('%s is a digit' % res[i][3])
      #   res[i][4:5] = [''.join(res[i][3:4])] 
      # else:
      #   print('%s is not a digit' % res[i][3])
        

  # print('\n \n', res)


