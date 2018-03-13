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
        #self.sensor = getLightSensor(debug=1)
        self.sensor = tsl2591.Tsl2591()
        if (self.sensor is None):
          raise LightSensorException(0); #change return val to the sensors default i2c address

    def getReading(self):
      #lux = self.sensor.lux()
      full, ir = self.sensor.get_full_luminosity()
      lux = self.sensor.calculate_lux(full, ir)
      if lux is not None:
        return lux
      else:
        raise LightSensorException(0)

    def printReading(self, lightFile):
      lux = self.getReading()
      print 'L{' + str(lux) + ',' +  time.strftime("%Y-%m-%d-%H:%M:%S") + '}'
      lightFile.write(str(lux) + "\n")

class Lights():
    __init__(self):
        # arr of lux values at each of 256 levels
        self.calArr = []
        # list of pin numbers in order for GPIOut
        self.pinOut = {18, 19, 20, 21, 22, 23, 24, 25}
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pinOut, GPIO.OUT)

        #array of active light pins
        self.active = []
        # do rest of GPIO setup

    def calibrate(self, sensor):
        for i in range(0, 256):
            lightOn(i)  # run lights at power level i
            lux = sensor.getReading()
            lightOff()
            calArr[i] = lux

    # def runAtLux(self, lux):
    #     i = 0
    #     while calibrateArr[i] < lux:
    #         i+=1
    #     if math.abs(calibrateArr[i] - lux) > math.abs(calibrateArr[i-1] - lux):
    #         i-=1
    #     runLights(i)  # run lights at power level i

    # def runLightsForTime(self, level):
    #     if level > 255 or level < 0:
    #         print("invalid light level")
    #         sys.exit(0)
    #     binLevel = bin(level)  # string of form '0b101010'
    #     binLevel = binLevel[2:]
    #     binList = list(binLevel)
    #     self.active = []
    #     for i in range(0, 7):
    #         if i < binList.length and binList[i] == '1':
    #             self.active.append(pinOut[i])
    #
    #     GPIO.output(active, GPIO.HIGH)
    #     time.sleep(2)
    #     GPIO.output(active, GPIO.LOW)

    def lightOn(self, level):
        if level > 255 or level < 0:
            print("invalid light level")
            sys.exit(0)
            binLevel = bin(level)  # string of form '0b101010'
            binLevel = binLevel[2:]
            binList = list(binLevel)
            active = []
            for i in range(0, 7):
                if i < binList.length and binList[i] == '1':
                    active.append(pinOut[i])

            GPIO.output(active, GPIO.HIGH)

    def lightOff(self):
        GPIO.output(active, GPIO.LOW)

    def main():
        l = Lights()
        ls = LightSensor()
        l.calibrate(ls)


    if __name__ == "__main__":
        main()

# class lightsCSV(Lights):
#     def __init__(self, f):
#         try:
#             Lights.__init__(self)
#             self.f = f #CSV File name String
#             self.levels = []
#         except:
#             print("Unexpected error in Lights init: ", sys.exc_info()[0])
#             sys.exit(0)
#
#     def makeFunc(self):
#
#         mult = 0
#         with open(f, "r") as file:
#             reader = csv.reader(file, delimiter = ' ', quotechar='|')
#             for row in reader:
#                 levels.append(row)
#
#
#
# class lightsTrig(Lights):
#     def __init__(self, daylen, nightlen, maxbright, offset=0):
#         try:
#             Lights.__init__(self)
#             self.dayLen = daylen #day cycle length in seconds
#             self.nightLen = nightlen #night length
#             self.maxBright = maxbright
#             self.interlen = interlen #length of intervals of darkness
#             self.interfreq = interfreq #frequency of intervals
#             self.offset = offset # 1/2 of daylen to start at high noon
#             self.levels = []
#         except:
#             print("Unexpected error in Lights init: ", sys.exc_info()[0])
#             sys.exit(0)
#
#     #make array of light level values for full cycle
#     def makeFunc(self):
#         amp = self.maxBright / 2
#         for x in range(0, self.dayLen - 1):
#             inCos = ((2*math.pi)/self.dayLen)*(x+self.offset)
#             levels.append(int(round(amp * -math.cos(inCos) + amp)))
