import os
import sys
import requests
from bs4 import BeautifulSoup
from links import *

base = os.path.dirname(os.path.abspath(__file__)) + '/'

r = requests.get(firstUrl)
soup = BeautifulSoup(r.text, 'html.parser')
post = soup.findAll("tr")
postNum = post[1].text[0:6]
# print(postNum)

with open(base + 'pointNum.txt', 'r') as chk:
    preNum = chk.read().strip()
    if preNum == postNum:
        print('dd')
        sys.exit()
    else:
        with open(base + 'pointNum.txt', 'w') as f:
            f.write(postNum)
            print('h')



postTitle = soup.findAll("td", {'class' : 'title'})
print(postTitle[0])