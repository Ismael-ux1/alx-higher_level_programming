#!/usr/bin/python3
""" Python script: Get URL, send request, display Request-Id. """
import urllib.request
import sys

# Check if the correct number of arguments are provided
if len(sys.argv) != 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    # Send a GET request to the provided URL
    with urllib.request.urlopen(url) as response:
        # Check if the 'X-Request-Id' header is present in the response
        if 'X-Request-Id' in response.headers:
            x_request_id = response.headers['X-Request-Id']
            print(f"{x_request_id}")
        else:
            print("X-Request-Id header not found in the response.")
except urllib.error.URLError as e:
    print(f"Error: {e}")
