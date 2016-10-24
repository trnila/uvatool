import os
import logging

import time

import utils
from api import uva

dir = os.path.dirname(os.path.realpath(__file__)) + '/../'

class Submit:
    def run(self, args):
        id = utils.get_problem_from_cwd()
        source_code = utils.find_source_code()

        api = uva.Uva()
        submit_id = api.submit(id, source_code)
        print(submit_id)

        problems = None
        while True:
            problems = api.stats()
            if problems and problems[0].submit_id == submit_id and problems[0].verdict != 'In judge queue':
                print()
                break

            print('.', end='')

            time.sleep(2)

        if problems[0].is_accepted():
            print(utils.color_green("ACCEPTED %fs" % problems[0].runtime))
        else:
            print(utils.color_red(problems[0].verdict))