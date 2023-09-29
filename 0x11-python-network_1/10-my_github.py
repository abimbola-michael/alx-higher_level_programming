#!/usr/bin/python3
"""
script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""

import requests
import sys


if __name__ == "__main__":
    uname = sys.argv[1]
    passwd = sys.argv[2]
    res = requests.get("https://api.github.com/user", auth=(uname, passwd))
    if res.status_code == 200:
        print(response.get("id"))
    else:
        print("Unable to get data")
