import os
import logging
from api import Request
import utils


class Generate:
    def run(self, args):
        id = utils.get_problem_from_cwd()
        request = Request()
        base = os.path.splitext(args.input)[0]
        with open(args.input) as input, open(base + '.out', 'w') as output:
            output.write(request.getOutput(id, input.read()))
            logging.info("output written to " + output.name)
