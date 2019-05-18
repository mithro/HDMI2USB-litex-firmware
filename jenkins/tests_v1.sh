#!/bin/bash -ex

cd /home/pi/HDMI2USB-litex-firmware/jenkins/tests

venv/bin/python ck_tty.py --tty /dev/hdmi2usb/by-num/all0/tty
venv/bin/python ck_video.py
venv/bin/python ck_version.py --tty /dev/hdmi2usb/by-num/all0/tty
venv/bin/python ck_jpg.py

diff \
    <(v4l2-compliance --device /dev/hdmi2usb/by-num/all0/video) \
    ../datas/v4l2-compliance.txt

diff <(v4l2-ctl --all) ../datas/v4l2-ctl.txt
