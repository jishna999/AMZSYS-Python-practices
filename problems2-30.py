# Problem 30: Write a python function parse_csv to parse csv (comma separated values) files.


import csv

def parse_csv(file):    
    print(open(file).read())
    with open(file,mode="r") as csvfile:        
        reader=csv.reader(csvfile)
        p=[row for row in reader]
    return p
file='a.csv'
parsed=parse_csv(file)
print(parsed)