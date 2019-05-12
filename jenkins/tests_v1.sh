cd /home/pi/HDMI2USB-litex-firmware/jenkins/tests

venv/bin/python ck_tty.py --tty /dev/ttyACM1
venv/bin/python ck_video.py --tty /dev/video0
venv/bin/python ck_version.py --tty /dev/ttyACM1
venv/bin/python ck_jpg.py --tty /dev/video0

diff \
  <(v4l2-compliance --device /dev/video0) \
  ../datas/v4l2-compliance.txt

diff <(v4l2-ctl --all) ../datas/v4l2-ctl.txt

