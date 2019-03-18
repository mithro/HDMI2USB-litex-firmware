#!/usr/bin/python3

import requests
import serial

# from pprint import pprint
from ck_tty import ck_tty


class ck_version(ck_tty):

    def git_rev(self):

        # print("import sys;sys.exit()"); import code; code.interact(local=locals())

        # import pdb; pdb.set_trace()

        url = "https://{host}/{base}/{platform}/{target}/{cpu}/channels.txt".format(**self.args.__dict__) ## save me f-strings

        if self.args.verbose:
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

        rev = channels[self.args.channel]['rev']

        return rev

    def board_rev(self):

        with serial.Serial(self.args.tty, 115200, timeout=1) as self.ser:

            # send command
            self.tx('\n\nversion\r\n')
            lines = self.rx()
            for line in lines:
                if "describe" in line:
                    rev = line.split(':')[1].strip()

        return rev

    """

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

    """

    def more_args(self, parser):

        parser.add_argument("--host", default="code.timvideos.us" ,
                help='default: %(default)s')
        parser.add_argument("--base", default="HDMI2USB-firmware-prebuilt",
                help='default: %(default)s')
        parser.add_argument("--platform", default="opsis",
                help='default: %(default)s')
        parser.add_argument("--target", default="hdmi2usb",
                help='default: %(default)s')
        parser.add_argument("--cpu", default="lm32",
                help='default: %(default)s')

        parser.add_argument("--channel", default="unstable",
                help='default: %(default)s')

        return


    def test(self):

        gr = self.git_rev()
        br = self.board_rev()
        assert gr==br

        if self.args.verbose:
            print("{gr} == {br}".format( gr=gr, br=br))
            print("expected version test passed.")

        return


if __name__=='__main__':
    t = ck_version()
    t.main()

