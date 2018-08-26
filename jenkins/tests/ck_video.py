#!/usr/bin/python3

import argparse
# import serial
import os
import time

from pprint import pprint

def test(args):

    assert os.path.exists(args.video), "{} does not exist.".format(args.video)
    assert not os.path.isfile(args.video), "{} is a regular file.".format(args.video)

    return

def pars_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("--video", default="/dev/video0",
            help='default: %(default)s')

    parser.add_argument("-v --verbose", action="store_true" )
    parser.add_argument("--version", action="store_true" )
    parser.add_argument("--debug", action="store_true" )
    args = parser.parse_args()

    return args


def main():

    args=pars_args()
    test(args)


if __name__=='__main__':
    main()

