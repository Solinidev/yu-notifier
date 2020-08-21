import os
from func import *

if __name__ == '__main__':
    base = os.path.dirname(os.path.abspath(__file__)) + '/'

    with open(base + 'acc.txt') as a:
        acc = a.read().strip()
        
    headers = {'Authorization' : 'Bearer ' + acc}
    instance = 'https://botsin.space'

    yunews(base, headers, instance)
    graduinfo(base, headers, instance)
    electroinfo(base, headers, instance)    # 비동기화?