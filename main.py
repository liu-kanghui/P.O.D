import json
import datetime
import os
from subprocess import Popen, PIPE

data = {}




# create group
def addGroup(group_name, host_array, light_csv, num_water, water_duration, photo_per_day, start_time, end_time):
    filename = "record_file.txt"
    append_write = 'w'
    if os.path.exists(filename):
        append_write = 'a'
    main_record_file = open(filename, append_write)
    little_config_file = open("pod-config", 'w')

    main_record_file.write("group_name: " + group_name + "\n")
    main_record_file.write("csv path: " + light_csv + "\n")
    main_record_file.write("num_water: " + str(num_water) + "\n")
    main_record_file.write("water_duration: " + str(water_duration) + "\n")
    main_record_file.write("photo_per_day: " + str(photo_per_day) + "\n")
    main_record_file.write("start_time: " + str(start_time) + "\n")
    main_record_file.write("end_time: " + str(end_time) + "\n")

    little_config_file.write("group_name: " + group_name + "\n")
    little_config_file.write("csv path: " + light_csv + "\n")
    little_config_file.write("num_water: " + str(num_water) + "\n")
    little_config_file.write("water_duration: " + str(water_duration) + "\n")
    little_config_file.write("photo_per_day: " + str(photo_per_day) + "\n")
    little_config_file.write("start_time: " + str(start_time) + "\n")
    little_config_file.write("end_time: " + str(end_time) + "\n")
    little_config_file.close()
    main_record_file.write("host: ")

    config_file_path = os.path.abspath("pod-config")

    light_csv_path =  os.path.abspath("test.csv")

    print(light_csv_path)
    print(config_file_path)

    for host in host_array:
        main_record_file.write(host + " ")
        remote_file_place = host + ":~/NewPod/client/"

        process = Popen('sshpass -p "raspberry" scp {} {} {}'.format(light_csv_path, config_file_path, remote_file_place),
                        stdout=PIPE, stderr=PIPE, shell=True)
        stdout, stderr = process.communicate()


        CMD = "python /home/pi/NewPod/client/light_client.py"
        process = Popen('sshpass -p "raspberry" {} {}'.format(host, CMD),
                        stdout=PIPE, stderr=PIPE, shell=True)
        stdout, stderr = process.communicate()



    main_record_file.write("\n\n")



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
