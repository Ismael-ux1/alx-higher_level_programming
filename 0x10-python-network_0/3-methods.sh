#!/bin/bash
# Send and OPTIONS request to the url and display the allowed HTTP methods
curl -sI -X OPTIONS "$1" | grep -i 'Allow' | sed 's/Allow: //i'
