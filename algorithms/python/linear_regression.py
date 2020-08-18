#Regression algorithm in python
#This algorithm uses Gradient Descent to optimize itself ✨✨

import csv


with open('/mnt/c/Users/sidha/Desktop/hello-world/algorithms/python/rand.csv', mode='r') as file:
    csv_reader = csv.reader(file,delimiter=',')
    line_count = 0
    for row in csv_reader:
        print(row[0],row[1],sep='\t')
        line_count += 1
