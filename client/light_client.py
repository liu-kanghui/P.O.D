from gpiozero import LEDBoard
import tsl2591
from time import sleep


parser = argparse.ArgumentParser()
parser.add_argument(("-cvs", metavar="m", help="cvs file for light"))

Light(parser.cvs)




class Light():

    def __init__(self, cvsFile):
        ''' initialize the hostIP and leds GPIO pins'''
        self.cvsFile = cvsFile
        # 18, 19, 20, 21, 22, 23, 24, 25 are the connected GPIO pins
        self.leds = LEDBoard(18, 19, 20, 21, 22, 23, 24, 25)
        self.sensor = tsl2591.Tsl2591()

    def calibrate_light(self):
        ''' Return a dictionary of lux and array value for GPIO Pins'''
        self.leds.on()
        lux_dictionary = dict()
        for led_7 in range(0, 11, 5):
            value_7 = led_7 / 100
            for led_6 in range(0, 11, 5):
                value_6 = led_6 / 10
                for led_5 in range(0, 11, 5):
                    value_5 = led_5 / 10
                    self.leds.value = (1, 1, 1, 1, 1,
                                       value_5, value_6, value_7)
                    sleep(1)  # make sure the light stay up at the range for 1s
                    full, ir = self.sensor.get_full_luminosity()
        			lux = self.sensor.calculate_lux(full, ir)
                    if lux not in lux_dictionary:
                        lux_dictionary[lux] = [1, 1, 1, 1, 1,
                                               value_5, value_6, value_7]
                        print("lux {} ： {}".format(lux, lux_dictionary[lux]))
                    else:
                        print("lux value already exist")
        return lux_dictionary
