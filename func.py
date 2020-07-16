import sys
import requests
from bs4 import BeautifulSoup
from links import *

def toot(message, headers, instance):
    t = dict()
    t['status'] = message
    t['visibility'] = 'private'
    requests.post(instance + '/api/v1/statuses', headers = headers, data = t)

def check(fileName, postNum, base):
    with open(base + 'src/' + fileName + '.txt', 'r') as chk:
        preNum = chk.read().strip()
        if preNum == postNum:
            sys.exit()
        else:
            with open(base + fileName + '.txt', 'w') as f:
                f.write(postNum)
    return preNum

def graduinfo(base, headers, instance):
    r = requests.get(graduinfoUrl)
    soup = BeautifulSoup(r.text, 'html.parser')
    ul = soup.findAll('ul', {'class' : 'boardCList'})

    posts = []
    for li in ul:
        for post in li.findAll('li'):
            for a in post.findAll('a'):
                posts.append(a)

    postNum = posts[0].get('title')[5:10].strip()
    preNum = check('graduinfoNum', postNum, base)
    num = int(postNum) - int(preNum)

    for i in range(num):
        msg = ''
        title = posts[i].text
        link = posts[i].get('href')
        msg += title + '\n' + baseUrl + link
        toot(msg, headers, instance)

def yunews(base, headers, instance):
    r = requests.get(yunewsUrl)
    soup = BeautifulSoup(r.text, 'html.parser')
    post = soup.findAll("tr")
    postNum = post[1].text[0:6]

    preNum = check('yunewsNum', postNum, base)

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
        toot(message, headers, instance)