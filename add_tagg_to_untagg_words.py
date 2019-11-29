import argparse
import os

parser = argparse.ArgumentParser()

parser.add_argument('-src', '--source', required=True)
args = parser.parse_args()

source = open(args.source, 'r')
list_words = []
for lines in source.readlines():
	list_words += lines.split(' ')

print(list_words)

for i in range(0, len(list_words)):
        if "|" not in list_words[i] and list_words[i].find(".") == -1:
                list_words[i] += "|none"
source.close()

source = open(args.source, 'w')
for i in range(0, len(list_words)-1):
	source.write(list_words[i] + ' ')
source.write(list_words[-1])
source.close()
