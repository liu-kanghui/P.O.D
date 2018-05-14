import time
from subprocess import Popen, PIPE

start_time = time.time()
exp_dur = 30
light_delay = 2
pump_delay = 5
pic_delay = 5
pump_dur = 2
error = 5

# #lightsensor
# process1 = Popen('python lightsensor_client.py -start {} -duration {} -delay {} -error {} &'.format(start_time, exp_dur, light_delay, error),
#                 stdout=PIPE, stderr=PIPE, shell=True)

# #lights
# process2 = Popen('python light_client.py &',
#                  stdout=PIPE, stderr=PIPE, shell=True)

# #waterpump
# process3 = Popen('python waterpump_client.py -start {} -duration {} -waterdel {} -waterdur {} &'.format(start_time, exp_dur, pump_delay, pump_dur),
#                 stdout=PIPE, stderr=PIPE, shell=True)

#lightsensor
process4 = Popen('python camera_client.py -start {} -duration {} -picdelay {}  &'.format(start_time, exp_dur, pic_delay),
                stdout=PIPE, stderr=PIPE, shell=True)

# stdout1, stderr1 = process1.communicate()
# output1 = stdout1.decode('ascii')
# outerr1 = stderr1.decode('ascii')
# print(output1)
# print(outerr1)

# stdout2, stderr2 = process2.communicate()
# output2 = stdout2.decode('ascii')
# outerr2 = stderr2.decode('ascii')
# print(output2)
# print(outerr2)

# stdout3, stderr3 = process3.communicate()
# output3 = stdout3.decode('ascii')
# outerr3 = stderr3.decode('ascii')
# print(output3)
# print(outerr3)

stdout4, stderr4 = process4.communicate()
output4 = stdout4.decode('ascii')
outerr4 = stderr4.decode('ascii')
print(output4)
print(outerr4)