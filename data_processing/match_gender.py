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
		

main1 = open_csv('towns_changed2.csv')
main1 = superlist(main1)

main2 = open_csv('dialect features.csv')
main2 = superlist(main2)

for row2 in main2:
	for row1 in main1:
		if row2[0]==row1[0]:
			#print row2[0]
			#print row2[1], row1[5]
			row1[5]=row2[1] 
			#print row1[5]
			row1[6]=row2[2]
			row1[7]=row2[3]
			print row1


with open('matched_gender.csv', 'w') as f:
    a = csv.writer(f)
    a.writerows(main1)

