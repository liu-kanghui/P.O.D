import RPi.GPIO as GPIO
import time
import Adafruit_MCP9808.MCP9808 as tempLib
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-start", type=float, required=True, help="experiment start time")
parser.add_argument("-duration", type=int, required=True, help="experiment duration")

parser.add_argument("-delay", type=int, required=False, help="delay between temp tests")
parser.add_argument("-error", type=int, required=False, help="allowable error in temp in Celcius")

args = parser.parse_args()

if args.delay:
    sensor_delay = args.delay
else:
	sensor_delay = 300 #sense every 5 minutes by default

print(sensor_delay)

sensor_error = 10
if args.error:
    sensor_error = args.error

exp_start = args.start
exp_dur = args.duration

sensor = tempLib.MCP9808()
sensor.begin()

while time.time() < exp_start:
    time.sleep(1)
    print("waiting...")

base_temp = sensor.readTempC()
cur_time = time.time() - exp_start
while cur_time < exp_dur:
	if int(cur_time) % sensor_delay == 0:
		cur_temp = sensor.readTempC()
		print(cur_temp)
		if abs(cur_temp - base_temp) > sensor_error:
			#TODO:Make error message/export to file
			print("Temp value out of range")
	time.sleep(1)
	cur_time = time.time() - exp_start
	print(int(cur_time))
