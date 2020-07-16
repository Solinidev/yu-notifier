import requests
from bs4 import BeautifulSoup
from links import *

r = requests.get(electroinfoUrl)
soup = BeautifulSoup(r.text, 'html.parser')
post = soup.findAll("td", {'class' : 'B'})
print(post[0].text)

# 게시판 번호 없음, notice와 일반 게시글이 분리되어 있음