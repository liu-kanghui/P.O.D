import json

data = {}

def createGroup(group_name, host_array, csv, water_time, water_delay, photo_per_day):
	file = open("record_file.txt","w")
	file.write("group_name: " + group_name )
	file.write("host: ")
	for host in host_array:
		file.write(host + ' ')
	file.write("\n")
	file.write("cvs: " + cvs + "\n")
	file.write("water_time: " + water_time + "\n")
	file.write("water_delay: " + water_delay + "\n")
	file.write("photo_per_day: " + photo_per_day + "\n")

