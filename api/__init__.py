import requests
from lxml import html


def getInfo(id):
    res = requests.get("https://www.udebug.com/UVa/" + id)
    tree = html.fromstring(res.content)

    return {
        'nid': tree.xpath("//input[@name='problem_nid']/@value"),
        'url': tree.xpath("//a[contains(@class, 'problem-statement')]/@href[1]")
    }

def getOutput(id, input):
       info = getInfo(id)

       data = {
            'problem_nid': info['nid'],
            'input_data': input,
            'node_nid': '',
            'op': 'Get Accepted Output',
            'user_output': '',
            'form_id': 'udebug_custom_problem_view_input_output_form'
        }
       res = requests.post('https://www.udebug.com/UVa/' + id, data)
       tree = html.fromstring(res.content)

       return tree.xpath("//textarea[@id='edit-output-data']/text()")[0]
