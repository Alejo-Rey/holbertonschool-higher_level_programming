#!/usr/bin/python3
''' use the requests library '''

import requests
import sys

try:
    data = {'email': sys.argv[2]}
    req = requests.post(sys.argv[1], data=data)
    print("{}".format(req.text))
except:
    pass
