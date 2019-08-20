#!/bin/bash
#script to get a content-length
curl -sI $1 | grep Content-Length | cut -d' ' -f2
