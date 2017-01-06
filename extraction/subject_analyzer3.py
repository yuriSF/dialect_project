# -*- coding: utf-8 -*-
"""
Created on Mon May 30 07:45:15 2016

@author: yuri
"""

#from __future__ import unicode_literals

import nltk
from nltk import tokenize
from nltk.tokenize import sent_tokenize
import csv
import sys
import os

grammar_np = "NP: {<PDT | DT | WDT | PRP\$ | CD>? <VBG>? <JJ|JJS|JJR>* <NN|NNP|NNS|NNPS>* <POS>* <NN|NNS|NNP|NNPS>* <POS>* <NN|NNP|NNS|NNPS> | <PRP> } "

def save(line):
   with open('test_subj2', 'a') as f5:
        f5.write(line)

def tree_string(tree):
    l = [item[0] for item in tree]
    l2 = ' '.join(l)
    return l2

def get_pattern(nounPhrase):
    l = [item[1] for item in nounPhrase]
    l2 = ' '.join(l)
    return l2


def subj_nps(data, central_word):
    cp_np = nltk.RegexpParser(grammar_np)
    for row in data:
        line =  row[1]
        print line
        tokens = nltk.word_tokenize(line)
        try:
            for i, j in enumerate(tokens):
                if j == 'finished':
                    # cut tokens to 'finished'
                    tokens_red = tokens[0:i-1]
                    #remove apositives if immediately preceding finished
                    if tokens_red[-1] == ',':
                        for i2, j2 in enumerate(tokens_red[0:-1]):
                            if j2 == ',':
                                tokens_red = tokens_red[0:i2]
                    tagged_tuples = nltk.pos_tag(tokens_red)
                    verb_list = ['VBZ', 'VBP', 'VBD', 'VBN', 'VBG', 'VB']
                    ind_list = []
                    for ind, tup in enumerate(tagged_tuples):
                        if tup[1] in verb_list:
                            ind_list.append(ind)

                    if ind_list:
                        m = max(ind_list)
                        tagged_tuples = tagged_tuples[m+1::]
                        tags_red = [tup[1] for tup in tagged_tuples]

                    parsed = cp_np.parse(tagged_tuples)
                    list_nps = [item for item in parsed if hasattr(item, 'label')==True]
                    last_tagged = tagged_tuples[-1][1]

                    if last_tagged == 'PRP':
                        row[2] = tagged_tuples[-1][0]
                        row[3] = tagged_tuples[-1][1]
                        row[4] = tagged_tuples[-1][1]
                        row[5] = tagged_tuples
                        row[6] = parsed
                        row[7] = 'CODE A'

                    elif last_tagged == 'CC':
                        row[2] = tagged_tuples[-1][0]
                        row[3] = tagged_tuples[-1][1]
                        row[4] = tagged_tuples[-1][1]
                        row[5] = tagged_tuples
                        row[6] = parsed
                        row[7] = 'CODE B'

                    elif last_tagged == 'WP':
                        row[2] = tagged_tuples[-1][0]
                        row[3] = tagged_tuples[-1][1]
                        row[4] = tagged_tuples[-1][1]
                        row[5] = tagged_tuples
                        row[6] = parsed
                        row[7] = 'CODE C'

                    elif last_tagged == 'TO': #and len(tagged_tuples) == 1:
                        row[2] = tagged_tuples[-1][0]
                        row[3] = tagged_tuples[-1][1]
                        row[4] = tagged_tuples[-1][1]
                        row[5] = tagged_tuples
                        row[6] = parsed
                        row[7] = 'CODE D'


                    else:
                        if len(parsed) == 1 and hasattr(parsed[-1], 'label') == True:
                            row[2] = tree_string(parsed[-1])
                            row[3] = get_pattern(parsed[-1])
                            row[4] = parsed[-1][0][1]
                            row[5] = tagged_tuples
                            row[6] = parsed
                            row[7] = 'CODE E'

                        elif len(parsed) > 1:
                            if 'and' in tokens_red:
                                for i4, j4 in enumerate(parsed):
                                    if hasattr(j4, 'label')==False and j4[1] == 'CC':
                                        if (hasattr(parsed[i4-1], 'label') == True and hasattr(parsed[i4+1], 'label') == True):
                                            if i4 > 2 or i4 == 2:
                                                if parsed[i4-2][1] != 'IN':
                                                    const1 = tree_string(parsed[i4-1])
                                                    const2 =  tree_string(parsed[i4+1])
                                                    s = const1 + ' ' + j4 + ' ' + const2
                                                    row[2] = s
                                                    row[3] = parsed[i4-1] +' '+ j4 + ' ' + parsed[i4+1]
                                                    row[4] = parsed[i4-1][0]
                                                    row[5] = tagged_tuples
                                                    row[6] = parsed
                                                    row[7] = 'CODE F'
                                            else:
                                                const1 = tree_string(parsed[i4-1])
                                                const2 =  tree_string(parsed[i4+1])
                                                print '\n\n'
                                                print 'const1', const1
                                                print 'const2', const2
                                                print 'j', j4
                                                print j is tuple
                                                print len(const1)
                                                print len(j4)
                                                print '\n\n'

                                                s = const1 + ' ' + j4 + ' ' + const2
                                                print 's', s
                                                row[2] = s
                                                row[3] = get_pattern(parsed[i4-1]) +' '+ j4 + ' ' + get_pattern(parsed[i4+1])
                                                row[4] = parsed[i4-1][0][1]
                                                row[5] = tagged_tuples
                                                row[6] = parsed
                                                row[7] = 'CODE G'


                            else:

                                list_nps = [item for item in parsed if hasattr(item, 'label')==True]

                                if len(list_nps) == 1:
                                    row[2] = tree_string(list_nps[0])
                                    row[3] = get_pattern(list_nps[0])
                                    row[4] = list_nps[0][0][1]
                                    row[5] = tagged_tuples
                                    row[6] = parsed
                                    row[6] = 'CODE H'

                                elif len(list_nps) > 1:
                                    ind_list_np = []
                                    list_np = []
                                    for i3, j3 in enumerate(parsed):
                                        try:
                                            if hasattr(j3, 'label') == True and parsed[i3-1][1]!='IN':
                                                ind_list_np.append(i3)
                                                list_np.append(j3)
                                        except:
                                            continue

                                    row[2] = tree_string(list_np[-1])
                                    row[3] = get_pattern(list_np[-1])
                                    row[4] = list_nps[0][0][1]
                                    row[5] = tagged_tuples
                                    row[6] = parsed
                                    row[7] = 'CODE I'

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            error = exc_type, fname, exc_tb.tb_lineno
            row[2] = 'ERROR'
            row[3] = ''
            row[4] = ''
            row[5] = tagged_tuples
            row[6] = parsed
            row[7] = error
        print '\n\n\n\n'

with open('part3/errors.csv', 'rb') as f:
    data=csv.reader(f)
    data2 = [row for row in data]
    subj_nps(data2, 'finished')

with open('part3/subjects_output3.csv', 'w' ) as f2:
    writer = csv.writer(f2)
    writer.writerows(data2)
