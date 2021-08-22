#!/usr/bin/python3
# Fetch a page and gets an specific header
if __name__ == '__main__':
    import requests
    from sys import argv
    r = requests.get(argv[1])
    print(r.headers.get('X-Request-Id'))
