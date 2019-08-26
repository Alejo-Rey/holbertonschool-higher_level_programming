#!/usr/bin/python3
'''send a request and desplay the value of the
one header response '''
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    header = 'X-Request-Id'
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as res:
        print(res.getheader(header))
