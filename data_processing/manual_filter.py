import csv
import nltk
from nltk import tokenize
from nltk.tokenize import sent_tokenize

be_list = ['be', 'am', 'is', 'are', 'was', 'were']
time_list = ['way', 'season', 'year', 'weak', 'month', 'fall', 'spring', 'winter', 'summer']

def write_row(csv_file, row):
    with open(csv_file, 'a' ) as f2:
        writer = csv.writer(f2)
        writer.writerow(row) 

with open('resources_whole10.csv', 'rb') as f:
    data=csv.reader(f)    
    data2 = [row for row in data]
    data3 = data2[411::]

for ind, row in enumerate(data3):
    stimulus = row[7]
    if 'done' in row[7]:
        stimulus=stimulus.replace('done', 'DONE')
    elif 'finished' in row[7]:
        stimulus=stimulus.replace('finished', 'FINISHED')
    print ind, stimulus
    print ''
    user = raw_input('1 for yes or 0 for n:  ')
    if user == '1':
        write_row('manual15.csv', row)
        print 'sentence ADDED'
        print ind, 'out of ', len(data3), ' completed'
        print float(ind+1)/float(len(data3)) * 100, '% completed'
        print ''
    elif user == '0':
        pass
        print 'sentence REJECTED'
        print ''
    else:
        print "INVALID INPUT"
        print ''
    
    
    

