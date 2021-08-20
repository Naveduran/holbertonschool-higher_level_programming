#!/usr/bin/python3
# fetches https://intranet.hbtn.io/status


if __name__ == "__main__":
    # fetches a web page
    import urllib.request
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        page = response.read()
    str = """Body response:\n\t- type: {}\n\t- content: {}
\t- utf8 content: {}""".format(type(page), page,
                               page.decode(encoding='utf-8'))
    print(str)
