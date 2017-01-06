
import nltk
#nltk.download()
nltk.help.upenn_tagset()
from nltk import tokenize
tokenizer = nltk.data.load('nltk:tokenizers/punkt/english.pickle')
from nltk.tokenize import sent_tokenize
import csv
import sys
import os
exit()

def get_string(tree):
    l = [item[0] for item in tree]
    l2 = ' '.join(l)
    return l2
    
def get_pattern(nounPhrase):
    l = [item[1] for item in nounPhrase]
    l2 = ' '.join(l)
    return l2

grammar_np = "NP: {<PDT | DT | WDT | PRP\$ | CD>* <RB>?<VBG|JJ|JJS|JJR>* <NN|NNP|NNS|NNPS|CD>* <POS>* <RB>? <VBG|JJ|JJS|JJR>* <NN|NNS|NNP|NNPS>* <POS>* <NN|NNP|NNS|NNPS> | <PRP> } "


with open('objects_output3.csv', 'rb') as f:
    data=csv.reader(f)    
    data2 = [row for row in data]

cp_np = nltk.RegexpParser(grammar_np)

for row in data2:
    line =  row[1]
    #print line
    tokens = nltk.word_tokenize(line)
    if row[2] == 'no NP found':
        try:        
            for i, j in enumerate(tokens):
                if j == 'finished' and tokens[i-1]=='have' or tokens[i-1]=='has' or tokens[i-1]=='had':
                    tokens_red = tokens[i+1::]
                    anaphList = ['I', 'we', 'you', 'he', 'she', 'it', 'they']
                    if tokens_red[0] in anaphList:
                        row[2] = tokens_red[0]
                    #print line
                    #print tokens_red
                    else:
                        tagged_red = nltk.pos_tag(tokens_red)
                        #print tagged_red
                        parsed = cp_np.parse(tagged_red)
            
                        if hasattr(parsed[0], 'label') == True:
                            #print parsed[0]
                            row[2] = parsed[0]
                            row[3] = get_string(parsed[0])
                            row[4] = get_pattern(parsed[0])
                            
                            if hasattr(parsed[1], 'label') == False and parsed[1][0] == 'of':
                                print line
                                print parsed
                                print parsed[0]
                                print 'FOUND', parsed[1][1]
                                # this is to catch postnominal modifiers
                            
                        else:
                            pass
                            row[2] = 'no NP found'
                    print ''
        except:
            row[2] = 'error'
            row[3] = 'error'
            row[4] = 'error'
            pass



with open('objects_output4.csv', 'w' ) as f2:
    writer = csv.writer(f2)
    writer.writerows(data2) 