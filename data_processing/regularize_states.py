import csv

with open('manual16.csv', 'r') as f1:
    data = csv.reader(f1)
    new_data = [row for row in data ]

with open('state_table.csv', 'r') as f1:
    data = csv.reader(f1)
    states_data = [row for row in data ]

for row in new_data:
    state = row[5]
    for abbr_row in states_data:
        abbr_state = abbr_row[2]
        if state == abbr_state:
            row[5] = abbr_row[1]
            
with open('manual17.csv', 'w' ) as f2:
    writer = csv.writer(f2)
    writer.writerows(new_data)
