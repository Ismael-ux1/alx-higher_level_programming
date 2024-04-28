#!/usr/bin/python3
""" displays the body of the response """
import urllib.request
import urllib.error
import sys


def fetch_url_content(url):
    """ doc """
    try:
        # Send an HTTP request to the URL
        with urllib.request.urlopen(url) as response:
            # Read the response body and decode it in UTF-8
            content = response.read().decode('utf-8')
            print(content)
    except urllib.error.HTTPError as e:
        # Handle HTTP errors
        print(f"Error code: {e.code}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <URL>")
        sys.exit(1)

    url_to_fetch = sys.argv[1]
    fetch_url_content(url_to_fetch)
