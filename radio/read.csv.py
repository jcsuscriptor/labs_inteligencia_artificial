import csv
with open('foo.csv') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=',')
     for row in spamreader:
         print(', '.join(row))