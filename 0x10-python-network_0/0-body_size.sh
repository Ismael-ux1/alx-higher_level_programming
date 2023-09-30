#!/bin/bash
# A Bash script that send a GET request to the URL and display the size of the body of the response

# Send a request to the URL and display only the size of the body of,
# the response in bytes
curl -sI "$1" | grep 'Content-Length' | cut -d' ' -f2
