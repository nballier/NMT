The tokenizer uses the spicy library. 

It takes a text file and outputs a tokenization of this file usable by subword-nmt.

How to use it:

Exemple:
python3.7 tokenizer.py -src DataSets/Europarl-FR-EN-Dataset/europarl-v7.test.fr-en.en -dst test-token-en.txt -lg_core en_core_web_sm

The -src argument is the source file you want to use to produce tokens (your input file)
The -dst argument is the file you want to create to put your results on (your output)
The -lg_core argument is the core you'll use depending on the language you're going to tokenize (here it's english)

Look here for more informations related to the Spicy Language Cores:

https://spacy.io/usage/models

Exemple of usages with subword-nmt using the test-token produces with the tokenizer:
subword-nmt -learn-bpe < test-token-en.txt > codes.bpe
subword-nmt apply_bpe -c codes.bpe < train.tok > train.tok.bpe
