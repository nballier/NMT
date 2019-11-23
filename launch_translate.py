import argparse
import os
import subprocess

parser = argparse.ArgumentParser()

parser.add_argument('-m', '--model', required=True)
args = parser.parse_args()


cmp = 0
process = []
for dirpath, dirnames, filenames in os.walk(args.model):
	for f in filenames:
		if cmp < 5:
			file_name_without_ext = f.split('.')[0]
			file_split = file_name_without_ext.split('_')
			number = file_split[-1]
			print(f)
			print(number)
			process += [subprocess.Popen("onmt_translate -model "+args.model+"/"+f+" -src /home/snake/DataSets/Europarl-Brute/test5k.en -output /home/snake/NeuralNet/Translate_Result/bpe_trad_"+number+".txt -replace_unk -gpu 0", shell=True, stdout=subprocess.PIPE)]
			cmp += 1
		else:
			for p in process:
				p.wait()
				process.remove(p)
			cmp = 0
