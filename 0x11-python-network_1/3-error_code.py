#!/usr/bin/python3
"""
Manage errors from a HTTP response
"""

if __name__ == "__main__":
    from urllib.request import Request, urlopen
    from urllib.error import URLError, HTTPError
    from sys import argv

    request = Request(argv[1])

    try:
        with urlopen(request) as response:
            content = response.read().decode()
        print(content)

    except HTTPError as error:
        if hasattr(error, 'code'):
            print("Error code: {}".format(error.code))
