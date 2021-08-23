#!/usr/bin/python3
"""
Using the GITHUB API and the user rails
"""

if __name__ == '__main__':
    import requests
    from sys import argv

    url = 'https://api.github.com/repos/{}/{}/commits'.format(argv[2],
                                                              argv[1])
    try:
        r = requests.get(url)
        for i in range(10):
            sha = r.json()[i].get('sha')
            name = r.json()[i].get('commit').get('author').get('name')
            print("{}: {}".format(sha, name))
    except:
        pass
