#!/bin/bash
# A Bash script that send a GET request to the URL and display the size of the body of the response


# Url as the first argument to the script
Url=$1

# Send a request to the URL and display only the size of the body of the response in bytes
curl -sI "$1" | grep 'Content-Length' | awk '{print $2}'
