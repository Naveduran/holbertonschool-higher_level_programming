#!/usr/bin/python3
# Fetches a web page whit the module requests
if __name__ == "__main__":
    import requests

    r = requests.get('https://intranet.hbtn.io/status')

    print("Body response:\n\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
