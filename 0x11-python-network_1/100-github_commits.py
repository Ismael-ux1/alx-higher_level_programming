#!/usr/bin/python3
import sys
import requests

def get_repo_info(repo_name, owner_name):
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    repo_info = get_repo_info(repo_name, owner_name)
    if repo_info is not None:
        print(f"Repository Name: {repo_info['name']}")
        print(f"Owner: {repo_info['owner']['login']}")
        print(f"Description: {repo_info['description']}")
    else:
        print("Could not fetch the repository information.")
