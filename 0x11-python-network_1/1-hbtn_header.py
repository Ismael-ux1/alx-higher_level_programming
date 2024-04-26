#!/usr/bin/python3
""" X-Request-Id header """
import urllib.request
import sys

# Get the URL from command line areguments
url = sys.argv[1]

# Create a Request object with the provided URL
request = urllib.request.Request(url)

# Send a request to the URL
with urllib.request.urlopen(request) as response:
    # Get the value of the X-Request-ID variable from the header,
    # of the response
    request_id = response.headers.get('X-Request-Id')

    # Display the value of the X-Request-Id variable
    if request_id:
        print(request_id)
    else:
        print("No X-Request-Id header found in the HTTP response")
