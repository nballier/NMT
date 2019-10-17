
# TODO 

## 0. Améliorer le script pour lancer à distance des entraînements d'OpenNMT sur du GPU
Nabil continue d'explorer les caractéristiques des différents paramètres d'OpenNMT, eg utiliser tensorboard pour le suivi de l'apprentissage. 

## 1. Améliorer le jeu de données initial (13 époques, score bleu).
Permettre la comparabilité avec le premier jeu de données produit.  
Adjoindre le WER (via github?), voire le score ROUGE. A moyen terme, permettre à NB d'avoir la main pour lancer les expés puis aux linguistes de récupérer les modèles entraînés.
Par exemple en utilisant [un outil trouvé sur GitHub ?](https://github.com/jitsi/asr-wer/blob/master/jiwer/wer.py)


## 2. Article sur la réplicabilité (Nematus, données annotées)

### Données Europarl
DE-EN
https://www.statmt.org/europarl/v7/de-en.tgz
FR-EN
https://www.statmt.org/europarl/v7/fr-en.tgz
et News-2013: extraction à discuter de
http://www.statmt.org/wmt14/translation-task.html


### Extractions données
Extraire 5K phrases pour corpus de validation (à réutiliser en test)



### Voici les premiers jobs à lancer:
Job 0. en deux fois, pour les deux couples de langues
Europarl en brut avec les paramètres d'entrainement donnés pour nematus
(EN-FR,EN-DE)
Extraire 5K phrases pour corpus de validation (à réutiliser en test)


Job 1
Europarl "tokenisé": word-segmentation with PBE (with 89,500 operations)
BPE-Encoding:(python)
https://github.com/rsennrich/subword-nmt

Job2 
texte anglais annoté, texte français sans annotation 
texte anglais annoté, texte allemand sans annotation 

Europarl POS-tagged avec Stanford
POStagging: stanford
https://nlp.stanford.edu/software/tagger.shtml
JAVA (English)
https://nlp.stanford.edu/software/stanford-postagger-full-2018-10-16.zip
or Python: http://www.nltk.org/_modules/nltk/tag/stanford.html#CoreNLPPOSTagger

Job3 texte anglais annoté, texte cible (allemand et français) annoté
German : https://nlp.stanford.edu/software/stanford-postagger-full-2016-10-31.zip
French : https://nlp.stanford.edu/software/stanford-postagger-full-2014-06-16.zip


Job 4 : cf example (3) Supersenses SST
BPE 

Job5 cf example 6
CCG tags with EasySRL 

Job6 Combined (SST–CCG)

Job 7 : contiguity tags versus boundary tags for mwe
Job 8: tags with pipes as separators ???

Job 9 combined info (to be discussed)

Job10 upos with 

Job  11 -> parsed information?
https://spacy.io/



Report precision rates of the tools
Baseline (BPE) vs Combined (SST–CCG) NMT Systems for EN–FR, evaluated on the newstest2013.
Baseline (BPE) vs Syntactic (CCG) vs Semantic (SST) and Combined (SST–CCG) NMT Systems for EN–FR, evaluated on the newstest2013.

(1) BPE Sennrich et al. (2016)  // word-segmentation with BPE (Sennrich, 2015). We ran the BPE algorithm with 89, 500 operations.

(2) supersenses SST 

(3) PoS tags with Stanford tool (Toutanova et al., 2003)

(4) CCG tags with EasySRL tool (Lewis et al., 2015) 
CCG tags provide global syntactic information on the lexical level 


##



## 3. Implémenter les solutions de visualisation développée dans les travaux de Montavon
http://www.heatmapping.org/
http://heatmapping.org/tutorial.
https://arxiv.org/pdf/1706.07979.pdf

Montavon [Vidéo](https://www.youtube.com/watch?v=gy_Cb4Do_YE)


## 4. pouvoir répliquer les trois papiers réplicables avec des données français/anglais :

### BeLINKOv ET AL. 2017 NEURAL : knowledge  morphology in MT (Hebrew morphology)
Belinkov, Y., Durrani, N., Dalvi, F., Sajjad, H., & Glass, J. (2017). What do neural machine translation models learn about morphology?. arXiv preprint arXiv:1704.03471.
https://arxiv.org/pdf/1704.03471.pdf
https://github.com/boknilev/nmt-repr-analysis

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
https://github.com/facebookresearch/colorlessgreenRNNs/tree/master/data


## 5. Problématiques diverses : Entraînement
Comment s'assurer qu'un réseau de neurones est correctement entraîné ? "neural network learning curve"

OpenNMT et la réplication d'expérience.
[Quelques paramètres d'entraînement](http://opennmt.net/OpenNMT-py/FAQ.html#how-do-i-use-the-transformer-model-do-you-support-multi-gpu).


## 6. Tâches et données typiques des conférences du domaine

[WMT2019 tasks](http://www.statmt.org/wmt19/)



## 7. DEADLINES FOR CONFERENCE PAPERS

### 25 Nov
(special focus on Neural Networks)  LREC2020 (Marseille, May 11-16, 2020.  ) https://lrec2020.lrec-conf.org/
https://lrec2020.lrec-conf.org/en/reprolang2020/call-for-papers/
REPROLANG 2020
Shared Task on the Reproduction of Research Results in Science and Technology of Language  
Satellite workshop: REPROLANG : paper for NMT:
Vanmassenhove, Eva, and Andy Way. 2018. “SuperNMT: Neural Machine Translation with Semantic Supersenses and Syntactic Supertags”. In Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (ACL 2018), pp. 67–73.
http://aclweb.org/anthology/P18-3010
Major reproduction comparables: BLEU scores (tables 1 and 2; plots in figures 2, 3 and 4).

### 9 décembre
texte long JADT : https://jadt2020.sciencesconf.org/
December 9, 2019
deadline ACL main conf https://acl2020.org/calls/papers/

### Feb
possible deadlines for ACL sattelites : 
[BLACKBOX] (https://blackboxnlp.github.io/) : workshop specialised in understanding neural networks for linguists
https://www.aclweb.org/anthology/volumes/W19-48/

FEB likely deadline for TALN (paper in French)
[TALN](https://jep-taln2020.loria.fr/dates/)


### JUNE 
Plausible deadline for The 5th Workshop on Multi-word Units in Machine Translation and Translation Technology (MUMTTT 2020) http://www.lexytrad.es/europhras2019/mumttt-2019-2/
Conf in Sept-Oct.
RQ: can Multi-word-unit annotation inprove the training phase for neural networks?


8-12 june 2020: [TALN](https://jep-taln2020.loria.fr/dates/) 
16-19 juin 2020 TOULOUSE (France) [JADT2020](https://jadt2020.sciencesconf.org/)


### JUILLET 
ACL2020 : July 5th through July 10th, 2020. Seattle https://acl2020.org/
WMT workshop 


## BIBLIOGRAPHIE
Taylor Arnold et al. 2019 *A Computational Approach to Statistical Learning* CRC Press. 
(see  chapter 8 on neural networks, code in R) 


## Notes
Autres systèmes : [Nematus](https://github.com/EdinburghNLP/nematus)

