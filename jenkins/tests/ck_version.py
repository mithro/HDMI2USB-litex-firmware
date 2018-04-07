#!/usr/bin/python3

import argparse
# import urllib.request
import requests
import serial
import time


from pprint import pprint


def git_rev(
        host='code.timvideos.us',
        base='HDMI2USB-firmware-prebuilt',
        platform='opsis',
        target='hdmi2usb',
        cpu='lm32',
        channel="unstable",
        ):

    url = "https://{host}/{base}/{platform}/{target}/{cpu}/channels.txt".format(**locals()) ## save me f-strings

    print(url)
    # data = urllib.request.urlopen(url)
    response = requests.get(url)
    channels = {}
    for line in response.text.split('\n'):
        if line:
            tds = line.split()
            channels[tds[0]] = {
                    'rev': tds[1],
                    'path': tds[2],
                    }

    rev = channels[channel]['rev']

    return rev

def board_rev(tty):

    with serial.Serial(tty, 115200, timeout=1) as ser:

        # send command
        for c in '\n\nversion\r\n':
            print("tx: {}".format(c.__repr__()))
            r = ser.write(c.encode())
            time.sleep(.3)

        # read and parse result
        line_no=0
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

            if "describe" in line:
                rev = line.split(':')[1].strip()

    return rev


def pars_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("--tty" )

    parser.add_argument("-v --verbose", action="store_true" )
    parser.add_argument("--version", action="store_true" )
    parser.add_argument("--debug", action="store_true" )
    parser.add_argument("--test", action="store_true" )
    args = parser.parse_args()

    return args

def test(args):

    gr = git_rev()
    br = board_rev(args.tty)
    assert gr==br
    print("{gr} == {br}".format( gr=gr, br=br))
    print("expected version test passed.")

    return


def main():

    args=pars_args()

    if args.test:
        test(args)


if __name__=='__main__':
    main()

