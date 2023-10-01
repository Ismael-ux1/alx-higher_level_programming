#!/bin/bash
# Send a JSON POST request with the contents of a file in the request body
curl -s -H "Content-Type: application/json" -X POST --data "@$2" "$1"
