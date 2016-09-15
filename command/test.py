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

            with open(file) as input:
                proc = subprocess.Popen(['./' + id], stdin=input, stdout=subprocess.PIPE)
                lines2 = proc.communicate()[0].decode('utf-8').splitlines()

            expectPath = os.path.splitext(file)[0] + '.out'
            with open(expectPath) as expect:
                for line in difflib.unified_diff(lines2, expect.read().splitlines(), fromfile='file1', tofile='file2', lineterm=''):
                    print(line)
                    ok = False

            if ok:
                logging.info("test %s is ok" % file)
            else:
                logging.error("test %s is failing" % file)