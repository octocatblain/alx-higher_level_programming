#!/usr/bin/python3
"""
    This script takes 2 arguments to list 10 commits (from the most recent to oldest    ) of the repository “rails” by the user “rails”
"""

import requests
from sys import argv

def get_commits_github(repository: str, owner: str):
    """
    Retrieves and displays the latest 10 commits from a GitHub repository.

    Args:
        repository (str): GitHub repository name.
        owner (str): GitHub owner name.

    Returns:
        None
    """
    url = f"https://api.github.com/repos/{owner}/{repository}/commits"
    headers = {"Accept": "application/vnd.github+json"}
    req = requests.get(url, headers=headers)

    list_commits = req.json()

    for commit_dict in list_commits[:10]:
        name = commit_dict.get("commit").get("author").get("name")
        sha = commit_dict.get("sha")
        print("{}: {}".format(sha, name))

if __name__ == "__main__":
    repository = argv[1]
    owner = argv[2]
    get_commits_github(repository, owner)
