#Quinn Murphy, Kanghui Liu, Jesse Kline, Emily Wright
#Plant Observation Device
#main experiment Loop (client)


import numpy as np
import pandas as pd
import time
import sys
import argparse
from subprocess import Popen, PIPE
from Light import Light

parser = argparse.ArgumentParser()
parser.add_argument("-config", type=str, required=False, help="config file filename")
args = parser.parse_args()

#TODO: parse config file
configfile = open(args.config, 'rb')
config_data = configfile.read().split('\r\n')#should be \n for linux-made csv
print("experiment.py params:", config_data)
#exp_start = int(config_data[0])
exp_start = time.time() + 120
exp_dur = config_data[1]

csv_path = config_data[2]

water_delay = config_data[3]
water_duration = config_data[4]

light_sensor_delay = config_data[5]
light_sensor_error = config_data[6]

temp_sensor_delay = config_data[7]
temp_sensor_error = config_data[8]

photo_delay = config_data[9]


#parse csv
csvData = pd.read_csv(csv_path)
dataMatrix = csvData.as_matrix()
luxval, luxdur = np.split(dataMatrix, 2, axis = 1)
luxval = luxval.reshape(luxval.shape[0])

#sum durations to get start time for each value
luxtimes = np.subtract(np.cumsum(luxdur.reshape(luxdur.shape[0])),luxdur.reshape(luxdur.shape[0]))

#TODO: Wait for start time if given
#wait for experiment to start
camera_proc_line = 'python ~/NewPod/client/camera_client.py -start {} -duration {} -picdelay {} & '.format(exp_start, exp_dur, photo_delay)
water_proc_line = 'python ~/NewPod/client/waterpump_client.py -start {} -duration {} -waterdel {} -waterdur {} & '.format(exp_start, exp_dur, water_delay, water_duration)
lightsensor_proc_line = 'python ~/NewPod/client/lightsensor_client.py -start {} -duration {} -delay {} -error {}  -csv {} & '.format(exp_start, exp_dur, light_sensor_delay, light_sensor_error, csv_path)
tempsensor_proc_line = 'python ~/NewPod/client/tempsensor_client.py -start {} -duration {} -delay {} -error {} & '.format(exp_start, exp_dur, temp_sensor_delay, temp_sensor_error)
light_proc_line = 'python ~/NewPod/client/light_client.py -start {} -duration {} -csv {} &'.format(exp_start, exp_dur, csv_path)
#camera
all_procs = Popen(camera_proc_line+water_proc_line+lightsensor_proc_line+tempsensor_proc_line+light_proc_line,
				stdout=PIPE, stderr=PIPE, shell=True)

stdout, stderr = all_procs.communicate()

output = stdout.decode('utf-8')
outerr = stderr.decode('utf-8')
print(output)
print(outerr)