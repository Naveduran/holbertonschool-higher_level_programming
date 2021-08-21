#!/usr/bin/python3
"""
Get an specific header from the Http response
"""


if __name__ == "__main__":
    import urllib.request
    from sys import argv
    with urllib.request.urlopen(argv[1]) as response:
        id = response.getheader('X-Request-Id')
    print(id)
