#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import sys


'''
This is the client side code for water pump
Board Pin is 11 for water pump circuit

Command Line Parameter:  run time
                         delay time

'''

print("water pump is running")

print(sys.argv[1])
print(sys.argv[2])
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)


GPIO.output(11, GPIO.HIGH)
print("water pump on")
time.sleep(float(sys.argv[1]))
GPIO.output(11, GPIO.LOW)
print("water pump off")
time.sleep(float(sys.argv[2]))
