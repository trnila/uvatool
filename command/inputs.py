import logging

import api
import utils


class Inputs:
    def run(self, args):
        id = utils.get_problem_from_cwd()

        req = api.Request()

        ids = req.getInfo(id)['input_ids']
        logging.info("Found %d example inputs", len(ids))

        for i, input_id in enumerate(ids):
            logging.info("Getting input %s", input_id)

            input = req.getInput(input_id)
            f = open(str(i) + ".in", "w")
            f.write(input)
            f.close()

            logging.info("Getting output %s", input_id)
            out = req.getOutput(id, input)

            f = open(str(i) + ".out", "w")
            f.write(out)
            f.close()
