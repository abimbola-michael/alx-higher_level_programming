#!/usr/bin/python3
"""script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays
the body of the response (decoded in utf-8)
"""

import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    url = sys.argv[1]
    param_map = {"email": sys.argv[2]}
    params = urllib.parse.urlencode(param_map).encode("ascii")
    req = urllib.request.Request(url, params)
    with urllib.request.urlopen(req) as res:
        print(res.read().decode("utf-8"))