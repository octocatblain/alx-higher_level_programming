#!/usr/bin/python3
"""
This script fetches https://alx-intranet.hbtn.io/status using the request package.
"""

import requests

def get_request():
    req = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(req.text)))
    print("\t- content: {}".format(req.text))

if __name__ == "__main__":
    get_request()
