#!/usr/bin/env python
import argparse
import logging
import command

logging.basicConfig(level=logging.INFO)

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
sub = subparsers.add_parser('init')
sub.add_argument('id', help='id of uva problem')
sub.add_argument('-t', '--template', help='template', default='c')

subparsers.add_parser('read')
subparsers.add_parser('inputs')

sub = subparsers.add_parser('test')
sub.add_argument('-i', '--input', action='append')

sub = subparsers.add_parser('generate')
sub.add_argument('input', help='input file')

args = parser.parse_args()

cmd = getattr(command, args.action[0].upper() + args.action[1:])()
cmd.run(args)
