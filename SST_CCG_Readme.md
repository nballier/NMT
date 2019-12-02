# tag_with_SST_CCG.py

The tag_with_SST_CCG script gives a text tag with both SST and CCG according to the "SuperNMT: Neural Machine Translation with Semantic Supersenses and Syntactic Supertags" paper 

It takes the original the text file tagged with CCG, the text file file tagged with SST and the destination and outputs a text tagged with both CCG and SST.

How to use it:

**Exemple:**

python3.7 tag_with_SST_CCG.py -sSST ../Annotation_tools/pysupersensetagger/stormtroopers.POS.SST.txt -sCCG ../Annotation_tools/EasySRL/stormtroopers.CCG.txt -dst test.txt

The **-sSST** argument is the file tagged with SST

The **-sCCG** argument is the file tagged with CCG

The **-dst** argument is the location where you wan to put your file