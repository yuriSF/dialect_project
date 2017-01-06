# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
import nltk
nltk.help.upenn_tagset()

from nltk import tokenize
from nltk.tokenize import sent_tokenize

grammar = "NP: {<PDT>?<DT>?<JJ>*<NN>}"
cp = nltk.RegexpParser(grammar)
result = cp.parse(s2)

f = open("done_test19.txt", 'r')
lines = f.readlines()
f.close()

def chunker():
	for line in lines:
		sent_list = sent_tokenize(line)
		#print sent_list
		for sentence in sent_list:
			tokens = nltk.word_tokenize(sentence)
			tagged_tuples = nltk.pos_tag(tokens)
			#print tagged_tuples
			#print " "
			parsed = cp.parse(tagged_tuples)
			for tuple in parsed:
				f = open("done_test21.txt", 'a')
				f.write(str(tuple)+'\n')
				f.close()
				print tuple
	
chunker()
