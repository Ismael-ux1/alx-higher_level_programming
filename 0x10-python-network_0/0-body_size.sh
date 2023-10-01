#!/bin/bash
# A Bash script that  GET request to the URL and,
# display the size of the body of response in byte
curl -s "$1" | wc -c
