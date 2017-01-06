# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
import nltk
#nltk.download()
nltk.help.upenn_tagset()

from nltk import tokenize
#tokenizer = nltk.data.load('nltk:tokenizers/punkt/english.pickle')
from nltk.tokenize import sent_tokenize

#grammar = nltk.CFG.fromstring
s =  [('To', 'TO'), ('do', 'VB'), ('that', 'DT'), ('they', 'PRP'), ('have', 'VBP'), ('done', 'VBN'), ('a', 'DT'), ('number', 'NN'), ('initiatives', 'VBZ'), ('including', 'VBG'), ('Raised', 'VBN')]

s2 = [('...', ':'), ('job', 'NN'), ('answering', 'NN'), ('them', 'PRP'), (',', ','), ('but', 'CC'), ('could', 'MD'), ('have', 'VB'), ('done', 'VBN'), ('a', 'DT'), ('better', 'JJR'), ('job', 'NN'), ('hanging', 'VBG'), ('on', 'IN'), ('to', 'TO'), ('the', 'DT'), ('lead', 'NN'), (',', ','), ("''", "''")]

grammar = "NP: {<PDT>?<DT>?<JJ>*<NN>}"	

# improve parser to include comparative adjectives

#  ? = one optional
# * = many optional

#grammar = "NP: {<NN>}"

cp = nltk.RegexpParser(grammar)

result = cp.parse(s2)
print result
print result[3]
print result[3][0]
print result[3][0][0]

print result[2]
print result[2][0]
print result[2][0][0]

# if result [n][0][0] is a character: not a target tag

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
			#for n in range(len(parsed)):
				# if parsed[n][0][0] = character this is not a target tag


	
chunker()		