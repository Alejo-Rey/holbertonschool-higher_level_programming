#!/bin/bash
# script to get the status of the request
curl -so --head --write-out '%{http_code}' $1
