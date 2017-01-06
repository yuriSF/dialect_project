# -*- coding: utf8 -*-
import nltk
from nltk import tokenize
from nltk.tokenize import sent_tokenize
import csv

town_list=[]
dates_list=[]
states_list2=[]
pub_list = []
blanks=[17, 26, 28, 30,33,57,61,89,97,99,]

text_file = 'new_titles20.txt'
csv_file = 'new_titles10.csv'


def read_lines(file):
	with open(file, 'r') as f:
		lines = f.readlines()
	return lines

def get_tokens(lines):
	for i, j in enumerate(lines):
		tok_list = []
		target ='    1.'
		if target in j:
			print j
			if search_string in lines[i+7]:
				tok_list.append(lines[i+7])
				data.append(tok_list)
			elif search_string in lines[i+8]:
				tok_list.append(lines[i+8])
				data.append(tok_list)
			elif search_string in lines[i+9]:
				tok_list.append(lines[i+9])
				data.append(tok_list)
			else:
				tok_list.append('no token')
				data.append(tok_list)


def get_info(lines):
	for i2, j2 in enumerate(lines):
		target = "    1."
		if target in j2:
			print j2
			tokens = nltk.word_tokenize(lines[i2+4])
			print tokens
			try:
				dates_list.append(tokens[-4] + ' ' + tokens[-3] + tokens[-2] + ' ' + tokens[-1])
			except:
				dates_list.append('error')
				print "date error"
							
			try:
				for i, j in enumerate(tokens):
					if j == '(':
						list =[]
						for n in range(i):
							print tokens[n] 
							list.append(tokens[n])
						list= ' '.join(list)
						print list
						pub_list.append(list)
					if '(' not in tokens and j=='-':
						list =[]
						for n in range(i):
							list.append(tokens[n])
						list= ' '.join(list)
						print list
						pub_list.append(list)
					if '(' not in tokens and '-' not in tokens:
						pub_list.append('unknown publication')
			except:
				pub_list.append('publication error')
				
			
						

	#return dates_list
	

#processing of data 
lines = read_lines(text_file)
#get_tokens(lines)
get_info(lines)

for blank_number in blanks:
	dates_list.insert(blank_number, 'blank')
	
for blank_number in blanks:
	pub_list.insert(blank_number, 'blank')


print ""
print dates_list
print ""
print pub_list


superlist = zip(dates_list, pub_list)



with open(csv_file, 'w') as fp:
    a = csv.writer(fp, delimiter=',')
    a.writerows(superlist)

