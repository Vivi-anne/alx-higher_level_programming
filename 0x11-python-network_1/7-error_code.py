#!/usr/bin/python3
"""A script that send request to URL & display response body
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    res = requests.get(url)
    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)
