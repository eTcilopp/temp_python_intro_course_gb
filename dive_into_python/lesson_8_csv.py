import csv

with open('biostats.csv', 'r', newline='') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        print(row)
