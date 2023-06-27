#!/bin/sh

INPUT=input
OUTPUT=output

DATA_SET=Exp
OUTDIR=$OUTPUT/datasets
mkdir -p $OUTDIR

echo "Preprocessing..."
onmt_preprocess -train_src $INPUT/src-train.txt -train_tgt $INPUT/tgt-train.txt -valid_src $INPUT/src-val.txt -valid_tgt $INPUT/tgt-val.txt -save_data $OUTDIR/$DATA_SET > $OUTDIR/$DATA_SET.log 2>&1
