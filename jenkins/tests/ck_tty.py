#!/usr/bin/python3

import argparse
# import serial
import os
import time

from pprint import pprint

class Tty_talker():

    def __init__(self, tty):
        with serial.Serial(tty, 115200, timeout=1) as ser:
            # um.. how's this gonna work?
            pass

def tx(ser, string):

    # send command
    print("tx: ", end='')

    for c in string:
        print(c.__repr__(), end='')
        r = ser.write(c.encode())
        time.sleep(.3)
    print()

    return

def rx(ser):

    # read result
    line_no=0
    lines=[]
    while True:
        line = ser.readline()

        line_no += 1
        print( "rx: {n} {leng} {line}".format(
            n=line_no,
            leng = len(line),
            line =line.__repr__()))

        if len(line)==0:
            break

        line = line.decode().strip()
        lines.append(line)

    return lines


def ck_prompt(tty):

    with serial.Serial(tty, 115200, timeout=1) as ser:

        tx(ser, '\r\n')
        lines = rx(ser)

        assert len(lines) == 1, "Unexpected prompt:{}".format(lines)
        assert lines[0].startswith('HDMI2USB'), "Unexpected prompt:{}".format(lines)

    return

def test(args):

    assert os.path.exists(args.tty), "{} does not exist.".format(args.tty)
    assert not os.path.isfile(args.tty), "{} is a regular file.".format(args.tty)

    return

def pars_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("--tty", default="/dev/ttyACM0",
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

