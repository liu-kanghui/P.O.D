#!/usr/bin/python

from subprocess import Popen, PIPE, CalledProcessError


def remote_command(hostIP, command):
    '''Parameter:   Host IP Address
                    A command to run with arguments'''
    HOST = hostIP

    # example commands
    # "python3 /home/pi/POD/waterpump_client.py"
    # "python3 /home/pi/POD/camera_client.py 120 10" <- take a pic every
    # 10 seconds for two minutes

    ssh = Popen(["ssh", "%s" % HOST, command],
                shell=False,
                universal_newlines=True,
                stdout=PIPE,
                stderr=PIPE)

    for stdout_line in iter(ssh.stdout.readline, ""):
        print(stdout_line)
    ssh.stdout.close()
    return_code = ssh.wait()

    if return_code:
        raise CalledProcessError(return_code, command)
