#!/bin/bash
# request an URL and displays the body of the html
curl "$1" -sD Y -o Z && if [[ $(grep '200 OK' Y ) ]] ; then cat Z; fi
