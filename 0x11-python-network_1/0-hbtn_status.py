#!/usr/bin/python3
# A python script that fetches https://alx-intranet.hbtn.io/status
import urllib.request


if __name__ == "__main__":

    # Define the URL
    url = 'https://alx-intranet.hbtn.io/status'

    with urllib.request.urlopen(url) as response:
        html = response.read()
        print("Body response:")
        print("    - type: {}".format(type(html)))
        print("    - content: {}".format(html))
        print("    - utf8 content: {}".format(html.decode('utf-8')))
