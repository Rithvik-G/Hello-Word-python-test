import argparse
import json


parser = argparse.ArgumentParser()

parser.add_argument("--config-file", help = "Configuration file")

args = parser.parse_args()
if args.config_file:
	f = open(args.config_file)
	data = json.load(f)
	print(data)
else:
	print("No Config file was entered")

