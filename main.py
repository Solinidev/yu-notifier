import os
import sys
import requests
from bs4 import BeautifulSoup
from links import *

base = os.path.dirname(os.path.abspath(__file__)) + '/'
with open(base + 'acc.txt') as a:
    acc = a.read().strip()
headers = {'Authorization' : 'Bearer ' + acc}
instance = 'https://botsin.space'

def toot(message):
    t = dict()
    t['status'] = message
    t['visibility'] = 'private'
    requests.post(instance + '/api/v1/statuses', headers = headers, date = t)

import graduinfo
graduinfo.graduinfo()