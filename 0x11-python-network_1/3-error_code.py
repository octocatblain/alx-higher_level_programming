#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8).
"""

from urllib.request import urlopen, Request
from urllib.error import HTTPError
from sys import argv

def manage_error(url_str: str):
    """
    Sends a request to the specified URL and manages HTTP errors.

    Args:
        url_str (str): The URL to make the request.

    Returns:
        None
    """
    try:
        req = Request(url_str)
        with urlopen(req) as response:
            body = response.read()
        print(body.decode("utf-8"))
    except HTTPError as e:
        print("Error code: {}".format(e.code))

if __name__ == "__main__":
    manage_error(argv[1])
