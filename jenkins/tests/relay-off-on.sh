#!/bin/bash -x

relay_dev=/dev/ttyACM0

printf "relay on 0\r" | cstream -t 60 -b 1 |tee ${relay_dev}
sleep 3
printf "relay off 0\r" | cstream -t 60 -b 1 |tee ${relay_dev}

