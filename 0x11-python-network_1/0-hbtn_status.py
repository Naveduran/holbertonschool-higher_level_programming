#!/usr/bin/python3
"""
Fetches https://intranet.hbtn.io/status
"""


if __name__ == "__main__":
    import urllib.request
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        page = response.read()
    print("Body response:\n\t- type: {}".format(type(page)))
    print("\t- content: {}".format(page))
    print("\t- utf8 content: {}".format(page.decode(encoding='utf-8')))
