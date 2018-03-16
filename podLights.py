import os
import sys
import time
import datetime as datetime
import requests
import threading

import RPi.GPIO as GPIO  # from pi zero light driver code


import tsl2591
import Adafruit_MCP9808.MCP9808 as tempLib
import math


# intended for use with an Adafruit TSL2561 breakout board
class LightSensor():
    def __init__(self):
        # self.sensor = getLightSensor(debug=1)
        self.sensor = tsl2591.Tsl2591()

    def getReading(self):
        # lux = self.sensor.lux()
        full, ir = self.sensor.get_full_luminosity()
        lux = self.sensor.calculate_lux(full, ir)
        if lux is not None:
            return lux

    def printReading(self, lightFile):
        lux = self.getReading()
        lightFile.write(str(lux) + "\n")


class Lights():

    def __init__(self):
        # arr of lux values at each of 256 levels
        self.calArr = []
        # list of pin numbers in order for GPIOut
        self.pinOut = [18, 19, 20, 21, 22, 23, 24, 25]
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pinOut, GPIO.OUT)
        self.active = []
        GPIO.output(self.pinOut, GPIO.LOW)
        # do rest of GPIO setup

    def calibrate(self, sensor):
        for i in range(113, 155):
            self.lightOn(i)  # run lights at power level i
            print(i)
            time.sleep(1)
            lux = sensor.getReading()
            print(lux)
            self.calArr.append(lux)
            self.lightOff()
        print(self.calArr)

    def lightOn(self, level):
        if level > 255 or level < 0:
            print("invalid light level")
            sys.exit(0)
        binLevel = bin(level)  # string of form '0b101010'
        binLevel = binLevel[2:]
        binList = list(binLevel)
        binList.reverse()
        active = []
        for i in range(0, 8):
            if i < len(binList) and binList[i] == '1':
                self.active.append(self.pinOut[i])

        GPIO.output(self.active, GPIO.HIGH)
        print(binList)

    def lightOff(self):
        GPIO.output(self.active, GPIO.LOW)


light = Lights()

light.lightOff()

ls = LightSensor()
# light.calibrate(ls)

for i in range(103, 155):
    light.lightOff()
    light.lightOn(i)
    time.sleep(1)

GPIO.cleanup()
