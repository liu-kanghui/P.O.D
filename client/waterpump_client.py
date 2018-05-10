#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import sys

parser = argparse.ArgumentParser()
parser.add_argument("-start", type=int, required=True, help="experiment start time")
parser.add_argument("-duration", type=int, required=True, help="experiment duration")
parser.add_argument("-nwater", type=int, required=True, help="pictures per day")
parser.add_argument("-waterdur", type=int, required=True, help="duration of water")

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

exp_start = args.start
exp_dur = args.duration
water_num = args.nwater
water_dur = sys.water_dur
water_delay = (60*60*24)/water_num

while time.time() < exp_start:
    time.sleep(1)

cur_time = time.time() - exp_start
while cur_time < exp_dur
    if cur_time % water_delay == 0:
        GPIO.output(11, GPIO.HIGH)
        time.sleep(water_dur)
        GPIO.output(11, GPIO.LOW)

    cur_time = time.time() - exp_start
