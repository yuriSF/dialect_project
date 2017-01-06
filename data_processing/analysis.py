# -*- coding: utf8 -*-
import nltk
from nltk import tokenize
from nltk.tokenize import sent_tokenize
import csv


text_file = raw_input('file for analysis: ')
csv_file = raw_input('csv: ')
search_string = raw_input('what to search for in the token sentence: ')

data = []

def read_lines(file):
	with open(file, 'r') as f:
		lines = f.readlines()
	return lines



def get_tokens(lines):
	for i, j in enumerate(lines):
		tok_list = []
		num_list = range(1,110)
		for num in num_list:
			target = "  "+str(num)+"."
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
			
	return data

town_list=[]
dates_list=[]
states_list2=[]
pub_list = []
def get_info(lines):
	for i2, j2 in enumerate(lines):
		try:
			num_list = range(1,110)
			for num in num_list:
				target = "  "+str(num)+"."
				if target in j2:
					print j2
					tokens = nltk.word_tokenize(lines[i2+4])
					print tokens
					dates_list.append(tokens[-4] + ' ' + tokens[-3] + tokens[-2] + ' ' + tokens[-1])
					if tokens[-6] == ')':
						states_list2.append(tokens[-7])
					else: 
						states_list2.append('unknown state')
					
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
					
					for i, j in enumerate(tokens):
						if j == ')' and tokens[i-2] == ',':
							print tokens[i-3]
							town_list.append(tokens[i-3])
						if j == ')' and tokens[i-2] == '(':
							print 'unknown town'
							town_list.append('unknown town')
					
					if tokens[-5] == "-" and tokens[-6] != ')':
						print 'unknown town'
						town_list.append('unknown town')
					
					#if tokens[-6] == "(" and tokens[-8] != ')':
					#	print 'unknown town'
					#	town_list.append('unknown town')
																	
						
		except UnicodeDecodeError: 
			pass
	#return dates_list
	

#processing of data 
lines = read_lines(text_file)
tokens = get_tokens(lines)
get_info(lines)
print " "
print tokens
print ""
print dates_list
print ""
print states_list2
print ""
print pub_list
print ""
print town_list
n = 0
for list in tokens:
	try:
		list.append(states_list2[n])
		list.append(town_list[n])
		list.append(pub_list[n])
		list.append(dates_list[n])
		n=n+1
	except IndexError:
		pass

print tokens
def remove_no_token():
	for list in tokens:
		if 'no token' in list:
			tokens.remove(list)
			print list


remove_no_token()
	
with open(csv_file, 'w') as fp:
    a = csv.writer(fp, delimiter=',')
    a.writerows(tokens)

exit()