import os

UDEBUG_WWW = "https://www.udebug.com"
UVA_WWW = "https://uva.onlinejudge.org"

credentials = None

try:
    with open(os.path.expanduser("~") + "/.uvatool") as f:
        data = dict([i.split('=', 1) for i in f.read().splitlines()])
        if 'username' in data and 'password' in data:
            credentials = data
except FileNotFoundError:
    pass
