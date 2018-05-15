import numpy as np
import pandas as pd
import time
import sys
import argparse
from subprocess import Popen, PIPE
from Light import Light

parser = argparse.ArgumentParser()
parser.add_argument("-csv", type=str, required=True, help="csv filename")
parser.add_argument("-start", type=float, required=True, help="experiment start time")
parser.add_argument("-duration", type=int, required=True, help="experiment duration")
args = parser.parse_args()

csv_path = args.csv
exp_start = args.start
exp_dur = args.duration


#parse csv
csvData = pd.read_csv(csv_path)
dataMatrix = csvData.as_matrix()
luxval, luxdur = np.split(dataMatrix, 2, axis = 1)
luxval = luxval.reshape(luxval.shape[0])

#sum durations to get start time for each value
luxtimes = np.subtract(np.cumsum(luxdur.reshape(luxdur.shape[0])),luxdur.reshape(luxdur.shape[0]))


#calibrate lights
L = Light()
lux_dict = L.lux_dictionary

#start light loop
loop_time = luxtimes[len(luxtimes)-1] + luxdur[len(luxdur)-1] #length of light pattern

while time.time() < exp_start:
    time.sleep(.1)

cur_time = time.time() - exp_start
i = 0
time_elapsed = True
last_changed = time.time() + 10
while cur_time < exp_dur:
	#increment to next light value if enough time has elapsed
	if time.time() - last_changed >= luxdur[i]:
		time_elapsed = True
		if i >= len(luxtimes) - 1:
			i = 0
		else:
			i += 1

	#double check:
	#1st check if it is right time to change
	#2nd check if light has been on long enough at last power level
	if cur_time % loop_time >= luxtimes[i] and time_elapsed==True:#time to change light level
		
		last_changed = time.time()
		time_elapsed = False

		#if in dict, use that. else find closest match
		if luxval[i] in lux_dict:
			L.leds.value = lux_dict[luxval[i]]
			print(lux_dict[luxval[i]])
		else:
			L.leds.value = lux_dict.get(luxval[i], lux_dict[min(lux_dict.keys(), key=lambda k: abs(k-luxval[i]))])
			print(luxval[i], lux_dict.get(luxval[i], lux_dict[min(lux_dict.keys(), key=lambda k: abs(k-luxval[i]))]))
		#inc i
		
	cur_time = time.time() - exp_start