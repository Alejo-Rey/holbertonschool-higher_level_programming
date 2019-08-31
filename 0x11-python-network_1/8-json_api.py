#!/usr/bin/python3
''' use the requests library '''

import requests
import sys

url = 'http://0.0.0.0:5000/search_user'
try:
    if (len(sys.argv) == 1):
        data = {'q': ''}
        print(data)
    else:
        data = {'q': sys.argv[1]}
        print(data)
    req = requests.post(url, data=data)
    if (len(req.json()) == 0):
        print(req.json())
        print('No result')
    else:
        print('[{}] <{}>'.format(req.json().get('id'), req.json().get('name')))
except:
        print('Not a valid JSON')
