#!/usr/bin/python3
'''Script to display the error message'''
from urllib.request import Request, urlopen
import urllib.error
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    req = Request(url)
    try:
        with urlopen(req) as res:
            print(res.read().decode())
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
