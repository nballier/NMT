# tag_with_SST_BPE.py
# tag_with_SST_CCG.py
# tag_with_POS_CCG.py
# tag_with_SST_BPE_CCG.py
# add_tag_and_mwe_to_untagg_words.py

The tag_with_SST_BPE script gives a text tag with both SST and BPE according to the "SuperNMT: Neural Machine Translation with Semantic Supersenses and Syntactic Supertags" paper 

It takes the original text file, the text file tagged with BPE, the text file file tagged with SST and the destination and outputs a text tagged with both BPE and SST.

How to use it:

**Exemple:**

python3.7 tag_with_SST_BPE.py -sBPE ../Annotation_tools/pysupersensetagger/stormtroopers.BPE -sSST ../Annotation_tools/pysupersensetagger/stormtroopers.POS.SST.txt -dst test.txt -src ../Annotation_tools/pysupersensetagger/stormtroopers.txt

The **-src** argument is the source file you want to use to produce tokens (your input file)

The **-sSST** argument is the file tagged with SST

The **-sBPE** argument is the file tagged with BPE

The **-dst** argument is the location where you wan to put your file



The tag_with_POS_CCG script gives a text tag with both POS and CCG according to the "SuperNMT: Neural Machine Translation with Semantic Supersenses and Syntactic Supertags" paper 

It takes the original text file, the text file tagged with POS, the text file file tagged with CCG and the destination and outputs a text tagged with both CCG and POS.

How to use it:

**Exemple:**

python3.7 tag_with_POS_CCG.py -sPOS stormtroopers.POS.txt -sCCG ../Annotation_tools/EasySRL/stormtroopers.CCG.txt -dst stormtroopers.POS.CCG.txt

The **-sCCG** argument is the file tagged with CCG

The **-sPOS** argument is the file tagged with POS

The **-dst** argument is the location where you wan to put your file




The tag_with_SST_BPE script gives a text tag with both SST, BPE and CCG according to the "SuperNMT: Neural Machine Translation with Semantic Supersenses and Syntactic Supertags" paper 

It takes the original text file, the text file tagged with SST and BPE, the text file file tagged with CCG and the destination and outputs a text tagged with both CCG, BPE and SST.

How to use it:

**Exemple:**

python3.7 tag_with_SST_BPE_CCG.py -sBPE_SST text1.txt -sCCG ../Annotation_tools/EasySRL/stormtroopers.CCG.txt -dst test.txt -src ../Annotation_tools/pysupersensetagger/stormtroopers.txt

The **-src** argument is the source file you want to use to produce tokens (your input file)

The **-sCCG** argument is the file tagged with CCG

The **-sBPE_SST** argument is the file tagged with BPE and SST

The **-dst** argument is the location where you wan to put your file



The tag_with_SST_CCG script gives a text tag with both SST and CCG according to the "SuperNMT: Neural Machine Translation with Semantic Supersenses and Syntactic Supertags" paper 

It takes the original the text file tagged with CCG, the text file file tagged with SST and the destination and outputs a text tagged with both CCG and SST.

How to use it:

**Exemple:**

python3.7 tag_with_SST_CCG.py -sSST ../Annotation_tools/pysupersensetagger/stormtroopers.POS.SST.txt -sCCG ../Annotation_tools/EasySRL/stormtroopers.CCG.txt -dst test.txt

The **-sSST** argument is the file tagged with SST

The **-sCCG** argument is the file tagged with CCG

The **-dst** argument is the location where you wan to put your file



The add_tagg_and_mwe_to_untagg_words script tagg untagg words with |none and expression with |mwe or |GROUP (which is the group of the expression) according to the "SuperNMT: Neural Machine Translation with Semantic Supersenses and Syntactic Supertags" paper 

It takes a text file and outputs the completed tagged file.

How to use it:

**Exemple:**

python3.7 add_tagg_to_untagg_words.py -src ../Annotation_tools/pysupersensetagger/valid.tag.cut.sst

The **-src** argument is the source file to complete





