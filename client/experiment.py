#main experiment loop
#includes calibration and light stuff, calls other processes (water, temp, light sensor, camera)

import numpy as np
import pandas as pd
import time
import sys
import argparse
from subprocess import Popen, PIPE
#from light_client import Light


parser = argparse.ArgumentParser()
parser.add_argument("-config", type=str, required=False, help="config file filename")
args = parser.parse_args()



#TODO: parse config file
configfile = open(args.config, 'r')
config_data = configfile.read().split('\n')

exp_start = int(config_data[0])
exp_dur = int(config_data[1])

csv_path = config_data[2]

water_delay = int(config_data[3])
water_duration = int(config_data[4])

light_sensor_delay = int(config_data[5])
light_sensor_error = int(config_data[6])

temp_sensor_delay = int(config_data[7])
temp_sensor_error = int(config_data[8])

photo_delay = int(config_data[9])


#parse csv
csvData = pd.read_csv(csv_path)
dataMatrix = csvData.as_matrix()
luxval, luxdur = np.split(dataMatrix, 2, axis = 1)
luxval = luxval.reshape(luxval.shape[0])

#sum durations to get start time for each value
luxtimes = np.subtract(np.cumsum(luxdur.reshape(luxdur.shape[0])),luxdur.reshape(luxdur.shape[0]))

# #calibrate lights
# L = Light()
# lux_dict = L.calibrate_light()

lux_dict = {10:1, 20:2, 30:3, 40:4, 50:5}

#TODO: Wait for start time if given
#wait for experiment to start
print(exp_start)
if exp_start == 0:
    exp_start = time.time()
else:
    while time.time() < exp_start:
        time.sleep(1)
# #start auxiliary experiment processes
# #lightsensor
# light_sensor_proc = Popen('python lightsensor_client.py -start {} -duration {} -delay {} -error {} &'.format(exp_start, exp_dur, light_sensor_delay, light_sensor_error),
#                 stdout=PIPE, stderr=PIPE, shell=True)

# #tempsensor
# temp_sensor_proc = Popen('python lightsensor_client.py -start {} -duration {} -delay {} -error {} &'.format(exp_start, exp_dur, temp_sensor_delay, temp_sensor_error),
#                 stdout=PIPE, stderr=PIPE, shell=True)

# #waterpump
# water_proc = Popen('python waterpump_client.py -start {} -duration {} -waterdel {} -waterdur {} &'.format(exp_start, exp_dur, water_delay, water_duration),
#                 stdout=PIPE, stderr=PIPE, shell=True)

# #camera
# camera_proc = Popen('python camera_client.py -start {} -duration {} picdel {} &'.format(exp_start, exp_dur, photo_delay),
# 				stdout=PIPE, stderr=PIPE, shell=True)


#start light loop
loop_time = luxtimes[len(luxtimes)-1] + luxdur[len(luxdur)-1] #length of light pattern

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
		print("inc i")	

	#double check:
	#1st check if it is right time to change
	#2nd check if light has been on long enough at last power level
	if cur_time % loop_time >= luxtimes[i] and time_elapsed==True:#time to change light level
		
		last_changed = time.time()
		time_elapsed = False

		#if in dict, use that. else find closest match
		if luxval[i] in lux_dict:
			# L.leds.value = lux_dict[luxval[i]]
			print(lux_dict[luxval[i]])
		else:
			# L.leds.value = lux_dict.get(luxval[i], lux_dict[min(lux_dict.keys(), key=lambda k: abs(k-luxval[i]))])
			print(luxval[i], lux_dict.get(luxval[i], lux_dict[min(lux_dict.keys(), key=lambda k: abs(k-luxval[i]))]))
		#inc i
		
	cur_time = time.time() - exp_start