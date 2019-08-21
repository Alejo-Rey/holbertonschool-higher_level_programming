#!/bin/bash
# script to send a post method with values
curl -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" $1
