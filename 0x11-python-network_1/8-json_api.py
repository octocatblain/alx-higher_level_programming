#!/usr/bin/python3
"""
This script takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
from sys import argv

def search_user(letter: str):
    """
    Sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.

    If the response body is properly JSON formatted and not empty, displays the id and name.
    Otherwise, displays an appropriate message.

    Args:
        letter (str): The letter to search for.

    Returns:
        None
    """
    payload = {"q": letter}
    url = "http://0.0.0.0:5000/search_user"
    req = requests.post(url, data=payload)

    try:
        resp_dict = req.json()
        if resp_dict:
            print("[{}] {}".format(resp_dict.get("id"), resp_dict.get("name")))
        else:
            print("No result")
    except requests.exceptions.JSONDecodeError:
        print("Not a valid JSON")

if __name__ == "__main__":
    try:
        letter = argv[1]
    except IndexError:
        letter = ""
    finally:
        search_user(letter)
