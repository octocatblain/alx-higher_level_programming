#!/usr/bin/python3
"""
This script takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response.
"""
import requests
from sys import argv

def send_post_request(url: str, email: str):
    """
    Sends a POST request to the specified URL with the provided email as a parameter.

    Args:
        url (str): The URL to make the POST request.
        email (str): The email to include in the request.

    Returns:
        None
    """
    payload = {"email": email}
    req = requests.post(url, data=payload)
    print(req.text)

if __name__ == "__main__":
    send_post_request(argv[1], argv[2])
