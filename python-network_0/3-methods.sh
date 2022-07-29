#!/bin/bash
# URL that displays all HTTP
curl -sI "$1" | grep "Allow: " | sed 's/Allow: //'
