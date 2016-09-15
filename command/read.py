import os
import logging
import subprocess
from shutil import copyfile

import requests
from lxml import html


class Read():
    def run(self, args):
        id = os.path.basename(os.getcwd())
        print(id)

        res = requests.get("https://www.udebug.com/UVa/" + id)
        tree = html.fromstring(res.content)
        nid = tree.xpath("//input[@name='problem_nid']/@value")
        url = tree.xpath("//a[contains(@class, 'problem-statement')]/@href[1]")[0]

        res = requests.get(url)
        tree = html.fromstring(res.content)
        pdf = 'https://uva.onlinejudge.org/' + tree.xpath('//img[@alt="Download as PDF"]/parent::a/@href')[0]
        os.system(subprocess.list2cmdline(['xdg-open', pdf]))