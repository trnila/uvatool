import datetime
import logging
import pickle
from sys import path
import urllib.parse

import requests
import sys
from lxml import html

import settings

storage = '/tmp/uva.storage'

class Problem:
    def __init__(self, data):
        self.submit_id = int(data[0])
        self.problem_id = int(data[1])
        self.name = data[2]
        self.verdict = data[3]
        self.language = data[4]
        self.runtime = float(data[5])
        self.submitted = datetime.datetime.strptime(data[6], "%Y-%m-%d %H:%M:%S")

    def is_accepted(self):
        return self.verdict == 'Accepted'

class Uva:
    def __init__(self):
        self.session = self._create_session()

    def _create_session(self):
        try:
            with open(storage, 'rb') as f:
                logging.debug("Loading cookies from %s" % storage)
                session = requests.Session()
                session.cookies = requests.utils.cookiejar_from_dict(pickle.load(f))
                return session
        except FileNotFoundError:
            client = requests.Session()
            self._login(client)
            return client

    def _login(self, client):
        if not settings.credentials:
            print("Set login credentials in ~/.uvatool")
            sys.exit(1)

        res = client.get("https://uva.onlinejudge.org/index.php?option=com_comprofiler&task=login")
        tree = html.fromstring(res.content)

        data = dict(
            [(i.attrib['name'], i.attrib.get('value', '')) for i in tree.xpath("//form[@id='mod_loginform']//input")])
        data['username'] = settings.credentials['username']
        data['passwd'] = settings.credentials['password']

        res = client.post("https://uva.onlinejudge.org/index.php?option=com_comprofiler&task=login", data)
        tree = html.fromstring(res.content)

        # save cookies
        with open(storage, 'wb') as f:
            pickle.dump(requests.utils.dict_from_cookiejar(client.cookies), f)

    def _get(self):
        pass

    def stringify_children(self, node):
        parts = [
            node.text
        ]
        for c in node.getchildren():
            parts.append(c.text)

        return ''.join(filter(None, parts)).strip()


    def submit(self, id, file):
        data = {
            "problemid": "",
            "category": "",
            "localid": id,
            "language": 3,
            "code": "",
            "submit": "Submit"
        }

        files = {
            "codeupl": ("main.c", open(file))
        }

        res = self.session.post("https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=25&page=save_submission", data, files=files)
        parsed_url = urllib.parse.urlparse(res.url)
        msg = urllib.parse.parse_qs(parsed_url.query)['mosmsg'][0]
        return int(msg.split(' ')[-1])

    def stats(self):
        res = self.session.get("https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=9")
        tree = html.fromstring(res.content)

        return [Problem([self.stringify_children(i) for i in i.xpath('td')]) for i in tree.xpath("//div[@id='col3_content_wrapper']//tr")[1:-2]]