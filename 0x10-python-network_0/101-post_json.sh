#!/bin/bash
# JSON POST request to a URL passed as the first arg and displays the body of the response
curl -s -H "Content-Type: application/json" -d @"$2" "$1" "http://localhost:5000"
