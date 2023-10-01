#!/bin/bash
# POST request with variable in the request body, display response bod
curl -s -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
