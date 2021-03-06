#!/usr/bin/env python3

import argparse
import re

parser = argparse.ArgumentParser(description='Prepare tagged text for ONMT. Flair tagging to POS tagging.')
parser.add_argument('src', type=argparse.FileType('r',encoding='UTF-8'), help='Flair tagged file')
parser.add_argument('out', type=argparse.FileType('w',encoding='UTF-8'), help='ONMT tagged output file')
parser.add_argument('-v','--verbose', action='store_true', default=False, help='verbose mode')
parser.add_argument('-pun','--punctuation', default='PUN', help='punctuation tag, default PUN')
parser.add_argument('-tok','--token', default='TOK', help='punctuation tag, default TOK')
parser.add_argument('-convert','--convert-tag-to-generic', action='store_true', default=False, help='convert Flair tagging to generic (ie X-YYYY to YYYY)', dest='convert')
#parser.add_argument('-pos','--src-pos', type=argparse.FileType('r',encoding='UTF-8'), help='POS tagged file')

args = parser.parse_args()
src = args.src
out = args.out

if args.convert:
    flair_tag_regex = '.-(.+?)'
else:
    flair_tag_regex = '(.+?)'
flair_regex = re.compile('(\S+?) <'+flair_tag_regex+'>')
onmt_pos_regex = re.compile('(\S+?)\uffe8(\S+)')
punc_pos_regex = re.compile('(\S+?)([,;\.\?])\uffe8(\S+)')

for line in src:
    line = line.rstrip(' \n')
    if args.verbose:
        print(f'INPUT: {line}')
    line = flair_regex.sub('\\1\uffe8\\2',line)
    words = line.split(' ')
    out_words = []
    for word in words:
        if not onmt_pos_regex.match(word):
            out_words.append(f'{word}\uffe8{args.token}')
        else:
            out_words.append(word)
    line = ' '.join(out_words)
    line = punc_pos_regex.sub(f'\\1\uffe8\\3 \\2\uffe8{args.punctuation}',line)
    if args.verbose:
        print(f'OUTPUT: {line}')
    out.write(line+'\n')
