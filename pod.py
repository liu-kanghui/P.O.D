#Vague skeleton of experiment loop

class Experiment():
    def __init__(self, csvFileName, configFileName):
        parser = CSVParser(csvFileName)
        self.lightVal, self.lightDur = parser.Read_Two_Column_File()

        #Experiment parameters may be changed
        configfile = open(configFileName, "r")
        self.expName = configfile.readline()
        self.expDur = int(configfile.readline())
        self.expPhotos = int(configfile.readline())
        self.expWater = float(configfile.readline())
        self.expStart = float(configfile.readline())
        self.expEnd = float(configfile.readline())

        #init lights, sensors, pump, camera
        self.l = Light()
        self.ls = LightSensor()
        self.ts = TempSensor()
        self.p = WaterPump()
        self.c = Camera()


    def run():
        #get experiment time from server (in case of previous crash)
        while time.time() < expEnd:
            #check lights are outputting correct intensity
            
            #check temperature

            #check if water needs to go on/off

            #check if camera needs to take picture

            #
