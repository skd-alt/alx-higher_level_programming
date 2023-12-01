#!/usr/bin/python3
"""uses the GitHub API to display your id"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    authn = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    req = requests.get("https://api.github.com/user", auth=authn)
    print(req.json().get("id"))
