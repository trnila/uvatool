import os
import logging
import subprocess
from shutil import copyfile

import requests
from lxml import html


class Inputs():
    def run(self, args):
        id = os.path.basename(os.getcwd())

        res = requests.get("https://www.udebug.com/UVa/" + id)
        tree = html.fromstring(res.content)
        nid = tree.xpath("//input[@name='problem_nid']/@value")
        url = tree.xpath("//a[contains(@class, 'problem-statement')]/@href[1]")


        ids = sorted(set(tree.xpath("//*[@data-id]/@data-id")))
        logging.info("Found %d example inputs", len(ids))

        for i, id in enumerate(ids):
            logging.info("Getting input %s", id)
            res = requests.post("https://www.udebug.com/get-selected-input", {'nid': id})
            input = res.json()['input_value']
            f = open(str(i) + ".in", "w")
            f.write(input)
            f.close()

            logging.info("Getting output %s", id)
            data = {
                'problem_nid': nid,
                'input_data': input,
                'node_nid': '',
                'op': 'Get Accepted Output',
                'user_output': '',
                'form_id': 'udebug_custom_problem_view_input_output_form'
            }
            res = requests.post('https://www.udebug.com/UVa/100', data)
            tree = html.fromstring(res.content)

            out = tree.xpath("//textarea[@id='edit-output-data']/text()")[0]

            f = open(str(i) + ".out", "w")
            f.write(out)
            f.close()
