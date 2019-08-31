#!/usr/bin/python3
''' use the requests library '''

import requests
import sys

try:
    req = requests.get(sys.argv[1])
    print("{}".format(req.headers.get('X-Request-Id')))
except:
    pass
