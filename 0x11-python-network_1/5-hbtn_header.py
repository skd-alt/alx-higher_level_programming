#!/usr/bin/python3
""" Takes in URL requests it and gets the X-Request id"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    req = requests.get(url)
    print(req.headers.get("X-Request-Id"))
