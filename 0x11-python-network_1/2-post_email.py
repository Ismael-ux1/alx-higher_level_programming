#!/usr/bin/python3
""" displays the body of the response """
import sys
import urllib.request
import urllib.parse


def send_post_request(url, email):
    """ doc """
    # Encode the email parameter
    data = urllib.parse.urlencode({'email': email})
    # Convert to bytes
    data = data.encode('ascii')

    # Send a POST request to the url with the email as a parameter
    with urllib.request.urlopen(url, data) as response:
        # Return the body of the response decoded in utf-8
        return response.read().decode('utf-8')


if __name__ == "__main__":
    # Get the URL and email from the command-line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # print the response body
    print(send_post_request(url, email))
