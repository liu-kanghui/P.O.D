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


    def light_sensor(self):
        ''' Get the lux reading'''
        HOST = self.hostIP
        # Ports are handled in ~/.ssh/config since we use OpenSSH
        CMD = "python /home/pi/NewPod/client/light_client.py -cvs " + self.cvsFile
        process = Popen('ssh {} {}'.format(HOST, CMD),
                        stdout=PIPE, stderr=PIPE, shell=True)
        stdout, stderr = process.communicate()
