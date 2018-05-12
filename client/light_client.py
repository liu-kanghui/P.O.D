#!/usr/bin/python
# -*- coding: utf-8 -*-
from gpiozero import LEDBoard
import tsl2591
from time import sleep


def floatToBinary(n):
        val_arr = [128.0,64.0,32.0,16.0,8.0,4.0,2.0,1.0]
        ans_arr = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        rem = n
        ans_arr[7] = rem % 1.0 #gets decimal
        rem = rem - ans_arr[7]#get rid of decimal

        for i in range(7):
            if rem > val_arr[i]:
                ans_arr[i] = 1.0
                rem -= val_arr[i]
            elif rem != 0.0:
                ans_arr[i] = rem/float(val_arr[i])
                rem = 0.0
        return ans_arr[::-1]

class Light():

    def __init__(self):
        ''' initialize the hostIP and leds GPIO pins'''

        # 18, 19, 20, 21, 22, 23, 24, 25 are the connected GPIO pins

        self.leds = LEDBoard(18,19,20,21,22,23,24,25, pwm=True)
        self.sensor = tsl2591.Tsl2591()

    


    def calibrate_light(self):
        ''' Return a dictionary of lux and array value for GPIO Pins'''

        self.leds.on()
        lux_dictionary = dict()
        start_level = 150.0
        end_level = 250.0
        interval = 0.1
        for i in range(int(start_level*10), int(end_level*10), int(interval*10)):
            self.leds.value = tuple(floatToBinary(float(i)/10.0))
            print(floatToBinary(float(i)/10.0))
        
            sleep(.5)
            (full, ir) = self.sensor.get_full_luminosity()
            lux = self.sensor.calculate_lux(full, ir)
            if lux not in lux_dictionary:
                lux_dictionary[lux] = floatToBinary(float(i)/10.0)
                print 'lux {} \xef\xbc\x9a {}'.format(lux,
                        lux_dictionary[lux])
            else:
                print 'lux value already exist'

        return lux_dictionary

    def run_test(self):
        start_level = 200.0
        end_level = 250.0
        interval = 0.5
        for i in range(int(start_level*10), int(end_level*10), int(interval*10)):
            print(floatToBinary(float(i)/10.0))
            self.leds.value = tuple(floatToBinary(float(i)/10.0))
            sleep(5)


        
L = Light()
L.calibrate_light()
#L.run_test()