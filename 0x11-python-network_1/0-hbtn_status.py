#!/usr/bin/python3

"""Write a Python script that 
-fetches https://alx-intranet.hbtn.io/status
"""

if __name__ == "__main__":
    import urllib.request

    url = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(url) as request:
        res = request.read()
        print("Body response:")
        print("\t- type: {}".format(type(res)))
        print("\t- content: {}".format(res))
        print("\t- utf8 content: {}".format(res.decode('utf-8')))