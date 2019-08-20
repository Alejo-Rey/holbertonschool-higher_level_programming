!/bin/bash
# scrip to get the allow methods
curl -sI $1 | grep Allow | cut -d" " -f2,3,4B
