import csv

def open_csv(file):
	f = open(file, 'rU')
	data = csv.reader(f)
	return data

def superlist(data):
	list=[]
	for row in data:
		list.append(row)
	return list
		
main1 = open_csv('dialect-features-cleaned2.csv')
main1 = superlist(main1)

main2 = open_csv('final_stats13.csv')
main2 = superlist(main2)


n=0
for row1 in main1:
	for row2 in main2:
		if row1[3] == row2[3] and row1[4] == row2[4] and row2[5]=='x':
			print row1[3]
			print row2[4]
			print ''
			print row2[5]
			row2[5]=row1[5]
			row2[6]=row1[6]
			row2[7]=row1[7]
			n=n+1

print n

with open('final_stats14.csv', 'w') as f:
    a = csv.writer(f)
    a.writerows(main2)
