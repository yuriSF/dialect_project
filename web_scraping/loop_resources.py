import csv
import mechanize
import time


def make_link(resource):
    query = '''http://infoweb.newsbank.com''' + resource
    return query

def write_row(csv_file, row):
    with open(csv_file, 'a' ) as f2:
        writer = csv.writer(f2)
        writer.writerow(row)


with open('extracted_filtered19.csv', 'rb') as f:
    data=csv.reader(f)
    data2 = [row for row in data]

for ind, row in enumerate(data2):
    resource = row[0].split('''="''')[-1]
    resource = resource.replace('''"''', '')
    resource = resource.replace('''>''', '')
    link = make_link(resource)
    print link
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
    request = br.open(link)
    response = request.read()
    ind = ind + step
    html_file = 'resources/' + str(ind) + '.html'
    with open(html_file, 'w') as f:
        f.write(response)
        print 'wrote response %s' %(ind)
    br.close()
    time.sleep(1)
