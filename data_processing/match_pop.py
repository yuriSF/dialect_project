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
		

main1 = open_csv('final_stats10.csv')
main1 = superlist(main1)

main2 = open_csv('pop_size2.csv')
main2 = superlist(main2)


for row1 in main1:
	for row2 in main2:
		if row1[1]==row2[1] and row1[2]==row2[0]:
			row1[10]=row2[2]
			print row1[10]
		

with open('final_stats11.csv', 'w') as f:
    a = csv.writer(f)
    a.writerows(main1)