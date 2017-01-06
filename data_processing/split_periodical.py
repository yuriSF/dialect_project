import csv


with open('extracted_filtered15.csv', 'r') as f:
    data = csv.reader(f)
    ling_data = [row for row in data]

for ling in ling_data:
    if '(' in ling[3]:
        print ling[3]
        print ling[3].split('(')[0]
        ling[3] = ling[3].split(' (')[0]
        print ling[3]
        ling[3] = ling[3].strip()


with open('extracted_filtered16.csv', 'w') as f:
    a = csv.writer(f)
    a.writerows(ling_data)
