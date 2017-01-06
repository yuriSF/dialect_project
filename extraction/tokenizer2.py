# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
import nltk
#nltk.download()
nltk.help.upenn_tagset()

from nltk import tokenize
#tokenizer = nltk.data.load('nltk:tokenizers/punkt/english.pickle')
from nltk.tokenize import sent_tokenize

f = open('had_done_hit.txt', 'r')
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
	#print filt_sentlist
	print len(filt_sentlist)

def sentencize_sg():
	grammar_sg = "NP: {<PDT>?<DT>?<WDT>?<PRP$>?<CD>?<JJ>*<JJS>*<JJR>*<NN>}"
	cp = nltk.RegexpParser(grammar_sg)
	for sentence in filt_sentlist:
		tokens = nltk.word_tokenize(sentence)
		tagged_tuples = nltk.pos_tag(tokens)
		parsed = cp.parse(tagged_tuples)
		for i, j in enumerate(parsed):
			try:
				if parsed[i][0] == 'have' and parsed[i+1][0] == 'done' and parsed[i+2][-1][1] == 'NN':
					x= parsed[i+2]
					f = open('sg', 'a')
					f.write(str(x) + '\n')
					f.close()

					f = open('sg_sent', 'a')
					f.write(sentence)
					f.close()

					print str(x)

			except IndexError:
				pass


def sentencize_pl():
	grammar_pl = "NP: {<PDT>?<DT>?<WDT>?<PRP$>?<CD>?<JJ>*<JJS>*<JJR>*<NNS>}"
	cp = nltk.RegexpParser(grammar_pl)
	for sentence in filt_sentlist:
		tokens = nltk.word_tokenize(sentence)
		tagged_tuples = nltk.pos_tag(tokens)
		parsed = cp.parse(tagged_tuples)

		for i, j in enumerate(parsed):
			try:
				if parsed[i][0] == 'have' and parsed[i+1][0] == 'done' and parsed[i+2][-1][1] == 'NNS':
					x= parsed[i+2]
					f = open('pl', 'a')
					f.write(str(x) + '\n')
					f.close()

					f = open('pl_sent', 'a')
					f.write(sentence)
					f.close()

					print str(x)

			except IndexError:
				pass

def sentencize_pro():
	grammar_pro = "NP: {<PRP>}"
	cp = nltk.RegexpParser(grammar_pro)
	for sentence in filt_sentlist:
		tokens = nltk.word_tokenize(sentence)
		tagged_tuples = nltk.pos_tag(tokens)
		parsed = cp.parse(tagged_tuples)

		for i, j in enumerate(parsed):
			try:
				if parsed[i][0] == 'have' and parsed[i+1][0] == 'done' and parsed[i+2][-1][1] == 'PRP':
					x= parsed[i+2]
					f = open('pro', 'a')
					f.write(str(x) + '\n')
					f.close()

					f = open('pro_sent', 'a')
					f.write(sentence)
					f.close()

					print str(x)

			except IndexError:
				pass


def sentencize_wh():
	grammar_wh = "NP: {<WP>}"
	cp = nltk.RegexpParser(grammar_wh)
	for sentence in filt_sentlist:
		tokens = nltk.word_tokenize(sentence)
		tagged_tuples = nltk.pos_tag(tokens)
		parsed = cp.parse(tagged_tuples)

		for i, j in enumerate(parsed):
			try:
				if parsed[i][0] == 'have' and parsed[i+1][0] == 'done' and parsed[i+2][-1][1] == 'WP':
					x= parsed[i+2]
					f = open('wh', 'a')
					f.write(str(x) + '\n')
					f.close()

					f = open('wh_sent', 'a')
					f.write(sentence)
					f.close()

					print str(x)

			except IndexError:
				pass

def sentencize_poss():
	grammar_poss = "NP: {<PRP$><NN>}"
	cp = nltk.RegexpParser(grammar_poss)
	for sentence in filt_sentlist:
		tokens = nltk.word_tokenize(sentence)
		tagged_tuples = nltk.pos_tag(tokens)
		parsed = cp.parse(tagged_tuples)

		for i, j in enumerate(parsed):
			try:
				if parsed[i][0] == 'have' and parsed[i+1][0] == 'done' and parsed[i+2][-1] == 'PRP$':
					x= parsed[i+2]
					f = open('poss', 'a')
					f.write(str(x) + '\n')
					f.close()

					f = open('poss_sent', 'a')
					f.write(sentence)
					f.close()

					print str(x)

			except IndexError:
				pass


filt()
print 'filtered sentences'
#sentencize_sg()
print 'sentencized singular NPs'
#sentencize_pl()
print 'sentencized plural NPs'
#sentencize_pro()
print 'sentencized pronominal NPs'
#sentencize_wh()
print 'sentencized wh NPs'
sentencize_poss()
print 'sentencized poss NPs'
