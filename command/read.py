import os
import sys
import subprocess

import requests
from settings import UVA_WWW, UDEBUG_WWW, DEBUGGING
from lxml import html


class Read:
    def run(self, args):
        id = os.path.basename(os.getcwd())
        if DEBUGGING :
            print(id)

        res = requests.get(UDEBUG_WWW + "/UVa/" + id)
        tree = html.fromstring(res.content)
        url = tree.xpath("//a[contains(@class, 'problem-statement')]/@href[1]")[0]

        res = requests.get(url)
        tree = html.fromstring(res.content)
        pdf = UVA_WWW + '/' + tree.xpath('//img[@alt="Download as PDF"]/parent::a/@href')[0]
        os.system(subprocess.list2cmdline(['xdg-open' if sys.platform == "linux" else 'open', pdf]))
