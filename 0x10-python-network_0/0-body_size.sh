#!/bin/bash
#This Bash script accepts a URL and sends a request to it.
curl -s "$1" | wc -c
