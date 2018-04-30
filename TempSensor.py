import RPi.GPIO as GPIO # from pi zero light driver code
import os, sys, time, datetime as datetime
import Adafruit_MCP9808.MCP9808 as tempLib

class TempSensorException(Exception):
  def __init__(self, value):
    self.value = value
  def __str__(self):
    return repr(self.value)

class TempSensor():
    def __init__(self):
        self.sensor = tempLib.MCP9808()
        self.sensor.begin()
    def getReading(self):
        return self.sensor.readTempC()
    def printReading(self, tempFile):
      #print '{0:0.3F} , {0:0.3F}'(self.sensor.readTempC(), time.clock())
      print 'T{' + str(self.getReading()) + ',' + time.strftime("%Y-%m-%d-%H:%M:%S") + '}'
      tempFile.write(str(self.getReading()) + "\n")
