

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-csv", type=str, help="cvs file for light")
    parser.add_argument("-config", type=str, help="config file name")

    fileParser = CSVParser(args.csv)
    lightVal, lightDur = fileParser.Read_Two_Column_File()

    #Experiment parameters may be changed
    configfile = open(args.config, "r")
    expName = configfile.readline()
    expDur = int(configfile.readline())
    expPhotos = int(configfile.readline())
    expWater = float(configfile.readline())
    expStart = float(configfile.readline())
    expEnd = float(configfile.readline())

    #init lights, sensors, pump, camera
    l = Light()
    ls = LightSensor()
    ts = TempSensor()
    p = WaterPump()
    c = Camera()

    #get experiment time from server (in case of previous crash)
    while time.time() < expEnd:
        #check lights are outputting correct intensity

        #check temperature

        #check if water needs to go on/off

        #check if camera needs to take picture

        #

main()
