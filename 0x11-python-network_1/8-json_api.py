#!/usr/bin/python3
"""
Script that takes in letter and send POST request
with the letter as a parameter
"""
import requests
import sys


def send_post_request(letter=""):
    url = "http://0.0.0.0:5000/search_user"
    data = {"q": letter}

    try:
        response = requests.post(url, data=data)
        response_json = response.json()

        if response_json:
            print("[{}] {}".format(response_json.get("id"),
                  response_json.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    send_post_request(letter)
