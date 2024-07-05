# Problem 17: Write a program reverse.py to print lines of a file in reverse order.
import sys
def rev_file(f1):
    f = open(f1, 'r')
    lines = f.readlines()
    print(lines)
    fs = open(sys.arg[1], 'w')
    fs.writelines(lines[::-1])


rev_file(sys.argv[0])