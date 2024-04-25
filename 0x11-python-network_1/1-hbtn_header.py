#!/usr/bin/python3
""" Python script: Get URL, send request, display Request-Id. """
import urllib.request
import sys


# Get the URL from command line areguments
url = sys.argv[1]

# Send a GET request to the provided URL
with urllib.request.urlopen(url) as response:
    # Get the value of the X-Request-ID variable from the header,
    # of the response
    request_id = response.headers.get('X-Request-Id')

    # Display the value of the X-Request-Id variable
    print(request_id)
