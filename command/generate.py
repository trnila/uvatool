import os
import logging
import api
import utils


class Generate():
    def run(self, args):
        id = utils.get_problem_from_cwd()
        base = os.path.splitext(args.input)[0]
        with open(args.input) as input, open(base + '.out', 'w') as output:
            output.write(api.getOutput(id, input.read()))
            logging.info("output written to " + output.name)

