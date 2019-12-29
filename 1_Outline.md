# TODO 

## DEADLINES FOR CONFERENCE PAPERS

### November 18th
abstract JADT : https://jadt2020.sciencesconf.org/
done


### 25 Nov
(special focus on Neural Networks)  LREC2020 (Marseille, May 11-16, 2020) https://lrec2020.lrec-conf.org/
https://lrec2020.lrec-conf.org/en/reprolang2020/call-for-papers/
REPROLANG 2020
Shared Task on the Reproduction of Research Results in Science and Technology of Language  
Satellite workshop: REPROLANG : paper for NMT:
Vanmassenhove, Eva, and Andy Way. 2018. “SuperNMT: Neural Machine Translation with Semantic Supersenses and Syntactic Supertags”. In Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (ACL 2018), pp. 67–73.
http://aclweb.org/anthology/P18-3010
Major reproduction comparables: BLEU scores (tables 1 and 2; plots in figures 2, 3 and 4).
done

### December 9th, 2019 : POSTPONED to ACL2021 ;)
deadline ACL main conf https://acl2020.org/calls/papers/


### January, 13th
[Article long JADT]: https://jadt2020.sciencesconf.org/


### 31 janvier 
deadline for TALN (paper in French)
[articleTALN](https://jep-taln2020.loria.fr/taln/)

### Feb 6th JADT notification
Camera-ready due: 10 March

### Feb 13th LREC2020 Notification
Camera-ready due: 6 March.

### March 6
8 page paper + 2 page project 
Lisbonne: http://www.eamt.org/news/news_cfp_eamt_2020.php
https://eamt2020.inesc-id.pt/

### April
possible deadlines for ACL sattelites : 
[BLACKBOX] (https://blackboxnlp.github.io/) : workshop specialised in understanding neural networks for linguists
https://www.aclweb.org/anthology/volumes/W19-48/
Workshop Paper Due Date 	April 6, 2020

### JUNE 
Plausible deadline for The 5th Workshop on Multi-word Units in Machine Translation and Translation Technology (MUMTTT 2020 in Louvain) http://www.lexytrad.es/europhras2019/mumttt-2019-2/
Conf in Sept-Oct.
RQ: can Multi-word-unit annotation inprove the training phase for neural networks?
8-12 june 2020: [TALN](https://jep-taln2020.loria.fr/dates/) 
16-19 juin 2020 TOULOUSE (France) [JADT2020](https://jadt2020.sciencesconf.org/)

### JULY
ACL2020 : July 5th through July 10th, 2020. Seattle https://acl2020.org/
WMT workshop?
July 15 deadline [Blackbox workshop](https://blackboxnlp.github.io/) @EMLP2020
[DEELIO](https://sites.google.com/view/deelio-ws/)

### AUGUST
31/08 -> 03/09 http://www.europhras.org/fr/component/jem/event/64-europhras-2020
(MUMTTT 2020 in Louvain)  

### APPELS A PROJETS
King's College, London
DIM informatique (juin 2020):
émergences 2020 (avril)
https://u-paris.fr/appel-a-manifestation-dinteret-pre-maturation/
http://www.eamt.org/news/news_call_for_proposals2020.php
institutdeshumanites.fr/linstitut/appels-a-projet/formulaire_appelaprojets2019/



## . Améliorer le script pour lancer à distance des entraînements d'OpenNMT sur du GPU
Nabil continue d'explorer les caractéristiques des différents paramètres d'OpenNMT, eg utiliser tensorboard pour le suivi de l'apprentissage. Les paramètres peuvent faire l'objet de commentaire sur la page [NN](https://github.com/nballier/NMT/blob/master/2.%20NN.md). Différentes solutions de traitement de données sont à tester, dont https://edu.google.com/ .
Jean-Baptiste installe déploie la version TensorFlow sur du Debian.


## 0bis identifier les articles rédigés à propos des deux grandes versions repérées pour OpenNMT.
TensorFlow versus Pytorch
collecter les articles correspondants 
Monter les Dockers équivalents 

## 1. ARTICLE JADT (deadline 13 janvier pour l'article)
1. Améliorer le jeu de données initial (13 époques, score BLEU).
Permettre la comparabilité avec le premier jeu de données produit.
Ajouter dans le tableau en deuxième colonne la traduction "attendue" (le tgt.test.txt).
Adjoindre le WER (via github?), voire le score ROUGE et les visualisations TensorFlow. Les données de tests et d'entraînement sont dans data.farm.zip. A moyen terme, permettre à NB d'avoir la main pour lancer les expés puis aux linguistes de récupérer les modèles entraînés.https://github.com/nballier/NMT/blob/master/1_Outline.md Par exemple, en utilisant [un outil trouvé sur GitHub ?](https://github.com/jitsi/asr-wer/blob/master/jiwer/wer.py)
A des fins de comparabilité pour les baselines, il serait judicieux de procéder à un pré-traitement type PBE pour voir si le nombre de scores BLEU négatifs diminue et si les mêmes phases sont observables. Tester avec 90000 et 30000 opérations. Il faut également relancer l'entraînement avec l'outil de visualisation TensorFlow. \\
Il serait intéressant de jouer avec ces deux options : 
**Unknown words : retrain the dataset with the two parameters**
The default translation mode allows the model to produce the <unk> symbol when it is not sure of the specific target word. Often times <unk> symbols will correspond to proper names that can be directly transposed between languages. The - replace_unk option will substitute <unk> with source words that have the highest attention weight. The
- replace_unk_tagged option will do the same, but wrap the token in a ｟unk:xxxxx｠ tag.

**JB** 
1. tester avec les 100 dernières phrases du corpus d'entraînement : DONE
2. tester avec the - replace_unk option : option disparue?
3. lancer avec plus encore plus d'époques : 30 
4. calculer le delta entre deux époques pour le score BLEU : différence 

## 2. Article sur la réplicabilité (Nematus, données annotées)  LREC2020 REPROLANG2020 
Finir l'annotation, préparer la reprise éventuelle (6 février) ou une resoumission de l'artcile.

### Données Europarl : chercher versions plus propres
@ comprend "strormtroopers", le XML permet d'extraire les langues fr, en et de (et es, si on veut)
<text language="en"> . Un script tout fait (nécessite  XMLStarlet Command Line XML Toolkit) génère des fichiers tabulaires bilingues. 

https://pub.cl.uzh.ch/wiki/public/costep/start#known_errors
The Corrected & Structured Europarl Corpus (CoStEP) http://pub.cl.uzh.ch/purl/costep
Graën, J., Batinic, D., and Volk, M. (2014). Cleaning the Europarl corpus for linguistic applications. In Konvens 2014. Stiftung Universität Hildesheim.

voir aussi
https://www.zora.uzh.ch/id/eprint/99005/
https://www.tandfonline.com/doi/suppl/10.1080/0907676X.2018.1485716?scroll=top

DE-EN
https://www.statmt.org/europarl/v7/de-en.tgz
FR-EN
https://www.statmt.org/europarl/v7/fr-en.tgz
et News-2013: extraction à discuter de
http://www.statmt.org/wmt14/translation-task.html

TODO -> RESTREINDRE à 1M mots à partir du début pour l'anglais et couper les corpus français et allemand équivalents. 
-> Récupérer l'équivalent taggué sous CCG: version française500K 
 
## script de plots (panda,numpy) OK
https://gitlab.com/nballier/reprolang2020

### Extractions données tests: OK 
- pour le corpus de test Europarl: compilation (4957 phrases en anglais ) test5k.en et 5,213 pour test5k.fr : OK
- Extraire 5K phrases de newstest2013: (2,932 sentences): newstest2013.en (OK pour 3,072 phrases .de et .fr) OK

### Voici les premiers jobs à lancer:

#### Job 0. en deux fois, pour les deux couples de langues à chaque étape et pour les fichiers de validation 
Europarl en brut avec les paramètres d'entrainement donnés pour nematus
(EN-FR,EN-DE). Le fichier de départ compte 2M de phrases. Nous avons un fichier d'entraînement à 2M de mots (EN-FE-DE).

Nous avons extrait le premier million de phrases pour la reproduction de l'expérience. (TODO)

####  Job 1<br/> OK
Europarl "tokenisé": word-segmentation with PBE (with 89,500 operations) <br/>
BPE-Encoding:(python) <br/>
https://github.com/rsennrich/subword-nmt <br/>

"To reduce the number of out-of-vocabulary (OOV) words, we follow the approach of Sennrich et al. (2016) using a variant of BPE for word segmentation capable of encoding open vocabularies with a compact symbol vocabulary of variable- length subword units. For each word that is split into subword units, we copy the features of the word in question to its subword units. 
In (3), we give an example with the word ‘stormtroopers’ that is tagged with the supersense tag ‘GROUP’. It is split into 5 subword units so the supersense tag feature is copied to all its five subword units. Furthermore, we add a none tag to all words that did not receive a supersense tag."


####  Job2  : POS
Sur 2 M de phrases en POS DE,FR, ALL, sans BPE
texte anglais annoté, texte français sans annotation 
texte anglais annoté, texte allemand sans annotation 
Europarl POS-tagged avec Stanford
POStagging: stanford
https://nlp.stanford.edu/software/tagger.shtml
JAVA (English)
https://nlp.stanford.edu/software/stanford-postagger-full-2018-10-16.zip
or Python: http://www.nltk.org/_modules/nltk/tag/stanford.html#CoreNLPPOSTagger

-> à refaire avec à 1M de phrases.
-> à refaire avec le BPE à 1M de phrases


####  Job3 texte anglais annoté, texte cible (allemand et français) annoté : DONE en 2M
German : https://nlp.stanford.edu/software/stanford-postagger-full-2016-10-31.zip
French : https://nlp.stanford.edu/software/stanford-postagger-full-2014-06-16.zip

-> à refaire avec à 1M de phrases.


####  Job 4 CCG tags with EasySRL 
EasySRL tool (Lewis et al., 2015)
https://github.com/uwnlp/EasySRL
The POS tags are generated by the Stanford POS-tagger (Toutanova et al., 2003); for the supertags we used the EasySRL tool (Lewis et al., 2015) which annotates words with CCG tags. CCG tags provide global syntactic information on the lexical level. This kind of information can help resolve ambiguity in terms of prepositional attachment, among others. An example of a CCG- tagged sentence is given in (6):

annotation 500K sur l'anglais -> faire le corpus de validation / identifier le brut français correspondant, le passer en PBE.


####  Job5 Supersenses SST
cf example (6) in the paper
Supersenses:
https://github.com/nschneid/pysupersensetagger
"To obtain the supersense tags we used the AMALGrAM (A Machine Analyzer of Lexical Groupings and Meanings) 2.0 tool 1" 

####  Job6 Combined (SST–CCG)
Discuss the separator (pipe), the order of tags and the feature representation : flat or I,O,B (TALN paper???)


####  Job 7 : contiguity tags versus boundary tags for mwe
Replace _mwe  _mwe _mwe   by  | [mwe  |mwe  | ]mwe 


####  Job 8: tags with pipes as separators ???

####  Job 9 combined info (to be discussed)
### ALL COMBINED ???
Deux scripts sont possibles pour associer les traits syntaxiques et sémantiques
Laure supervise les deux scripts exprimant les deux possibilités
-> étude de la redondance des traits et des signaux contradictoires pour mwe

#### For post-edition of MWE:
http://www.cs.cmu.edu/~ark/LexSem/
Multi-Word Expressions (MWE) and the copied feature:  
"For each word that is split into subword units, we copy the features of the word in question to its subword units. In (3), we give an example with the word ‘stormtroopers’ that is tagged with the supersense tag ‘GROUP’ "
For the MWEs we decided to copy the super- sense tag to all the words of the MWE (if provided by the tagger), as in (4). If the MWE did not receive a particular tag, we added the tag mwe to all its components, as in example (5)

####  Job10 Named Entities Recognition and upos with https://spacy.io/
####  Job  11 -> parsed information?

### Job 12 alternative annotations of MWE
[MWEToolkit3](https://gitlab.com/mwetoolkit/mwetoolkit3)
[backrground reading on MWE detection](https://m2if.lis-lab.fr/doku.php?id=20142015:memoire:sujets#unsupervised_extraction_of_multiword_expressions_from_word_alignments_and_integration_with_mwetoolkit)

### Report precision of tagging for MWE
[CLARIN gold corpus of manually annotated verbal MWE](https://lindat.mff.cuni.cz/repository/xmlui/handle/11372/LRT-2842#)
Estimate precision and recall of MWE annotation against gold corpora.

####  Report precision rates of the tools
Baseline (BPE) vs Combined (SST–CCG) NMT Systems for EN–FR, evaluated on the newstest2013.
Baseline (BPE) vs Syntactic (CCG) vs Semantic (SST) and Combined (SST–CCG) NMT Systems for EN–FR, evaluated on the newstest2013.

(1) BPE Sennrich et al. (2016)  // word-segmentation with BPE (Sennrich, 2015). We ran the BPE algorithm with 89, 500 operations.
(2) supersenses SST 
(3) PoS tags with Stanford tool (Toutanova et al., 2003)
(4) CCG tags with EasySRL tool (Lewis et al., 2015) 
CCG tags provide global syntactic information on the lexical level 


### Explorations bilingues des annotations 
- upos, pos
- mwe et PARSEME (pour les langues où c'est disponible)
Schmitt, M., Moreau, E., Constant, M., & Savary, A. (2019, July). Démonstrateur en-ligne du projet ANR PARSEME-FR sur les expressions polylexicales.
- CCG pour le français et les autres langues
- SST et WOLF pour French and German wordnet

### Article 3: TALN  (31 janvier)
Jean-Baptiste a reçu le lien Overleaf


### Article 4: EAMT
1 article de recherche
1 projet avec invitation à candidater


### ARticle 5 réplication Belinkov et al2017: qu'ont appris les réseaux de neurones?

## 3. pouvoir répliquer les trois papiers réplicables avec des données français/anglais :

### BeLINKOv ET AL. 2017 NEURAL : knowledge  morphology in MT (Hebrew morphology)
Belinkov, Y., Durrani, N., Dalvi, F., Sajjad, H., & Glass, J. (2017). What do neural machine translation models learn about morphology?. arXiv preprint arXiv:1704.03471.
https://arxiv.org/pdf/1704.03471.pdf
https://github.com/boknilev/nmt-repr-analysis
The lua code relies on a seq2seq attention model https://github.com/harvardnlp/seq2seq-attn now superseded by OpenNMT.

@inproceedings{evaluating-fine-grained-semantic-phenomena-in-neural-machine-translation-encoders-using-entailment,

  author = {Poliak, Adam and Belinkov, Yonatan and Glass, James and {Van Durme}, Benjamin},

  title = {On the Evaluation of Semantic Phenomena in Neural Machine Translation Using Natural Language Inference},

  year = {2018},

  booktitle = {Proceedings of the Annual Meeting of the North American Association of Computational Linguistics (NAACL)}

}Replicable for French???   


### TAL Linzen (monolingual language model):  using syntactic structures, verb/subject agreements and possibility of  insertions between subjects and verbs)

Tal Linzen, Emmanuel Dupoux & Yoav Goldberg (2016). Assessing the ability of LSTMs to learn syntax-sensitive dependencies. Transactions of the Association for Computational Linguistics 4, 521–535. http://tallinzen.net/media/papers/linzen_dupoux_goldberg_2016_tacl.pdf
https://github.com/TalLinzen/rnn_agreement
@article{linzen2016assessing,     Author = {Linzen, Tal and Dupoux, Emmanuel and Goldberg, Yoav},     Journal = {Transactions of the Association for Computational Linguistics},     Title = {Assessing the ability of {LSTMs} to learn syntax-sensitive dependencies},     Volume = {4},     Pages = {521--535},     Year = {2016} }
 
### K. Gulordava, P. Bojanowski, E. Grave, T. Linzen, M. Baroni. 2018. Colorless green recurrent networks dream hierarchically. Proceedings of NAACL.
https://arxiv.org/pdf/1803.11138
https://github.com/facebookresearch/colorlessgreenRNNs/tree/master/data


## 4. Implémenter les solutions de visualisation développée dans les travaux de Montavon
http://www.heatmapping.org/
http://heatmapping.org/tutorial.
https://arxiv.org/pdf/1706.07979.pdf
Montavon [Vidéo](https://www.youtube.com/watch?v=gy_Cb4Do_YE)


## 5. Problématiques diverses : Entraînement
Comment s'assurer qu'un réseau de neurones est correctement entraîné ? "neural network learning curve"

OpenNMT et la réplication d'expérience.
[Quelques paramètres d'entraînement](http://opennmt.net/OpenNMT-py/FAQ.html#how-do-i-use-the-transformer-model-do-you-support-multi-gpu).



## 6. Tâches et données typiques des conférences du domaine

[WMT2019 tasks](http://www.statmt.org/wmt19/)

News2013



## 7 BIBLIOGRAPHIE
Taylor Arnold et al. 2019 *A Computational Approach to Statistical Learning* CRC Press. 
(see  chapter 8 on neural networks, code in R) 

Servan, Chr., Crego, J and Senellart, J. (2017) Adaptation incrémentale de modèles de traduction neuronaux. In I. Eshkol and J.-Y. Antoine (Eds.) 24e Conférence sur le Traitement Automatique des Langues Naturelles TALN2017.  [218-226](taln2017.cnrs.fr/wp-content/uploads/2017/06/actes_TALN_2017-vol2Final.pdf#page=230)

Ruder, Sebastian. 2016. “An Overview of Gradient Descent Optimization Algorithms.” arXiv Preprint arXiv:1609.04747.
https://arxiv.org/pdf/1609.04747


Thushan Ganegedara Neural Machine Translator with Less than 50 lines of Code + Guide
http://www.thushv.com/natural_language_processing/neural-machine-translator-with-50-lines-of-code-using-tensorflow-seq2seq/?source=post_page-----1fe4fdfe6292----------------------

## 8. Notes
Autres systèmes : [Nematus](https://github.com/EdinburghNLP/nematus)


## ALTERNATES
Monitoring the input
CCG bank
-> test twhat the neural network has learned for CCG annotation???
Cluster the number of labels fpr each pos-tag to be learnt by the system: learning the input


Replace Byte Pair Encoding with morphological boundaries: BPE vs. Chipmunk



