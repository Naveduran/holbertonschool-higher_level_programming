#!/usr/bin/python3
# fetches https://intranet.hbtn.io/status

import urllib.request

if __name__ == "__main__":
    # fetches a web page
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        the_page = response.read()
    content = str(the_page).split("'")[1]
    str = """Body response:
    - type: {}
    - content: {}
    - utf8 content: {}""".format(type(the_page), the_page, content)
    print(str)
