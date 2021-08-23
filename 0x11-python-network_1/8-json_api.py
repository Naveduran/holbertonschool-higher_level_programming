#!/usr/bin/python3
"""
POST a letter and receive a json response
"""

if __name__ == '__main__':
    import requests
    from sys import argv

    url = 'http://c0cd6e92.hbtn-cod.io:5000/search_user'

    q = ""
    if len(argv) >= 2:
        q = argv[1]

    data = {'q': q}

    r = requests.post(url, data)

    if r.headers.get('Content-Type') == 'application/json':
        json = r.json()
        if json:
            print("[{}] {}".format(json.get('id'), json.get('name')))
        else:
            print("No result")
    else:
        print("Not a valid JSON")
