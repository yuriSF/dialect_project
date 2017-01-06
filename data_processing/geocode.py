import geopy
from geopy.geocoders import Nominatim
import csv

with open('manual25.csv', 'r') as f1:
    data = csv.reader(f1)
    data2 = [row for row in data ]

    
for row in data2:
    geolocator = Nominatim()
    target = row[2]+' '+row[3]
    location = geolocator.geocode(target)
    print location.latitude, location.longitude
    row[5] = location.latitude
    row[6] = location.longitude

with open('manual27.csv', 'w' ) as f2:
    writer = csv.writer(f2)
    writer.writerows(data2)
