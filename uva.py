#!/usr/bin/env python
import argparse
import logging
import command

logging.basicConfig(level=logging.DEBUG)

try:
    from colorlog import ColoredFormatter
    logging.getLogger().handlers[0].setFormatter(ColoredFormatter())
except:
    pass

try:
    import requests_cache
    requests_cache.install_cache('/tmp/uva.cache', allowable_methods=('GET', 'POST'))
except:
    pass

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(help='sub-command help', dest="action")
parser_a = subparsers.add_parser('init')
parser_a.add_argument('id', help='id of uva problem')
parser_a.add_argument('-t', '--template', help='template', default='c')

parser_b = subparsers.add_parser('read')

parser_b = subparsers.add_parser('inputs')
parser_b = subparsers.add_parser('test')
parser_b.add_argument('-i', '--input', action='append')

parser_b = subparsers.add_parser('generate')
parser_b.add_argument('input', help='input file')

# parse some argument lists
args = parser.parse_args()

cmd = getattr(command, args.action[0].upper() + args.action[1:])()
cmd.run(args)
