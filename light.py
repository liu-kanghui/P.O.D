#!/usr/bin/python3
# -*- coding: utf-8 -*-
from time import sleep
from gpiozero import LEDBoard
from gpiozero.pins.pigpio import PiGPIOFactory
import sys


# run this script from central computer
# this module controls the indiviual light of a pod

class Lights():

    def __init__(self):
        # host is the one that control the light
        factory = PiGPIOFactory(host='192.168.90.58')
        self.leds = LEDBoard(18, 19, 20, 21, 22, 23, 24, 25,
                             pwm=True, pin_factory=factory)

    # adjust LED intensity according to brightness assigned
    def adjustableLED(self, brightness):
        leds = self.processBrightness(brightness)
        self.leds.value = (leds[0], leds[1], leds[2], leds[3],
                           leds[4], leds[5], leds[6], leds[7])

    # turn LEDS light on for onTime and off for offTime forever
    def hardOnOffLED(self, onTime, offTime, brightness):
        while True:
            leds = self.processBrightness(brightness)
            self.leds.value = (leds[0], leds[1], leds[2], leds[3],
                               leds[4], leds[5], leds[6], leds[7])
            sleep(onTime)
            self.leds.off()
            sleep(offTime)

    # Return leds on and off value as a list
    def processBrightness(self, brightness):
        if brightness > 255 or brightness < 0:
            print("invalid light brightness level")
            sys.exit(0)
        leds = [0, 0, 0, 0, 0, 0, 0, 0]
        binLevel = bin(brightness)  # string of form '0b101010'
        binLevel = binLevel[2:]
        binList = list(binLevel)
        binList.reverse()
        for i in range(0, len(binList)):
            if binList[i] == '1':
                leds[i] = 1
        print("active led")
        print(leds)
        return leds


LED = Lights()
for i in range(100, 255):
    LED.adjustableLED(i)
# LED.hardOnOff(1, 2, 240)


