import sys
import requests
import main
from bs4 import BeautifulSoup
from links import *

r = requests.get(yunewsUrl)
soup = BeautifulSoup(r.text, 'html.parser')
post = soup.findAll("tr")
postNum = post[1].text[0:6]

with open(main.base + 'pointNum.txt', 'r') as chk:
    preNum = chk.read().strip()
    if preNum == postNum:
        sys.exit()
    else:
        with open(main.base + 'pointNum.txt', 'w') as f: # 개선 여지?
            f.write(postNum)

num = int(postNum) - int(preNum)
posts = []
postTag = soup.findAll('a')

for i in postTag:
    title = i.get('title')
    if title is None or '새창으로' in title or '팝업' in title or '현재페이지 프린트' in title:
        pass
    else:
        msg = ''
        link = i.get('href')
        msg += title + '\n' + baseUrl + link
        posts.append(msg)

for j in range(num):
    message = posts[j]
    main.toot(message)