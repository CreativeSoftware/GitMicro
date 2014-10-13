import csv
import re

element = 266488

with open('material.txt', 'rt') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        if element == row[0]: # if the username shall be on column 3 (-> index 2)
            print "is in file"

with open('material.txt', 'rt') as f:
    reader = csv.reader(f, delimiter='\t') # good point by @paco
    for row in reader:
        for field in row:
            if field == element:
                print "is in file"
