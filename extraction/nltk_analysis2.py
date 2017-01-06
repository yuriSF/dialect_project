import csv
import nltk
from nltk import tokenize
tokenizer = nltk.data.load('nltk:tokenizers/punkt/english.pickle')
from nltk.tokenize import sent_tokenize
nltk.help.upenn_tagset()

grammar = "NP: {<PDT>?<DT>?<WDT>?<PRP\$>?<CD>?<JJ>*<JJS>*<JJR>*<NN>?<NNS>?<NNPS>?<NNP>?}"
cp = nltk.RegexpParser(grammar)
parsed = cp.parse(tagged_tuples)

with open('extracted_filtered14.csv', 'r') as f:
    data = csv.reader(f)
    data2 = [row for row in data]

for row in data2:
    target = row[1]
    sentlist = sent_tokenize(target)
    for sent in sentlist:
        if 'done' in sent or 'finished' in sent:
            tokens = nltk.word_tokenize(sent)
            for i, j in enumerate(tokens):
                cop_list = ['am', 'is', 'are', 'was', 'were', 'be']
                if j=='done' or j=='finished' and tokens[i-1] in cop_list:
                    clipped = tokens[i+1:]
                    adv_nouns = ['day', 'season', 'year', 'week', 'month', 'way']
                    tagged_tuples = nltk.pos_tag(clipped)
                    verb_list = ['VB', 'VBZ', 'VBP', 'VBD', 'MD']
                    if (clipped[0]=='the' or clipped[0]=='that' or clipped[0]=='this') and clipped[1] in adv_nouns:
                        row[6] = 'misfit'
                        print  'misfit ', sent
                    elif clipped[1] == 'time' or clipped[2] == 'time':
                        row[6] = 'misfit'
                    elif tagged_tuples[0][0] == 'that' and tagged_tuples[1][1] in verb_list:
                        row[6]='misfit'
                    elif tagged_tuples[0][0]=='-' or tagged_tuples[0][0]==',':
                        row[6] = 'misfit'
                    elif parsed[0][0] == 'that' and str(parsed[1])[1] == 'N' and str(parsed[1])[2] == 'P':
                        row[6] = 'misfit'
                    elif parsed[0][0] == 'that' and parsed[1][1] == 'PRP':
                        row[6] = 'misfit'
