#!/usr/bin/python3
# -*- coding: utf-8 -*-
from time import sleep
from gpiozero import LEDBoard
from gpiozero.pins.pigpio import PiGPIOFactory
from subprocess import Popen, PIPE


'''
This contains a Lights object, can assign patterns to the lighting

run this script from central computer this module
controls the indiviual light of a pod the light will be on around 100
that is [0,0,1,0,0,1,1,0]  1/4 + 1/8 + 1/64

Parameter: hostIP

'''


class Light():

    def __init__(self, cvsFile, hostIP):
        ''' initialize the hostIP and leds GPIO pins'''
        self.hostIP = hostIP    # host is the one that controls the lights
        self.cvsFile = cvsFile
        self.factory = PiGPIOFactory(host=hostIP)
        # 18, 19, 20, 21, 22, 23, 24, 25 are the connected GPIO pins
        self.leds = LEDBoard(18, 19, 20, 21, 22, 23, 24, 25,
                             pwm=True, pin_factory=self.factory)

    def light_sensor(self):
        ''' Get the lux reading'''
        HOST = self.hostIP
        # Ports are handled in ~/.ssh/config since we use OpenSSH
        CMD = "python /home/pi/NewPod/client/light_sensor_client.py"
        process = Popen('ssh {} {}'.format(HOST, CMD),
                        stdout=PIPE, stderr=PIPE, shell=True)
        stdout, stderr = process.communicate()
        output = stdout.decode('ascii')
        lux_value = int(float(output))
        return lux_value

    def calibrate_light(self):
        ''' Return a dictionary of lux and array value for GPIO Pins'''
        self.leds.on()
        lux_dictionary = dict()
        for led_7 in range(0, 11, 5):
            value_7 = led_7 / 100
            for led_6 in range(0, 11, 5):
                value_6 = led_6 / 10
                for led_5 in range(0, 11, 5):
                    value_5 = led_5 / 10
                    self.leds.value = (1, 1, 1, 1, 1,
                                       value_5, value_6, value_7)
                    sleep(1)  # make sure the light stay up at the range for 1s
                    lux = self.light_sensor()
                    if lux not in lux_dictionary:
                        lux_dictionary[lux] = [1, 1, 1, 1, 1,
                                               value_5, value_6, value_7]
                        print("lux {} ： {}".format(lux, lux_dictionary[lux]))
                    else:
                        print("lux value already exist")
        return lux_dictionary

    def start_running_light(self):
        lux_dictionary = self.calibrate_light()
        for key in sorted(lux_dictionary):
            print("lux {} : array  {}".format(key, lux_dictionary[key]))
        '''
         read throught the self.cvs file for light
         while True:
            read the cvs line
            extract lux and delay
            self.leds.value = lux_dictionary[lux]
            sleep(delay)
        '''
