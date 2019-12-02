# tag_with_SST_BPE_CCG.py

The tag_with_SST_BPE script gives a text tag with both SST, BPE and CCG according to the "SuperNMT: Neural Machine Translation with Semantic Supersenses and Syntactic Supertags" paper 

It takes the original text file, the text file tagged with SST and BPE, the text file file tagged with CCG and the destination and outputs a text tagged with both CCG, BPE and SST.

How to use it:

**Exemple:**

python3.7 tag_with_SST_BPE_CCG.py -sBPE_SST text1.txt -sCCG ../Annotation_tools/EasySRL/stormtroopers.CCG.txt -dst test.txt -src ../Annotation_tools/pysupersensetagger/stormtroopers.txt

The **-src** argument is the source file you want to use to produce tokens (your input file)

The **-sCCG** argument is the file tagged with CCG

The **-sBPE_SST** argument is the file tagged with BPE and SST

The **-dst** argument is the location where you wan to put your file




