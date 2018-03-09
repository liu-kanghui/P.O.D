#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''This is the config file for POD contains all the global variables'''

podNames = ['pod-1', 'pod-2']
piMacAddress = ['b8:27:eb:83:9c:8f', 'b8:27:eb:b3:39:cc']

server_host = '192.168.1.100'  # Pi 3 has a static ip address.

podName_mac_dict = {}
for i in range(len(podNames)):
    podName_mac_dict[piMacAddress[i]] = podNames[i]


sqlite_file = 'db.sqlite'