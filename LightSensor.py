import tsl2591

class LightSensor():
    def __init__(self):
        self.sensor = tsl2591.Tsl2591()
        if (self.sensor is None):
          raise LightSensorException(0); #change return val to the sensors default i2c address

    def getReading(self):
      #lux = self.sensor.lux()
      full, ir = self.sensor.get_full_luminosity()
      lux = self.sensor.calculate_lux(full, ir)
      if lux is not None:
        return lux
      else:
        raise LightSensorException(0)

    def printReading(self, lightFile):
      lux = self.getReading()
      print 'L{' + str(lux) + ',' +  time.strftime("%Y-%m-%d-%H:%M:%S") + '}'
      lightFile.write(str(lux) + "\n")
