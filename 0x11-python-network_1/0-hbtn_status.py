#!/usr/bin/python3
"""A script that
- fetches https://alx-intranet.hbtn.io/status.
- uses urlib package
"""


if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as resquest:
        page_info= resquest.read()
        print("Body response:")
        print("\t- type: {}".format(type(page_info)))
        print("\t- content: {}".format(page_info))
        print("\t- utf8 content: {}".format(page_info.decode('utf-8')))
