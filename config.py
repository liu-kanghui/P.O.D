#!/usr/bin/python3
# -*- coding: utf-8 -*-

from subprocess import Popen, PIPE
import socket

'''This is the config file for POD contains all the global variables'''

podNames = ['pod-1', 'pod-2']
piMacAddress = ['b8:27:eb:83:9c:8f', 'b8:27:eb:b3:39:cc']
aviable_pod = podNames

server_host = '192.168.1.100'  # Pi 3 has a static ip address.

podName_mac_dict = {}
for i in range(len(podNames)):
    podName_mac_dict[piMacAddress[i]] = podNames[i]

def arp_scan():
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
                validate_IPV4(host)     # maybe don't need to validate
                print(macAddress)
                piZeroHost[config.podName_mac_dict.get(macAddress)] = host
    print("podname  and its host")
    print(piZeroHost)
    return piZeroHost


def validate_IPV4(address):
    """Validate the IPV4 address"""
    try:
        socket.inet_aton(address)
    except socket.error:
        print(address + "sorry the addr is not valid ip v4 address")



podName_ip_dic = arp_scan()
aviable_pos = podName_ip_dic
