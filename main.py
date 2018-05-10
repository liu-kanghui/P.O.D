import json
import datetime
import os
import config
import detect_device_ip
from subprocess import Popen, PIPE

data = {}


# create group
def addGroup(group_name, host_array, light_csv, num_water, water_duration, photo_per_day, start_time, end_time):
    filename = "record1_file.txt"
    append_write = 'w'
    if os.path.exists(filename):
        append_write = 'a'
    file_pointer = open(filename, append_write)
    config_file = open("pod-config", 'w')

    file_pointer.write("group_name: " + group_name + "\n")
    file_pointer.write("csv path: " + light_csv + "\n")
    file_pointer.write("num_water: " + str(num_water) + "\n")
    file_pointer.write("water_duration: " + str(water_duration) + "\n")
    file_pointer.write("photo_per_day: " + str(photo_per_day) + "\n")
    file_pointer.write("start_time: " + str(start_time) + "\n")
    file_pointer.write("end_time: " + str(end_time) + "\n")

    config_file.write("group_name: " + group_name + "\n")
    config_file.write("csv path: " + light_csv + "\n")
    config_file.write("num_water: " + str(num_water) + "\n")
    config_file.write("water_duration: " + str(water_duration) + "\n")
    config_file.write("photo_per_day: " + str(photo_per_day) + "\n")
    config_file.write("start_time: " + str(start_time) + "\n")
    config_file.write("end_time: " + str(end_time) + "\n")
    file_pointer.write("host: ")

    config_file_path = os.path.abspath("pod-config")
    light_csv_path =  os.path.abspath(light_csv)

    for host in host_array:
        file_pointer.write(host + " ")
        print("how many")
        # remote_file_place = host + ":/P.O.D/client/"
        # process = Popen('scp {} {} {}'.format(light_csv_path, config_file_path,  remote_file_place),
        #                 stdout=PIPE, stderr=PIPE, shell=True)
        # stdout, stderr = process.communicate()
    file_pointer.write("\n\n")



hi = ['192.168.1.100',  '192.168.1.101',  '192.168.1.102']


if __name__ == "__main__":
    addGroup("funny", hi, '/test.cvs', 2, 10, 1, "2018-5-12-12", "2018-6-12-12")





# def main():
#     parser = argparse.ArgumentParser()
#     parser.add_argument("-csv", type=str, help="cvs file for light")
#     parser.add_argument("-config", type=str, help="config file name")
#
#     fileParser = CSVParser(args.csv)
#     lightVal, lightDur = fileParser.Read_Two_Column_File()

    #Experiment parameters may be changed
    # configfile = opeconfigfile.readline())
    # expWater = float(configfile.readline())
    # expStart = float(configfile.readline())
    # expEnd = float(configfile.readline())

    #init lights, sensors, pump, camera
    # l = Light()
    # ls = LightSensor()
    # ts = TempSensor()
    # p = WaterPump()
    # c = Camera()

    #get experiment time from server (in case of previous crash)
    # while time.time() < expEnd:
        #check lights are outputting correct intensity

        #check temperature

        #check if water needs to go on/off

        #check if camera needs to take picture

        #

# main()
