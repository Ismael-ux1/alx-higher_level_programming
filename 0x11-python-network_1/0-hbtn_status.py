#!/usr/bin/python3
# A python script that fetches https://alx-intranet.hbtn.io/status
if __name__ == "__main__":
    import urllib.request

    # Use a with statement to open the url and
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode('utf-8')))
