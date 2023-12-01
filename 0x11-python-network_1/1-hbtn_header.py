#!/usr/bin/python3
#  script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response.

import urllib.request
import sys

def get_x_request_id(url):
    try:
        with urllib.request.urlopen(url) as response:
            headers = response.headers
            x_request_id = headers.get('X-Request-Id')
            return x_request_id
    except urllib.error.HTTPError as e:
        return "Error: {}".format(e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    x_request_id = get_x_request_id(url)
    print(x_request_id)
