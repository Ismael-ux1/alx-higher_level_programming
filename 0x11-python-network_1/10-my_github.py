#!/usr/bin/python3
""" takes github credentials and uses the github api to display id """
import requests
import sys


def get_github_id(username, token):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url, auth=(username, token))
    data = response.json()
    return data['id']


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    print(get_github_id(username, token))
