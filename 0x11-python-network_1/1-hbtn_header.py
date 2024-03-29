#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id variable found in the
header of the response
"""
import urllib.request
import sys


if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as res:
        head_map = dict(res.headers)
        print(head_map.get("X-Request-Id"))
