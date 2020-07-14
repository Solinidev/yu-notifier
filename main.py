import os
import requests
from bs4 import BeautifulSoup

base = os.path.dirname(os.path.abspath(__file__)) + '/'

firstUrl = 'http://www.yu.ac.kr/_korean/about/index.php?c=about_08_a_list'
r = requests.get(firstUrl)
soup = BeautifulSoup(r.text, 'html.parser')
post = soup.findAll("tr")
postNum = post[1].text[0:6] # txt파일의 postNum과 대치 후 다르면 새로 저장
print(postNum)

postTitle = soup.findAll("td", {'class' : 'title'})
print(postTitle[0])