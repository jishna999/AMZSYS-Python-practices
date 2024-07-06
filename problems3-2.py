# Problem 2: Write a program extcount.py to count number of files for each extension in the given directory.
# The program should take a directory name as argument and print count and extension for each available file extension.

import glob
import sys

tifCounter = len(glob.glob1(sys.argv[1],"*.tif"))
print(tifCounter)