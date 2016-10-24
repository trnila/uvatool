import os
import logging
import utils
from api import uva

class Stats:
    def _pad(self, str, size):
        return str.ljust(size)[:size]

    def _status(self, problem):
        if problem.is_accepted():
            return utils.color_green(problem.verdict.upper())

        return utils.color_red(problem.verdict.upper())

    def _print(self, problem):
        print(self._pad("#%d %s" % (problem.problem_id, problem.name), 50), end=' | ')

        print(self._pad(self._status(problem), 30), end=' | ')
        print(utils.pretty_date(problem.submitted))

    def run(self, args):
        api = uva.Uva()
        problems = api.stats()

        if len(problems):
            print("Your last solution: %s (%s) " % (self._status(problems[0]), utils.pretty_date(problems[0].submitted)))

        for problem in problems:
            self._print(problem)



