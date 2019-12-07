import argparse
import os

parser = argparse.ArgumentParser()

parser.add_argument('-sCCG', '--source_CCG', required=True)
parser.add_argument('-sPOS', '--source_POS', required=True)
parser.add_argument('-dst', '--destination', required=True)
args = parser.parse_args()

source_CCG = open(args.source_CCG, 'r')
source_POS = open(args.source_POS, 'r')

list_words_CCG = []
for lines in source_CCG.readlines():
        list_words_CCG += lines.split(' ')
source_CCG.close()

list_words_POS = []
for lines in source_POS.readlines():
        list_words_POS += lines.split('\n')
list_words_POS = [word for word in list_words_POS if word is not '']

source_POS.close()
print(list_words_POS)
print(list_words_CCG)
for i in range(0, len(list_words_POS)-1):
	list_words_POS[i] = list_words_POS[i].split("|")[1]

destination = open(args.destination, 'a+')
for i in range(0, len(list_words_CCG)):
	word = list_words_CCG[i].split("|", 1)
	destination.write(word[0]+"|"+list_words_POS[i]+"|"+word[1]+" ")

destination.close()
