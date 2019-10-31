import argparse
import os
from nltk.tag import StanfordPOSTagger

parser = argparse.ArgumentParser()

parser.add_argument('-src', '--source', required=True)
parser.add_argument('-dst', '--destination', required=True)
parser.add_argument('-lg_core' ,'--language_core' ,required=True)
args = parser.parse_args()

def display_models_list(model_list):
        cmp = 1
        for elt in list_models:
                print("["+ str(cmp) +"] " + elt)
                cmp+=1

def list_models_empty(list_models, stanford_dir, model_type):
	for dirpath, dirnames, filenames in os.walk(stanford_dir):
		for f in filenames:
			if f.find(model_type) != -1 and f.find("props") == -1:
				list_models.append(f)
	if not list_models:
		model_type = input("\nWrong language. Pick another one:\n")
		print(model_type)
		list_models_empty(list_models, stanford_dir, model_type)


print("models available:")

list_models = []
for dirpath, dirnames, filenames in os.walk("/"):
	for d in dirnames:
		if d.find("stanford-postagger-full") != -1:
			stanford_dir = d
			break

list_models_empty(list_models, stanford_dir, args.language_core)

display_models_list(list_models)

number_modelfile = input("\nWhich one would do like to use?:\n")
while int(number_modelfile)-1 <=0 or int(number_modelfile)-1 >= len(list_models):
	display_models_list(list_models)
	number_modelfile = input("\nWrong model. Pick another one:\n")

modelfile = stanford_dir+"/models/"+list_models[int(number_modelfile)-1]
jarfile=stanford_dir+"/stanford-postagger.jar"
tagger = StanfordPOSTagger(modelfile, jarfile)
source = open(args.source,'r')
destination = open(args.destination, 'w+')
doc = tagger.tag(source)

separator = input("\nWhich separator would you like to use?:\n")

for token in doc:
	destination.write(token[0] + separator + token[1] + "\n")

destination.close()
source.close()
