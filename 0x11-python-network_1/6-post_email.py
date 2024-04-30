#!/usr/bin/python3
""" displays the body of the response """
import requests
import sys


def post_email(url, email):
    data = {'email': email}
    response = requests.post(url, data=data)
    print(response.text)


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    post_email(url, email)
