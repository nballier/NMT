import argparse
import os

parser = argparse.ArgumentParser()

parser.add_argument('-sCCG', '--source_CCG', required=True)
parser.add_argument('-sSST', '--source_SST', required=True)
parser.add_argument('-dst', '--destination', required=True)
args = parser.parse_args()

os.system("python3.7 add_tagg_to_untagg_words.py -src "+args.source_SST)

source_CCG = open(args.source_CCG, 'r')
source_SST = open(args.source_SST, 'r')

list_words_CCG = []
for lines in source_CCG.readlines():
        list_words_CCG += lines.split(' ')
source_CCG.close()
print(list_words_CCG)
list_words_SST = []
for lines in source_SST.readlines():
        list_words_SST += lines.split(' ')
source_SST.close()
print(list_words_SST)
for i in range(0, len(list_words_SST)-1):
	list_words_SST[i] = list_words_SST[i].split("|")[1]
print(list_words_SST)
print(list_words_CCG)

destination = open(args.destination, 'a+')
for i in range(0, len(list_words_CCG)):
	word = list_words_CCG[i].split("|", 1)
	destination.write(word[0]+"|"+list_words_SST[i]+"|"+word[1]+" ")

destination.close()
