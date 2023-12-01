#!/usr/bin/python3
"""
This script takes your GitHub credentials (username and password) and uses the GitHub API to display your id.
"""

import requests
from requests.auth import HTTPBasicAuth
from sys import argv

def get_id_from_github_api(username: str, password: str):
    """
    Uses the GitHub API to display the user's id.

    Args:
        username (str): GitHub username.
        password (str): Personal access token.

    Returns:
        None
    """
    basic_auth = HTTPBasicAuth(username, password)
    url = "https://api.github.com/user"

    headers = {"Accept": "application/vnd.github.v3+json"}
    req = requests.get(url, headers=headers, auth=basic_auth)

    resp_dict = req.json()
    print(resp_dict.get("id"))

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    get_id_from_github_api(username, password)
