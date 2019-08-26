#!/usr/bin/python3
'''Send a request (POST) with a email'''
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    value = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(value).encode('utf-8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as res:
        html = res.read()
        print(html.decode('utf-8'))
