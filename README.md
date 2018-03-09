## It is python3 not python2
## Always do git pull, in order to minimise possible conflicts.
## Please follow good coding style. 
1. good comment, meaningful variable name
2. no line longer than 80
3. if using sublime. highly recommend anaconda pacakge. 
   it has autocomplete and code linting.


##How to run 
on main pi, cd NewPod, run python3 App.py

# P.O.D
self automate plant monitoring system

1. main controller and mini controller must be under the same network
2. replace the host in light.py to whatever mini controller's host
3. Run app.py from the main controller machine. 


## Environment requirement for mini(pi zero):
1. pi@raspberrypi:~$ sudo apt update
2. pi@raspberrypi:~$ sudo apt upgrade
3. pi@raspberrypi:~$ sudo apt install python3-gpiozero
4. enable ssh, and GPIO remote for raspberry pi


## Environment requirement for center(pi 3):
arp-scan: for getting the address of devices under the same network
qt: for frontend


1. pi@raspberrypi:~$ sudo apt update
2. pi@raspberrypi:~$ sudo apt upgrade
3. pi@raspberrypi:~$ sudo apt-get install arp-scan
4. pi@raspberrypi:~$ sudo apt-get install qt5-default qt5-designer qt5-doc qt5-dev-tools python-qt5
5. pi@raspberrypi:~$ sudo apt-get install sqlitebroswer


## Circuit:
1. LED light pins  BMP 18, 19, 20, 21, 22, 23, 24, 25