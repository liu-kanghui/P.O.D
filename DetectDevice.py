#!/usr/bin/python
# -*- coding: utf-8 -*-

from subprocess import Popen, PIPE
import socket

"""This file finds connected devices' IPV4 address on the same network"""
"""The device name must contains 'Raspberry'"""


def arpScan():
    """Return a list of IPV4 addresses of detected Raspberry devices"""
    pwd = 'raspberry'   # password for sudo
    # -l : localhosts
    # -g : no duplicate
    # wlan: wifi connected
    cmd = 'arp-scan -l --interface=wlan0 -g | grep Raspberry'
    process = Popen('echo {} | sudo -S {}'.format(pwd, cmd),
                    stdout=PIPE, stderr=PIPE, shell=True)
    stdout, stderr = process.communicate()
    output = stdout.decode('ascii').splitlines()
    piZeroHost = list()
    for eachLine in output:
        eachLine = eachLine.split('\t')
        if len(eachLine) == 3:
            host = eachLine[0]
            validateIPV4(host)
            piZeroHost.append(eachLine[0])
    print("connected device IPv4")
    print(piZeroHost)
    return piZeroHost


def validateIPV4(address):
    """Validate the IPV4 address"""
    try:
        socket.inet_aton(address)
    except socket.error:
        print(address + "sorry the addr is not valid ip v4 address")
