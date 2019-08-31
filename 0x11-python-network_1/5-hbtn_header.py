#!/usr/bin/python3
''' use the requests library '''

import requests

req = requests.get('https://intranet.hbtn.io/status')
print("{}".format(req.headers.get('X-Request-Id')))
