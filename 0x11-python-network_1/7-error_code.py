#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL and displays the body of the response.
"""

import requests
from sys import argv

def get_request_body(url: str):
    """
    Sends a GET request to the specified URL and displays the body of the response.

    If the HTTP status code is greater than or equal to 400, prints an error message.

    Args:
        url (str): The URL to make the GET request.

    Returns:
        None
    """
    req = requests.get(url)
    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)

if __name__ == "__main__":
    get_request_body(argv[1])
