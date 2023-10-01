#!/bin/bash
# GET reque with custom header and display response body
curl -s -H "X-School-User-Id: 98" "$1"
