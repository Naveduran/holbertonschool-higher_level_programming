#!/usr/bin/python3
"""
POST a letter and receive a json response
"""

if __name__ == '__main__':
    import requests
    from sys import argv

    url = 'http://0.0.0.0:5000/search_user'

    q = ""
    if len(argv) >= 2:
        q = argv[1]

    data = {'q': q}

    try:
        r = requests.post(url, data)
        json = r.json()
        if json:
            print("[{}] {}".format(json.get('id'), json.get('name')))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
