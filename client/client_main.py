import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-light_dic', metavar="light dictionary")
parser.add_argument('-config_obj', metavar="config object")
args = parser.parse_args()

light_dic = args.light_dic
config_obj = args.config_obj
