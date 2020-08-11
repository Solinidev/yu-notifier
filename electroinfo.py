import requests
from bs4 import BeautifulSoup
from links import *

r = requests.get(electroinfoUrl)
soup = BeautifulSoup(r.text, 'html.parser')
post = soup.findAll("tbody")
# title = soup.findAll("td", {'class' : 'B'})

title = soup.findAll("tr", {"style" : "height:30px;background:#fafafa;"})

for i in title:
    for j in i.findAll("td"):
        # if j.text is None:
        #     pass
        if len(j.text) != 10:
            pass
        print(j.text)


# 게시판 번호 없음, notice와 일반 게시글이 분리되어 있음