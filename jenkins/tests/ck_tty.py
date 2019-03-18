#!/usr/bin/python3

import argparse
import serial
import os
import time

from ck_ab import ck_ab


class Tty_talker():

    def __init__(self, tty):
        with serial.Serial(tty, 115200, timeout=1) as ser:
            # um.. how's this gonna work?
            pass


class ck_tty(ck_ab):

    version = 0.7
    ser = None

    def tx(self, string):

        # send command
        if self.args.verbose: print("tx: ", end='')

        for c in string:
            if self.args.verbose: print(c.__repr__(), end='')
            r = self.ser.write(c.encode())
            time.sleep(.3)

        if self.args.version: print()

        return

    def rx(self):

        # read result
        line_no=0
        lines=[]
        while True:
            line = self.ser.readline()

            line_no += 1
            if self.args.verbose:
                print( "rx: {n} {leng} {line}".format(
                    n=line_no,
                    leng = len(line),
                    line =line.__repr__()))

            if len(line)==0:
                break

            line = line.decode().strip()
            lines.append(line)

        return lines


    def ck_prompt(self):

        with serial.Serial(self.args.tty, 115200, timeout=1) as self.ser:

            self.tx('\r\n')
            lines = self.rx()

            assert len(lines) == 2, "Unexpected prompt:{}".format(lines)
            if self.args.verbose: print( "len(lines) == 1: {}".format(lines))
            assert lines[1].startswith('H2U'), "Unexpected prompt:{}".format(lines)
            if self.args.verbose: print( "lines[1].startswith('H2U') {}".format(lines[1]))

        return


    def ck_port(self):

        assert os.path.exists(self.args.tty), "{} does not exist.".format(
                self.args.tty)
        if self.args.verbose: print( "{} does exist.".format(self.args.tty) )

        assert not os.path.isfile(self.args.tty), "{} is a regular file.".format(self.args.tty)
        if self.args.verbose: print( "{} is not a regular file. (good)".format(self.args.tty) )

        return


    def test(self):
        self.ck_port()
        self.ck_prompt()
        return

if __name__=='__main__':
    t = ck_tty()
    t.main()

