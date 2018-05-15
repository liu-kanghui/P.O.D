import time
from subprocess import Popen, PIPE

start_time = time.time()
exp_dur = 30
pic_delay = 5


hosts = ['192.168.1.102', '192.168.1.111']

process1 = Popen('ssh '+hosts[0]+' python ~/NewPod/client/camera_client.py -start {} -duration {} -picdelay {}  &'.format(start_time, exp_dur, pic_delay),
                stdout=PIPE, stderr=PIPE, shell=True)
stdout1, stderr1 = process1.communicate()


process2 = Popen('ssh '+hosts[1]+' python ~/NewPod/client/camera_client.py -start {} -duration {} -picdelay {}  &'.format(start_time, exp_dur, pic_delay),
                stdout=PIPE, stderr=PIPE, shell=True)
stdout2, stderr2 = process2.communicate()


output1 = stdout1.decode('ascii')
outerr1 = stderr1.decode('ascii')
print(output1)
print(outerr1)

output2 = stdout2.decode('ascii')
outerr2 = stderr2.decode('ascii')
print(output2)
print(outerr2)