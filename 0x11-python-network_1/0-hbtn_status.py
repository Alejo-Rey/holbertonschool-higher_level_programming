#!/usr/bin/python3
''' request  and response liblary '''
import urllib.request


if __name__ == "__main__":
    req = urllib.request.Request('https://intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as res:
        html = res.read()
        print('Body response:')
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf-8 content: {}".format(html.decode(encoding='UTF-8')))
