import csv


file = open('data/titanic.csv')
csv_file = csv.reader(file, delimiter=',')
for row in csv_file:
    print(row)

