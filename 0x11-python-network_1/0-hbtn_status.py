#!/usr/bin/python3
# A python script that fetches https://alx-intranet.hbtn.io/status
import urllib.request
# Define the URL
url = 'https://alx-intranet.hbtn.io/status'

# Open the URL using urlib
with urllib.request.urlopen(url) as response:
    # Read the content of the response
    content = response.read()
    # Decode the content into UTF-8 format
    utf8_content = content.decode('utf-8')

# Display the body response
print("Body response:")
# Display the type of the content
print("\t- type:", type(content))
# Display the content
print("\t- content:", content)
# Display the content in UTF-8 format
print("\t- utf8 content:", utf8_content)
