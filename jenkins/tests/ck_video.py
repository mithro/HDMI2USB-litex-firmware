#!/usr/bin/python3

import os

from ck_ab import ck_ab

class ck_video(ck_ab):

    def test(self):

        assert os.path.exists(self.args.video), "{} does not exist.".format(self.args.video)
        assert not os.path.isfile(self.args.video), "{} is a regular file.".format(self.args.video)

        return

if __name__=='__main__':
    t = ck_video()
    t.main()

