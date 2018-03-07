#!/usr/bin/python
# -*- coding: utf-8 -*-

from subprocess import Popen, PIPE
import socket
import config


"""This file finds connected devices' IPV4 address on the same network"""
"""The device name must contains 'Raspberry'"""


def arpScan():
    """Return a list of IPV4 addresses of detected Raspberry devices"""
    pwd = 'raspberry'   # password for sudo
    # -l : localhosts
    # -g : no duplicate
    # wlan: wifi connected
    cmd = 'arp-scan -l --interface=wlan0 -g'  # scan all the connected network
    process = Popen('echo {} | sudo -S {}'.format(pwd, cmd),
                    stdout=PIPE, stderr=PIPE, shell=True)
    stdout, stderr = process.communicate()
    output = stdout.decode('ascii').splitlines()
    piZeroHost = {}
    for eachLine in output:
        eachLine = eachLine.split('\t')
        if len(eachLine) >= 2:
            macAddress = eachLine[1]   # grab the mac address
            host = eachLine[0]         # grab the host
            if macAddress in config.piMacAddress:
                validateIPV4(host)     # maybe don't need to validate
                print(macAddress)
                piZeroHost[config.podName_mac_dict.get(macAddress)] = host
    print("podname  and its host")
    print(piZeroHost)
    return piZeroHost


def validateIPV4(address):
    """Validate the IPV4 address"""
    try:
        socket.inet_aton(address)
    except socket.error:
        print(address + "sorry the addr is not valid ip v4 address")
