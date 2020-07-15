import requests
import main
from bs4 import BeautifulSoup
from links import *

r = requests.get(graduinfoUrl)
soup = BeautifulSoup(r.text, 'html.parser')
# post = soup.findAll('div', {'class' : 'div_content content_top'})
# postNum = post.get('title')

# post = soup.findAll('ul', {'class' : 'boardCList'})
post = soup.findAll('a')
num = post.get('title')
print(num)