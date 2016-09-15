import os
import logging
import api


class Generate():
    def run(self, args):
        base = os.path.splitext(args.input)[0]
        with open(args.input) as input, open(base + '.out', 'w') as output:
            output.write(api.getOutput("100", input.read()))
            logging.info("output written to " + output.name)

