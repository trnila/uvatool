import difflib
import filecmp
import glob
import os
import logging
import subprocess

import api
import utils


class Test():
    def run(self, args):
        id = utils.get_problem_from_cwd()

        os.system(subprocess.list2cmdline(['make', id]))

        for file in glob.glob("*.in"):
            ok = True

            with open("/tmp/out", "w") as programOut:
                with open(file) as input:
                    proc = subprocess.Popen(['./' + id], stdin=input, stdout=programOut)
                    proc.communicate()

            expectPath = os.path.splitext(file)[0] + '.out'

            proc = subprocess.Popen(["diff", "-w", "-y", "/tmp/out", expectPath], stdout=subprocess.PIPE)
            out = proc.communicate()[0]
            if proc.returncode == 0:
                logging.info("test %s is ok" % file)
            else:
                print(out.decode('utf-8'))
                logging.error("test %s is failing" % file)
                exit(1)
