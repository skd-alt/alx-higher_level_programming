#!/usr/bin/python3
"""
script that takes in a letter and sends a POST request 
to http://0.0.0.0:5000/search_user
"""
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) == 1:
        char = ""
    else:
        char = sys.argv[1]
    search_req = {"q": char}

    req = requests.post("http://0.0.0.0:5000/search_user", data=search_req)
    try:
        response = req.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
