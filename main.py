import csv

data = []
with open('data.csv', 'r') as csvfile:
    csvdata = csv.reader(csvfile, delimiter=',')
    for row in csvdata:
        print(row)
        data = row

with open('data.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerows(data)
