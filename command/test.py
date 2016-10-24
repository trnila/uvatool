import glob
import os
import logging
import subprocess
import utils


class Test:
    def run(self, args):
        id = utils.get_problem_from_cwd()

        os.system(subprocess.list2cmdline(['make', str(id)]))

        inputs = args.input if args.input is not None else glob.glob("*.in")
        for file in inputs:
            with open("/tmp/out", "w") as programOut:
                with open(file) as input:
                    proc = subprocess.Popen(['./' + str(id)], stdin=input, stdout=programOut)
                    proc.communicate()

            expectPath = os.path.splitext(file)[0] + '.out'

            proc = subprocess.Popen(["diff", "-y", "/tmp/out", expectPath], stdout=subprocess.PIPE)
            out = proc.communicate()[0]
            if proc.returncode == 0:
                logging.info("test %s is ok" % file)
            else:
                print(out.decode('utf-8'))
                logging.error("test %s is failing" % file)
                exit(1)
