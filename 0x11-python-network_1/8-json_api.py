#!/usr/bin/python3
"""
script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import sys
import requests


if __name__ == "__main__":
    value = "" if len(sys.argv) == 1 else sys.argv[1]
    param_map = {"q": value}
    res = requests.post("http://0.0.0.0:5000/search_user", data=param_map)
    try:
        data = res.json()
        if data == {}:
            print("No result")
        else:
            print("[{}] {}".format(data.get("id"), data.get("name")))
    except ValueError:
        print("Not a valid JSON")
