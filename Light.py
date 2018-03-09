#!/usr/bin/python3
# -*- coding: utf-8 -*-
from time import sleep
from gpiozero import LEDBoard
from gpiozero.pins.pigpio import PiGPIOFactory
import sys
from bisect import bisect_left, bisect_right
import tsl2591


'''
This contains a Lights object, can assign patterns to the lighting

run this script from central computer this module
controls the indiviual light of a pod the light will be on around 100
that is [0,0,1,0,0,1,1,0]  1/4 + 1/8 + 1/64

Parameter: hostIP

'''


class Lights():
    #add csv file as parameter
    def __init__(self, hostIP):
        ''' initialize the hostIP and leds GPIO pins'''
        #self.lightVals, self.lightDelay = Read_Two_Column_File(file)
        self.sensor = tsl2591.Tsl2591()
        if (self.sensor is None):
          raise LightSensorException(0);
        self.hostIP = hostIP    # host is the one that controls the lights
        self.factory = PiGPIOFactory(host=hostIP)
        # 18, 19, 20, 21, 22, 23, 24, 25 are the connected GPIO pins
        self.leds = LEDBoard(18, 19, 20, 21, 22, 23, 24, 25,
                             pwm=True, pin_factory=self.factory)
        #array for lux values at given power level (index)
        self.calibrateArr = []
        calibrate();
    def adjustableLED(self, brightness):
        ''' adjust LED intensity according to brightness assigned'''
        leds = self.processBrightness(brightness)
        self.leds.value = (leds[0], leds[1], leds[2], leds[3],
                           leds[4], leds[5], leds[6], leds[7])

    def hardOnOffLED(self, onTime, offTime, brightness):
        ''' turn LEDS light on for onTime and off for offTime,
            with assigned brightness'''
        while True:
            leds = self.processBrightness(brightness)
            self.leds.value = (leds[0], leds[1], leds[2], leds[3],
                               leds[4], leds[5], leds[6], leds[7])
            sleep(onTime)
            self.leds.off()
            sleep(offTime)

    def processBrightness(self, brightness):
        ''' Return leds switch value as a list
            1 for on, 0 for off '''
        if brightness > 255 or brightness < 0:
            print("invalid light brightness level")
            sys.exit(0)
        leds = [0, 0, 0, 0, 0, 0, 0, 0]     # initially turn everything off
        binLevel = bin(brightness)          # string of form '0b101010'
        binLevel = binLevel[2:]
        binList = list(binLevel)
        binList.reverse()   # because the pins are in reversed order
        for i in range(0, len(binList)):
            if binList[i] == '1':
                leds[i] = 1
        print("active led")
        print(leds)
        return leds

    #make array mapping power levels to lux vals
    def calibrate(self):
        calibrateArr = []
        for i in range(0,255):
            #run these statements as threads?
            try:
                thread.start_new_thread( hardOnOffLED, (2, 0, i))
                sleep(1)
                lux = thread.start_new_thread( getReading, ())
                sleep(1)
                calibrateArr.append(lux)
            except:
                print "Error: unable to start thread


    #run at given lux value determined by array
    def runAtLux(self, onTime, offTime, lux):
        try:
            #find position in array of lux
            i=bisect_left(calibrateArr, lux)
            #turn on light at lux
            hardOnOffLED(onTime, offTime, i)
        except:
            print "Lights not calibrated:", sys.exc_info()[0]
            sys.exit(0)

    def getReading(self):
      #lux = self.sensor.lux()
      full, ir = self.sensor.get_full_luminosity()
      lux = self.sensor.calculate_lux(full, ir)
      if lux is not None:
        return lux
      else:
        raise LightSensorException(0)

def Read_Two_Column_File(file_name):
    with open(file_name, 'r') as data:
        x = []
        y = []
        for line in data:
            p = line.split()
            x.append(float(p[0]))
            y.append(float(p[1]))

    return x, y
