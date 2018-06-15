#Quinn Murphy, Kanghui Liu, Jesse Kline, Emily Wright
#Plant Observation Device
#Water Pump Loop (client)


#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-start", type=float, required=True, help="experiment start time")
parser.add_argument("-duration", type=int, required=True, help="experiment duration")
parser.add_argument("-waterdel", type=int, required=True, help="waters delay")
parser.add_argument("-waterdur", type=int, required=True, help="duration of water")

args = parser.parse_args()

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

exp_start = args.start
exp_dur = args.duration
water_delay = args.waterdel
water_dur = args.waterdur

print("water args: ",args)
#water_delay = (60*60*24)/water_num

#wait for experiment to start

while time.time() < exp_start:
    time.sleep(1)

cur_time = time.time() - exp_start
while int(cur_time) < exp_dur:
    if int(cur_time) % water_delay == 0:
        GPIO.output(11, GPIO.HIGH)
        time.sleep(water_dur)
        GPIO.output(11, GPIO.LOW)

    cur_time = time.time() - exp_start

GPIO.cleanup()