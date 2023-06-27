import argparse
import os

parser = argparse.ArgumentParser()

parser.add_argument('-sBPE', '--source_BPE', required=True)
parser.add_argument('-sSST', '--source_SST', required=True)
parser.add_argument('-src', '--source', required=True)
parser.add_argument('-dst', '--destination', required=True)
args = parser.parse_args()

os.system("python3.7 add_tagg_and_mwe_to_untagg_words.py -src "+args.source_SST)

source_BPE = open(args.source_BPE, 'r')
source_SST = open(args.source_SST, 'r')
source = open(args.source, 'r')

list_words_BPE_tmp = []
for lines in source_BPE.readlines():
	list_words_BPE_tmp += lines.split(' ')
source_BPE.close()

list_words_SST = []
for lines in source_SST.readlines():
	list_words_SST += lines.split(' ')
source_SST.close()
list_words_SST = [words for words in list_words_SST if words != '\n']

list_words = []
for lines in source.readlines():
	list_words += lines.replace(".", " .").split(' ')
source.close()

list_words_BPE = [""]*len(list_words_SST)
cmp = 0
idx_list_words = 0
reconstitution_str = ""
for elt in list_words_BPE_tmp:
	if cmp < len(list_words[idx_list_words]):
		reconstitution_str += elt
		elt_tmp = elt.replace("@@", "")
		cmp += len(elt_tmp)
	else:
		list_words_BPE[idx_list_words] = reconstitution_str
		idx_list_words += 1
		reconstitution_str = elt
		elt_tmp = elt.replace("@@", "")
		cmp = len(elt_tmp)

list_words_BPE[-1] = reconstitution_str

destination = open(args.destination, 'a+')
for i in range(0, len(list_words_BPE)):
	if list_words_BPE[i].find(".") == -1:
		group = list_words_SST[i].split("|")
		if "@@" in list_words_BPE[i]:
			list_words_BPE[i] = list_words_BPE[i].replace("@@","@@|" + group[1] + " ")
		if list_words_BPE[i].endswith(" "):
			list_words_BPE[i] = list_words_BPE[i][:-1]
		if not list_words_BPE[i].endswith(group[1]):
			list_words_BPE[i] = list_words_BPE[i] +"|" + group[1]
	destination.write(list_words_BPE[i]+' ')

destination.close()
