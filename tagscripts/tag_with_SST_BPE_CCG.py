import argparse
import os

parser = argparse.ArgumentParser()

parser.add_argument('-sBPE_SST', '--source_BPE_SST', required=True)
parser.add_argument('-sCCG', '--source_CCG', required=True)
parser.add_argument('-src', '--source', required=True)
parser.add_argument('-dst', '--destination', required=True)
args = parser.parse_args()


source_BPE_SST = open(args.source_BPE_SST, 'r')
source_CCG = open(args.source_CCG, 'r')
source = open(args.source, 'r')

list_words_BPE_SST = []
for lines in source_BPE_SST.readlines():
	list_words_BPE_SST += lines.split(' ')
source_BPE_SST.close()

list_words_CCG = []
for lines in source_CCG.readlines():
	list_words_CCG += lines.split(' ')
source_CCG.close()

for i in range(0, len(list_words_CCG)):
	list_words_CCG[i] = list_words_CCG[i].split("|", 1)[1]
list_words_CCG[len(list_words_CCG)-1] = list_words_CCG[-1][0:-2]

list_words = []
for lines in source.readlines():
	list_words += lines.replace(".", " .").split(' ')
source.close()

final_list = [""] * len(list_words_BPE_SST)
cmp = 0
idx_list_words = 0

for i in range(0, len(list_words_BPE_SST)):
	if cmp >= len(list_words[idx_list_words]):
		idx_list_words += 1
		cmp = 0
	if idx_list_words < len(list_words_CCG):
		final_list[i] = list_words_BPE_SST[i] + "|" +  list_words_CCG[idx_list_words]
	else:
		final_list[i] = list_words_BPE_SST[i]
	elt_tmp = list_words_BPE_SST[i].split("|")[0]
	cmp += len(elt_tmp)

destination = open(args.destination, 'a+')
for elt in final_list:
	destination.write(elt+' ')

destination.close()
