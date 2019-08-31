#!/usr/bin/python3
''' use the requests library '''

import requests
import sys

url = 'http://0.0.0.0:5000/search_user'
try:
    if (len(sys.argv[1]) == 0):
        data = {'q': ''}
    else:
        data = {'q': sys.argv[1]}
    req = requests.post(url, data=data)
    if (len(req.json()) == 0):
        print('No result')
    else:
        print('[{}] <{}>'.format(req.json().get('id'), req.json().get('name')))
except:
        print('Not a valid JSON')
