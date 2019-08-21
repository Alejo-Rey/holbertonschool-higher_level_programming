#!/bin/bash
# scrip to sent post request in a file
curl -sX post -H "Content-Type: application/json" -d "@$1" $2
