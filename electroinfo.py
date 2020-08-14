import requests
from bs4 import BeautifulSoup
from links import *

base = os.path.dirname(os.path.abspath(__file__)) + '/'

r = requests.get(electroinfoUrl)
soup = BeautifulSoup(r.text, 'html.parser')
# post = soup.findAll("tbody")
# title = soup.findAll("td", {'class' : 'B'})

title = soup.findAll("tr", {"style" : "height:30px;background:#fafafa;"})

date = []
for i in title:
    for j in i.findAll("td"):
        # if j.text is None:
        #     pass
        if len(j.text) != 10:
            pass
        else:
            date.append(j.text)

prev = check('electroinfo', date[0], base)
msg = '새로운 학과 공지사항이 있습니다.\n' + electroinfoUrl

if prev != date[0]:
    toot(msg, headers, instance)

# 게시판 번호 없음, notice와 일반 게시글이 분리되어 있음