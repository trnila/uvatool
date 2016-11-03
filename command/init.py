import os
import logging
from shutil import copyfile

dir = os.path.dirname(os.path.realpath(__file__)) + '/../'


class Init:
    def run(self, args):
        if not os.path.exists(args.id):
            os.makedirs(args.id)

        template = '%s/templates/template.%s' % (dir, args.language)

        try:
            copyfile(template, '%s/%s.%s' % (args.id, args.id, args.language))
        except IOError as e:
            print(e)

