#!/usr/bin/python3
"""
Posts a request with an email and shows response
"""

if __name__ == '__main__':
    import requests
    from sys import argv

    r = requests.post(argv[1], data={'email': argv[2]})
    print(r.text)
