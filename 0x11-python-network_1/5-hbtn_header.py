#!/usr/bin/python3
# Fetch a page and gets an specific header
import requests
from sys import argv
r = requests.get(argv[1])
print("Body response:\n\t- type: {}".format(type(r.text)))
print("\t- content: {}".format(r.text))
