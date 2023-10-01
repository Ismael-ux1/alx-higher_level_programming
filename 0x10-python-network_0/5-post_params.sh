#!/bin/bash
# POST request with variable in the request body, display response body
url="$1"
email="test@gmail.com"
subject="I will always be here for PLD"

curl -s -d "email=$email&subject=$subject" "$url"
