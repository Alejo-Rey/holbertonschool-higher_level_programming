#!/usr/bin/python3
''' use the requests library '''

import requests
import sys

try:
    req = requests.get(sys.argv[1])
    if (req.status_code > 400):
        print("Error code: {}".format(req.status_code))
    else:
        print("{}".format(req.text))
except:
    pass
