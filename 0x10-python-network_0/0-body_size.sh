#!/bin/bash
# A Bash script that send a GET request to the URL and display the size of the body of the response

# URL as the first argument to the script
URL="$1"

# Send a request to the URL and get the response body
RESPONSE_BODY=$(curl -s -o /dev/null -w "%{size_download}\n" "$URL")

# Display the size of the response body in bytes
echo "$RESPONSE_BODY"
