# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
import nltk
from nltk import tokenize
tokenizer = nltk.data.load('nltk:tokenizers/punkt/english.pickle')
from nltk.tokenize import sent_tokenize

data = raw_input("File path: ")
f = open(data, 'r')
lines = f.readlines()
f.close()

for line in lines:
	try:
		sentlist = sent_tokenize(line)
		for sentence in sentlist:
			tokens = nltk.word_tokenize(sentence)
			tagged_tuples = nltk.pos_tag(tokens)
			grammar_sg = "NP: {<DT><JJ><NN>}"
			cp = nltk.RegexpParser(grammar_sg)
			parsed = cp.parse(tagged_tuples)
			print parsed
	except:
		pass
