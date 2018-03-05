# P.O.D
self automate plant monitoring system

1. main controller and mini controller must be under the same network
2. replace the host in light.py to whatever mini controller's host
3. Run app.py from the main controller machine. 


## Language: python3
## UI: PyQt 5 

## Environment requirement for mini(pi zero):
1. pi@raspberrypi:~$ sudo apt update
2. pi@raspberrypi:~$ sudo apt install python3-gpiozero
3. enable ssh, and GPIO remote for raspberry pi


## Environment requirement for center(pi 3):
1. sudo apt-get install qt5-default qt5-designer qt5-doc qt5-dev-tools python-qt5

## Circuit:
1. LED light pins  BMP 18, 19, 20, 21, 22, 23, 24, 25