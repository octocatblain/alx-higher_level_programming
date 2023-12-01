#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header.
"""

import requests
from sys import argv

def get_request(url: str):
    """
    Sends a GET request to the specified URL and prints the value of the X-Request-Id header.

    Args:
        url (str): The URL to make the GET request.

    Returns:
        None
    """
    req = requests.get(url)
    print(req.headers.get("X-Request-Id"))

if __name__ == "__main__":
    get_request(argv[1])
