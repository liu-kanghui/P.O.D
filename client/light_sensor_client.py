#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tsl2591
import sys


# intended for use with an Adafruit TSL2561 breakout board
class LightSensor():
    def __init__(self):
        # self.sensor = getLightSensor(debug=1)
        self.sensor = tsl2591.Tsl2591()
    def getReading(self):
        # lux = self.sensor.lux()
        full, ir = self.sensor.get_full_luminosity()
        lux = self.sensor.calculate_lux(full, ir)
        sys.stdout.write(str(lux))


sensor = LightSensor()
sensor.getReading()