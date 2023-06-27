import argparse
import os

parser = argparse.ArgumentParser()

parser.add_argument('-src', '--source', required=True)
args = parser.parse_args()

source = open(args.source, 'r')
list_words = []
for lines in source.readlines():
	list_words += lines.split(' ')

for i in range(0, len(list_words)):
	if "|" not in list_words[i] and list_words[i].find(".") == -1 and list_words[i].find("_")== -1:
		list_words[i] += "|none"
	if "_" in list_words[i] and ("|") in list_words[i]:
		split = list_words[i].split("|")
		group = split[1]
		ss_list_words = split[0].split("_")
		for j in range(0, len(ss_list_words)):
			ss_list_words[j] = ss_list_words[j] + "|" + group
		list_words[i] = " ".join(ss_list_words)
	if "_" in list_words[i]:
		ss_list_words = list_words[i].split("_")
		for j in range(0, len(ss_list_words)):
			ss_list_words[j] = ss_list_words[j] + "|mwe"
		list_words[i] = " ".join(ss_list_words)
source.close()

source = open(args.source, 'w')
source.write(" ".join(list_words))
source.close()
