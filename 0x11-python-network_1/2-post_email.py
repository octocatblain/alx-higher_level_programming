#!/usr/bin/python3
"""
This script takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8)
"""

from urllib.request import urlopen, Request
from urllib.error import URLError
from urllib.parse import urlencode
from sys import argv

def make_post_request(url_str: str, email_arg: str):
    """
    Makes a POST request to the specified URL with the provided email.

    Args:
        url_str (str): The URL to make the POST request.
        email_arg (str): The email to include in the request.

    Returns:
        None
    """
    try:
        data = urlencode({"email": email_arg})
        email = data.encode("utf-8")
        req = Request(url_str, email)
        with urlopen(req) as response:
            body = response.read()
        print(body.decode("utf-8"))
    except URLError as e:
        if hasattr(e, "reason"):
            print(e.reason)
        elif hasattr(e, "code"):
            print(e.code)

if __name__ == "__main__":
    make_post_request(argv[1], argv[2])
