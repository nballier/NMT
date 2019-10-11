
# TODO 


## Améliorer le script pour lancer à distance des entraînements d'OpenNMT sur du GPU

## 1. Améliorer le jeu de données initial (13 époques, score bleu).
Adjoindre le WER
A moyen terme, permettre d'avoir la main pour lancer les expés.

Par exemple en utilisant [un outil trouvé sur GitHub ?](https://github.com/jitsi/asr-wer/blob/master/jiwer/wer.py)



## 1. Implémenter les solutions de visualisation développée dans les travaux de Montavon
http://www.heatmapping.org/
http://heatmapping.org/tutorial.
https://arxiv.org/pdf/1706.07979.pdf

Montavon [Vidéo](https://www.youtube.com/watch?v=gy_Cb4Do_YE)

## 2. pouvoir répliquer les trois papiers réplicables avec des données français/anglais :

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



## DEADLINES FOR CONFERENCE PAPERS

25 Nov  (special focus on Neural Networks)  LREC2020 (Marseille, May 11-16, 2020.  ) https://lrec2020.lrec-conf.org/
https://lrec2020.lrec-conf.org/en/reprolang2020/call-for-papers/
REPROLANG 2020
Shared Task on the Reproduction of Research Results in Science and Technology of Language  
Satellite workshop: REPROLANG : paper for NMT:
Vanmassenhove, Eva, and Andy Way. 2018. “SuperNMT: Neural Machine Translation with Semantic Supersenses and Syntactic Supertags”. In Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (ACL 2018), pp. 67–73.
http://aclweb.org/anthology/P18-3010
Major reproduction comparables: BLEU scores (tables 1 and 2; plots in figures 2, 3 and 4).

9 décembre texte long JADT : https://jadt2020.sciencesconf.org/
December 9, 2019 deadline ACL main conf https://acl2020.org/calls/papers/


Feb possible deadlines for ACL sattelites : 
BLACKBOX : https://blackboxnlp.github.io/
https://www.aclweb.org/anthology/volumes/W19-48/

JUNE 
Plausible deadline for The 5th Workshop on Multi-word Units in Machine Translation and Translation Technology (MUMTTT 2020) http://www.lexytrad.es/europhras2019/mumttt-2019-2/
Conf in Sept-Oct.

16-19 juin 2020 TOULOUSE (France) JADT2020 https://jadt2020.sciencesconf.org/

JUILLET 
ACL2020 : July 5th through July 10th, 2020. Seattle 	 https://acl2020.org/
WMT workshop 


## BIBLIOGRAPHIE
Taylor Arnold et al. 2019 *A Computational Approach to Statistical Learning* CRC Press. 
(see  chapter 8 on neural networks, code in R) 

## Notes

Autre systèmes : [Nematus](https://github.com/EdinburghNLP/nematus)

