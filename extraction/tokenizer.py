# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
import nltk
nltk.help.upenn_tagset()
from nltk import tokenize
from nltk.tokenize import sent_tokenize

grammar_pl = "NP: {<PDT>?<DT>?<WDT>?<PRP$>?<CD>?<JJ>*<JJS>*<JJR>*<NNS>}"
grammar_poss = "NP: {<PRP$><NN>}"
grammar_pro = "NP: {<PRP>}"
grammar_wh = "NP: {<WP>}"
cp = nltk.RegexpParser(grammar_sg)

f = open('has_done_hit.txt', 'r')
lines = f.readlines()
f.close()

sentence_list = []
filt_sentlist=[]

def filt():
	n=1
	for line in lines:
		sent_list = sent_tokenize(line)
		sentence_list.append(sent_list)
		n = n+1
	print n
	for list in sentence_list:
		for sentence in list:
			if "have done" in sentence and sentence not in filt_sentlist:
				filt_sentlist.append(sentence)
	print len(filt_sentlist)

def sentencize()
	for sentence in filt_sentlist:
		tokens = nltk.word_tokenize(sentence)
		tagged_tuples = nltk.pos_tag(tokens)
		parsed = cp.parse(tagged_tuples)
		for i, j in enumerate(parsed):
			try:
				if parsed[i][0] == 'have' and parsed[i+1][0] == 'done' and parsed[i+2][-1][1] == 'NN':
					x= parsed[i+2]
					f = open('has_done_poss', 'a')
					f.write(str(x) + '\n')
					f.close()
					f = open('has_done_poss_sent', 'a')
					f.write(sentence)
					f.close()
					print str(x)
			except IndexError:
				pass

sentencize()
