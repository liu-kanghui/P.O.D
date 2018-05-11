import time
from subprocess import Popen, PIPE

start_time = time.time() + 2
exp_dur = 10
delay = 2
error = 5

process = Popen('python tempsensor_client.py -start {} -duration {} -delay {} -error {}'.format(start_time, exp_dur, delay, error),
                stdout=PIPE, stderr=PIPE, shell=True)
stdout, stderr = process.communicate()
output = stdout.decode('ascii')
outerr = stderr.decode('ascii')
print(output)
print(outerr)