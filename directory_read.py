# Python program to:
# - read files and sizes from directory
# - print a nice little report that tells us the number of files and total size of directory

import os

def print_name():
    basepath = '/Users/ian/Documents/EvolveU/JavaScript'
    count = 0
    for entry in os.listdir(basepath):
        if os.path.isfile(os.path.join(basepath, entry)):
            count = count + 1
    return count

def file_size():
    basepath = '/Users/ian/Documents/EvolveU/JavaScript'
    total = 0
    with os.scandir(basepath) as dir_contents:
        for entry in dir_contents:
            info = entry.stat()
            total = total + info.st_size
    return total


def report():
    print(f" Total # of files in /Users/ian/Documents/EvolveU/JavaScript: {print_name()}, Total Size of /Users/ian/Documents/EvolveU/JavaScript: {file_size()} bytes")


report()








