#!/usr/bin/env python3
import sys
import requests
from multiprocessing.dummy import Pool

requests.urllib3.disable_warnings()

try:
    target = [i.strip() for i in open(sys.argv[1], mode='r').readlines()]
except IndexError:
    exit('python3 script.py urilist.txt 50')

usragt = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

def check(uri):
    try:
        if not uri.endswith('/'):
            uri = uri + '/'
        if not uri.startswith('http'):
            uri = 'http://' + uri

        r = requests.get(url, headers=usragt, timeout=10)
        if r.status_code == 200:
            print (uri+' OK\n')
            with open('200.txt', mode='a') as d:
                d.write(uri + '/\n')
    except:
        pass

mp = Pool(sys.argv[2])
mp.map(check, target)
mp.close()
mp.join()
