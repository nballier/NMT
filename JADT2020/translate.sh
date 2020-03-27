#!/bin/sh

INPUT=input
OUTPUT=output

MODEL=Exp-model
mkdir -p $OUTPUT/datasets/translations

for m in "$OUTPUT/datasets/snapshots/$MODEL"_step_*
do
	OUTPREFIX=`echo $m | sed -e "s/model/translation/" | sed -e "s/.pt//" | sed -e "s/snapshots/translations/"`
	OUTFILE="$OUTPREFIX.txt" 
	LOGFILE="$OUTPREFIX.log"
	echo "Translating to $OUTFILE..."
	onmt_translate -verbose -gpu 0 -replace_unk -seed 0 -model $m -src $INPUT/src-test.txt -tgt $INPUT/tgt-test.txt -output $OUTFILE > $LOGFILE 2>&1
	BLEU_SCORE="$OUTPREFIX.bleu"
	BLEU_LOG="$OUTPREFIX.bleu.log"
	echo "Generating BLEU score to $BLEU_SCORE..."
	sacrebleu --sentence-level $INPUT/tgt-test.txt --input $OUTFILE > $BLEU_SCORE 2> $BLEU_LOG
done
