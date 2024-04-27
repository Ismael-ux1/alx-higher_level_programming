#!/usr/bin/python3
""" X-Request-Id header """
import urllib.request
import sys


def get_request_id(url):
    """
    Fetches the X-request-Id header from the given URL

    Args:
       url: The URL to send the request to.
    Returns:
       The value of the X-request-Id header or None if not found.
    """
    with urllib.request.urlopen(url) as response:
        return response.getheader('X-Request-Id')


if __name__ == "__main__":
    url = sys.argv[1]
    print(get_request_id(url))
