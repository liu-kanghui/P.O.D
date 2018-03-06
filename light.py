#!/usr/bin/python3
# -*- coding: utf-8 -*-
from time import sleep
from gpiozero import LEDBoard
from gpiozero.pins.pigpio import PiGPIOFactory
import sys

'''
This contains a Lights object, can assign patterns to the lighting

run this script from central computer this module
controls the indiviual light of a pod the light will be on around 100
that is [0,0,1,0,0,1,1,0]  1/4 + 1/8 + 1/64

Parameter: hostIP

'''


class Lights():

    def __init__(self, hostIP):
        ''' initialize the hostIP and leds GPIO pins'''
        self.hostIP = hostIP    # host is the one that controls the lights
        self.factory = PiGPIOFactory(host=hostIP)
        # 18, 19, 20, 21, 22, 23, 24, 25 are the connected GPIO pins
        self.leds = LEDBoard(18, 19, 20, 21, 22, 23, 24, 25,
                             pwm=True, pin_factory=self.factory)

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


