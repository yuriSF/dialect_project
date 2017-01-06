# -*- coding: utf8 -*-
import os
from HTMLParser import HTMLParser
import time
import random
import mechanize
from mechanize._opener import urlopen
from mechanize._form import ParseResponse
from bs4 import BeautifulSoup
import nltk
from nltk import tokenize
from nltk.tokenize import sent_tokenize

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def save_full():
	response = br.response().read()
	response2 = strip_tags(response)
	with open(text_file_full, 'a') as f:
		f.write(response2)

def save():
	response = br.response().read()
	response2 = strip_tags(response)
	with open(text_file, 'a') as f:
		f.write(response2)


def print_links():
	n=1
	links = br.links()
	for link in links:
		print n, link.url, link.text
		n=n+1
		print ""

def remove_script():
	soup = BeautifulSoup(response)
	for script in soup(['script', 'style']):
		script.extract()
		text = soup.get_text()
		print text
		text.decode('ascii', 'ignore')


def read_lines(file):
	with open(file, 'r') as f:
		lines = f.readlines()
	return lines


def capture_links():
	links = br.links()
	n = 1
	for link in links:
		if n>57 and n<103 and 'Save as PDF' not in link.text and "Email" not in link.text and 'Print' not in link.text and 'Add to My Collection' not in link.text:
			print n, link.text, link.url
			br.follow_link(text_regex=link.text)
			br.response().read()
			print 'read response %s' %str(n)
			save_full()
			br.follow_link(text_regex='Return to Results')
			print 'returned by following!'
			print ""
			n=n+1
		else:
			n=n+1

url = 'http://infoweb.newsbank.com/resources/search/nb?p=AWNB&b=results&action=search&fld0=alltext&val0=%22between+you+and+I%22&bln1=AND&fld1=YMD_date&val1=&sort=YMD_date%3AD'

text_file = raw_input('text file for results: ')
br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
response = br.open(url)
response = br.response().read()

for link in br.links():
	print link
	print ' '

n = 2
while n < 1000000:
	try:
		br.follow_link(text_regex='next ›')
		save()
		#capture_links()
		print n
		n=n+1

	except mechanize._mechanize.LinkNotFoundError:
		print "hit exception"
		pass
