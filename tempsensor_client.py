import RPi.GPIO as GPIO
import time
import Adafruit_MCP9808.MCP9808 as tempLib

parser = argparse.ArgumentParser()
parser.add_argument("-start", type=int, required=True, help="experiment start time")
parser.add_argument("-duration", type=int, required=True, help="experiment duration")

parser.add_argument("-delay", type=int, required=False, help="delay between temp tests")
parser.add_argument("-error", type=int, required=False, help="allowable error in temp in Celcius")

sensor_delay = 300 #sense every 5 minutes by default
if args.delay==True:
    sensor_delay = args.delay

sensor_error = 10
if args.error == True:
    sensor_error = args.error

exp_start = args.start
exp_dur = args.duration

sensor = tempLib.MCP9808()
sensor.begin()

while time.time() < exp_start:
    time.sleep(1)

base_temp = sensor.readTempC()
cur_time = time.time() - exp_start
while cur_time < exp_dur:
    if cur_time % sensor_delay == 0:
        cur_temp = sensor.readTempC()
        if abs(cur_temp - base_temp) > sensor_error:
            #TODO:Make error message/export to file
            print("Temp value out of range")

    cur_time = time.time() - exp_start
