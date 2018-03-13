#!/usr/bin/python
# -*- coding: utf-8 -*-
from subprocess import Popen, PIPE, CalledProcessError


'''
This is the server side code for water pump

'''


def pump_water(hostIP, runTime, delayTime):
    '''Parameter:  host IP address
            run time for each pump
            delay time after each pump '''
    HOST = hostIP
    # Ports are handled in ~/.ssh/config since we use OpenSSH
    CMD = "python3 /home/pi/POD/waterpump_client.py"

    ssh = Popen(["ssh", "%s" % HOST, CMD, str(runTime), str(delayTime)],
                shell=False,
                universal_newlines=True,
                stdout=PIPE,
                stderr=PIPE)
    for stdout_line in iter(ssh.stdout.readline, ""):
        print(stdout_line)
    ssh.stdout.close()
    return_code = ssh.wait()
    if return_code:
        raise CalledProcessError(return_code, CMD)


# waterPump('192.168.1.102', 2, 10)
