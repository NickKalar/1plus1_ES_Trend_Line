import numpy
import csv


numpy.random.normal()
data = []

with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        data.append(row)

for row in data:
    print(row)