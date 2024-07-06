# Problem 4: Write a program to print directory tree.
# The program should take path of a directory as argument and print all the files in it recursively as a tree.

import os


def print_tree(dir_path, indent=""):
    for item in os.listdir(dir_path):
        full_path = os.path.join(dir_path, item)
        print(indent + item)
        if os.path.isdir(full_path):
            print_tree(full_path, indent + "  ")


if __name__ == "__main__":
    import sys

    path = sys.argv[1] if len(sys.argv) > 1 else "."
    print(path)
    print_tree(path)
