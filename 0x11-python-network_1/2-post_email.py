#!/usr/bin/python3
"""
Send an email through a header in a POST request
"""

if __name__ == "__main__":
    import urllib.parse
    import urllib.request
    from sys import argv
    values = {'email': argv[2]}
    data = urllib.parse.urlencode(values).encode('ascii')
    req = urllib.request.Request(argv[1], data)
    with urllib.request.urlopen(req) as response:
        content = response.read().decode('utf-8')
    print(content)
