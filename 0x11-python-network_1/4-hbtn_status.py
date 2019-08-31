#!/usr/bin/python3
''' use the requests library '''

import requests

req = requests.get('https://intranet.hbtn.io/status')
print("Body response:\n\t- type: {}".format(type(req.text)))
print("\t- content: {}".format(req.text))
