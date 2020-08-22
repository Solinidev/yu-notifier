import time
import requests
from bs4 import BeautifulSoup
from links import *

def toot(message, headers, instance):
    t = dict()
    t['status'] = message
    t['visibility'] = 'private'
    requests.post(instance + '/api/v1/statuses', headers = headers, data = t)

def check(fileName, postNum, base):
    try:
        with open(base + 'src/' + fileName + '.txt', 'r') as chk:
            # for i in range(2):  # check time, date but pass if it's none
            #     preNum = chk.readline().strip()
            #     if preNum is None:
            #         pass
            preNum = chk.read().strip()
            if len(preNum) >= 10:
                raise ValueError
            elif preNum == postNum:
                return preNum
            else:
                with open(base + 'src/' + fileName + '.txt', 'w') as f:
                    f.write(postNum)
        return preNum
    except ValueError:
        if postNum != preNum:
            with open(base + 'src/' + fileName + '.txt', 'w') as d:
                d.write(postNum)
            return
        else:
            return    # can't compare with time need another solutions
            # times = time.strftime('%H:%M:%S', time.localtime(time.time()))
            # with open(base + 'src/' + fileName + '.txt', 'a') as d:
            #     d.write('\n' + times)

# def check_time(fileName, postNum, base):
#     with open(base + 'src/' + fileName + '.txt', 'r') as chk:
#         preNum = chk.readline().strip()
        # only for majorinfo, pass if it is None.

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

def electroinfo(base, headers, instance):
    r = requests.get(electroinfoUrl)
    soup = BeautifulSoup(r.text, 'html.parser')
    posts = soup.findAll("tr", {"style" : "height:30px;background:#fafafa;"})

    date = []
    for i in posts:
        for day in i.findAll("td"):
            if len(day.text) != 10:
                pass
            else:
                date.append(day.text)
    check('electroinfo', date[0], base)  # returned previous num
    msg = '새로운 학과 공지사항이 있습니다.\n' + electroinfoUrl
    toot(msg, headers, instance)


    # 임시방편, 하루 뒤 알림 받으므로 개선 필요