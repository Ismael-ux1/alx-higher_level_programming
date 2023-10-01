#!/bin/bash
# A Bash script that  GET request to the URL and,
# display the size of the body of the response
curl -sI "$1" | grep 'Content-Length' | awk '{print $2}'
