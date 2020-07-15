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

with open(base + 'pointNum.txt', 'r') as chk:
    preNum = chk.read().strip()
    if preNum == postNum:
        sys.exit()
    else:
        with open(base + 'pointNum.txt', 'w') as f: # 개선 여지?
            f.write(postNum)

num = int(postNum) - int(preNum)

# postTitle = soup.findAll("td", {'class' : 'title'})
# title = postTitle[0].get('title')
# print(postTitle[0])
# print(title)

postTag = soup.findAll('a')
for i in range(num):
    for j in postTag:
        title = j.get('title')
        if title is None or '새창으로' in title or '팝업' in title or '현재페이지 프린트' in title:
            pass
        else:
            print(title)
# print(test)

for k in postTag:
    link = k.get('href')
    print(link)