#!/usr/bin/python3
""" Displays the value of the variable X-Request-Id in the response header """
import requests
import sys


def get_request_id(url):
    """ doc """
    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))


if __name__ == '__main__':
    url = sys.argv[1]
    get_request_id(url)
