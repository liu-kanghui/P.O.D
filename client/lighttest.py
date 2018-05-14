#!/usr/bin/python
# -*- coding: utf-8 -*-
from gpiozero import LEDBoard
import tsl2591
from time import sleep

val_arr = [128.0,64.0,32.0,16.0,8.0,4.0,2.0,1.0]

def floatToBinary(n):
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
	return ans_arr


print(floatToBinary(235.5))

