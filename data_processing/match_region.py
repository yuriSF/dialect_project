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
		

main = open_csv('states_changed3.csv')
main = superlist(main)

main2 = open_csv('dialect_region.csv')
main2 = superlist(main2)


for row2 in main2:
	for row1 in main:
		if row2[0]==row1[2] and row2[1]==row1[1]:
			row1[8]=row2[2]
			row1[9]=row2[3]

with open('matched_regions2.csv', 'w') as f:
    a = csv.writer(f)
    a.writerows(main)

