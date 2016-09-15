import os
import logging
from shutil import copyfile

dir = os.path.dirname(os.path.realpath(__file__)) + '/../'

class Init():
    def run(self, args):
        logging.info('initing %s' % args.id)
        logging.debug('creating directory')
        if not os.path.exists(args.id):
            os.makedirs(args.id)

        logging.debug('creating template')
        print(dir)
        copyfile(
                '%s/templates/template.%s' % (dir, args.template),
                '%s/%s.%s' % (args.id, args.id, args.template))