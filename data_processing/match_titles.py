import csv

with open('list_periodicals.csv', 'r') as f:
    data = csv.reader(f)
    per_data = [row for row in data]

with open('extracted_filtered16.csv', 'r') as f:
    data = csv.reader(f)
    ling_data = [row for row in data]

for ling in ling_data:
    for ind, per in enumerate(per_data):
        ling[3] = ling[3].strip()
        if ling[3] in per[0]:
            ling[4] = per_data[ind+1][0]
            ling[5] = per_data[ind+1][1]

with open('extracted_filtered17.csv', 'w') as f:
    a = csv.writer(f)
    a.writerows(ling_data)
