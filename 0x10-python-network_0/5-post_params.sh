#!/bin/bash
# script to send a post method with values
curl -sd "email: hr@holbertonschool.com" -sd "subject: I will always be here for PLD" $1
