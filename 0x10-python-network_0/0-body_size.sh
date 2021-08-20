#!/bin/bash
# request an URL and displays the size of the body of the response
curl "$1" -sD Y -o Z && grep "Content-Length:" Y | awk '{print $2}'
