#!/bin/bash
# takes in a URL sends a request to it, and displays the size of the body
curl --output /dev/null -w '%{size_download}\n' --silent $1