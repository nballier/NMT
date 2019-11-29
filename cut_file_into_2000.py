import argparse
import os

parser = argparse.ArgumentParser()

parser.add_argument('-src', '--source', required=True)
parser.add_argument('-dst', '--dst', required=True)
args = parser.parse_args()

source = open(args.source, 'r')

list_lines = source.readlines()
source.close()

cmp = 0
destination = open(args.dst+str(0), 'a+')
for i in range(0, len(list_lines)):
	if cmp < 2000:
		cmp += 1
	else:
		cmp = 1
		destination.close()
		destination = open(args.dst+"file-"+str(i)+".txt", 'a+')
	destination.write(list_lines[i])

destination.close()
