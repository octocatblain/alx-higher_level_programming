#!/usr/bin/python3
""" This script takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response."""

from urllib.request import urlopen, Request
from urllib.error import URLError
from sys import argv


def get_header_value(url_str: str):
    try:
        req = Request(url_str)
        with urlopen(req) as response:
            body = response.read()
        print(response.info().get("X-Request-Id"))
    except URLError as e:
        if hasattr(e, "reason"):
            print(e.reason)
        elif hasattr(e, "code"):
            print(e.code)


if __name__ == "__main__":
    get_header_value(argv[1])
