#!/bin/bash
# send a request to an URL with curl
# Displays the byte size of the body of the response
curl -s "$1" | wc -c
