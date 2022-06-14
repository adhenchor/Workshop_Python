import csv
import urllib.request

url = ('https://people.sc.fsu.edu/~jburkardt/data/csv/addresses.csv' 'r')
response = urllib.request.urlopen(url)
cr = csv.reader(response)

for rows in cr:
    print(rows)
