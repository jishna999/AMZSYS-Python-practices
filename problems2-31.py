# Problem 31: Generalize the above implementation of csv parser to support any delimiter and comments.

import csv
def parse_csv(file, delimiter=',', comment='#'):
    with open(file, mode="r") as csvfile:
        reader = csv.reader(csvfile, delimiter=delimiter)
        p=[row for row in reader]
    return p
file = 'E:\\a.csv'
parse = parse_csv(file, delimiter=',', comment='#')
print(parse)