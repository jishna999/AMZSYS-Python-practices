# Problem 3: Write a program to list all the files in the given directory along with their length and last
# modification time. The output should contain one line for each file containing filename,
# length and modification date separated by tabs.

# Hint: see help for os.stat.

import os
from pathlib import Path
import sys
path_file = Path(sys.argv[1])
status = os.stat(path_file)
print(status)
