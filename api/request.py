import requests
from lxml import html
from settings import UDEBUG_WWW
import requests, requests.utils, pickle

class Request():
    def getInfo(self, id):
        res = requests.get("%s/UVa/%d" % (UDEBUG_WWW, id))
        tree = html.fromstring(res.content)

        return {
            'nid': tree.xpath("//input[@name='problem_nid']/@value"),
            'url': tree.xpath("//a[contains(@class, 'problem-statement')]/@href[1]"),
            'input_ids': sorted(set(tree.xpath("//*[@data-id]/@data-id")))
        }

    def getOutput(self, id, input):
        info = self.getInfo(id)

        data = {
            'problem_nid': info['nid'],
            'input_data': input,
            'node_nid': '',
            'op': 'Get Accepted Output',
            'user_output': '',
            'form_id': 'udebug_custom_problem_view_input_output_form'
        }
        res = requests.post("%s/UVa/%d" % (UDEBUG_WWW, id), data)
        tree = html.fromstring(res.content)

        return tree.xpath("//textarea[@id='edit-output-data']/text()")[0]

    def getInput(self, id):
        res = requests.post(UDEBUG_WWW +"/get-selected-input", {'nid': id})
        return res.json()['input_value']
