#!/usr/bin/python3
"""A script that:
- takes your GitHub credentials (username and password)
- uses the GitHub API to display your id
"""

import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    login = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    res = requests.get("https://api.github.com/user", auth=login)
    print(res.json().get("id"))
