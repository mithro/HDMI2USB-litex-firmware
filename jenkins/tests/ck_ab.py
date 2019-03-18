#!/usr/bin/python3

import argparse


class ck_ab:

    def pars_args(self):
        parser = argparse.ArgumentParser()

        parser.add_argument("--tty", default="/dev/ttyACM0",
                help='default: %(default)s')

        parser.add_argument("-v", "--verbose", action="store_true" )
        parser.add_argument("--version", action="store_true" )
        parser.add_argument("--debug", action="store_true" )
        args = parser.parse_args()

        self.args = args

        return

    def main(self):

        self.pars_args()

        if self.args.version:
            print(self.version)
            return

        self.test()

