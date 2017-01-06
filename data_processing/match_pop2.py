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
		
def count_pop(target):
	location_list = []
	n=0
	for row1 in main1:	
		if row1[4]==target and row1[3] not in location_list:
				location_list.append(row1[3])
				n=n+int(row1[5])
	print '%s = %s' % (target, n)


main1 = open_csv('match_pop2.csv')
main1 = superlist(main1)
region_list=['North Midland', 'North', 'South', 'South Midland', 'West']

for region in region_list:
	count_pop(region)

			


exit()

with open('final_stats11.csv', 'w') as f:
    a = csv.writer(f)
    a.writerows(main1)