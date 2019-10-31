import spacy
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-src','--source', required=True)
parser.add_argument('-dst','--destination', required=True)
parser.add_argument('-lg_core','--language_core', required=True)
args = parser.parse_args()
nlp = spacy.load(args.language_core)
source = open(args.source,'r')
dest = open(args.destination,'w+')
doc = nlp(source.read())
for token in doc:
    dest.write(token.text+ ' ')
source.close()
dest.close()
