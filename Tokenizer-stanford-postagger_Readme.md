# tokenizer-stanford-postagger.py

The tokenizer uses the StanfordPOSTagger library. 

It takes a text file and outputs a tokenization of this file XXX.

How to use it:

**Exemple:**

python3.7 tokenizer-stanford-postagger.py -src DataSets/Europarl-FR-EN-Dataset/europarl-v7.test.fr-en.en -dst stanford-postagger-full-2018-10-16/test-token-en.txt -lg_core english

The **-src** argument is the source file you want to use to produce tokens (your input file)

The **-dst** argument is the file you want to create to put your results on (your output)

The **-lg_core** argument is the language of the core you're going to tokenize (here it's English)

Look here for more informations related to the StanfordPOSTagger library:

https://www.nltk.org/api/nltk.tag.html
https://www.nltk.org/api/nltk.tag.html#nltk.tag.stanford.StanfordTagger

