#!/bin/bash
# find a specific request
curl -sLX PUT -d "user_id=98" -H "Origin: HolbertonSchool" $1
