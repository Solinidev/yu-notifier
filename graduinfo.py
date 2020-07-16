import sys
import requests
import main
from bs4 import BeautifulSoup
from links import *

def graduinfo():
    r = requests.get(graduinfoUrl)
    soup = BeautifulSoup(r.text, 'html.parser')
    ul = soup.findAll('ul', {'class' : 'boardCList'})

    # swt = 0
    posts = []
    for li in ul:
        for post in li.findAll('li'):
            for a in post.findAll('a'):
                posts.append(a)
                # if swt:
                #     break
                # postNum = a.get('title')[5:10].strip()
                # print(postNum)
                # swt = 1

    postNum = posts[0].get('title')[5:10].strip()

    with open(main.base + 'graduinfoNum.txt', 'r') as chk:
        preNum = chk.read().strip()
        if preNum == postNum:
            sys.exit()
        else:
            with open(main.base + 'graduinfoNum.txt', 'w') as f:
                f.write(postNum)

    num = int(postNum) - int(preNum)

    for i in range(num):
        msg = ''
        title = posts[i].text
        link = posts[i].get('href')
        msg += title + '\n' + baseUrl + link
        main.toot(msg)