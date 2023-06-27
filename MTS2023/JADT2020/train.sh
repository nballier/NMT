#!/bin/sh

INPUT=input
OUTPUT=output

OUTDIR=$OUTPUT/datasets/snapshots
INDIR=$OUTPUT/datasets

DATA_SET=Exp
MODEL=$DATA_SET-model

mkdir -p $OUTDIR

sentences=`wc -l < input/src-train.txt`
BATCH_SIZE=100
STEPS=`expr $sentences / $BATCH_SIZE`
EPOCH=20
TOTAL_STEPS=`expr $EPOCH \* $STEPS`

echo "Training...(sentences=$sentences, batch_size=$BATCH_SIZE, steps=$STEPS, epoch=$EPOCH)"
onmt_train -data $INDIR/$DATA_SET -save_model $OUTDIR/$MODEL -world_size 1 -gpu_ranks 0  --batch_size=$BATCH_SIZE --seed 0 --train_steps $TOTAL_STEPS --save_checkpoint_steps $STEPS > $OUTDIR/$MODEL.log 2>&1
