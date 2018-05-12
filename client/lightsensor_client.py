#!/bin/env python3

import tsl2591
import time
import numpy as np
import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-start", type=float, required=True, help="experiment start time")
parser.add_argument("-duration", type=int, required=True, help="experiment duration")
# parser.add_argument("-csv", type=str, required=False, help="delay between lux tests")

parser.add_argument("-delay", type=int, required=False, help="delay between lux tests")
parser.add_argument("-error", type=int, required=False, help="allowable error in lux")
args = parser.parse_args()

sensor_delay = 300 #sense every 5 minutes by default
if args.delay:
    sensor_delay = args.delay

sensor_error = 1000
if args.error:
    sensor_error = args.error

# #read csv file
# csvData = pd.read_csv(args.csv)
# dataMatrix = csvData.as_matrix()
# luxval, luxdur = np.split(dataMatrix, 2, axis = 1)
#
# #sum durations to get start time for each value
# luxtimes = np.subtract(np.cumsum(luxdur.reshape(luxdur.shape[0])),luxdur.reshape(luxdur.shape[0]))

exp_start = args.start
exp_dur = args.duration

sensor = tsl2591.Tsl2591()

while time.time() < exp_start:
    time.sleep(1)

arr_ind = 0
cur_time = time.time() - exp_start
while cur_time < exp_dur:
    # while cur_time < luxtimes[arr_ind]:
    #     arr_ind+=1

    if int(cur_time) % sensor_delay == 0:
        full, ir = sensor.get_full_luminosity()
        lux = sensor.calculate_lux(full, ir)
        print(lux)
    time.sleep(1)
        # if abs(luxval[arr_ind]-lux) > sensor_error:
        #     #TODO:Make error message/export to file
        #     print("Light value out of range")

    cur_time = time.time() - exp_start
