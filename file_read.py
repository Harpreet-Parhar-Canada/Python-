# Reads array.js into Python as a variable/input

# Open in Read mode
# use f.read to rwad file data dn store it in variable
# Determine the number of lines in program and print/display to the user
import re

def read_lines():
    f = open('functions.js', 'r')
    contents = f.readlines()
    count = 0
    for x in contents:
        count = count + 1

    print(count)

read_lines()

# Method to determine how many else statements are in array.js file
def else_search():
    f = open('functions.js', 'r')
    contents = f.read()
    x = re.findall('else', contents)
    count = 0
    if(x):
        count = count + 1

    print(count)

else_search()

# Method to calculate the number of characters
def char_count():
    f = open('functions.js', 'r')
    contents = f.read()
    x = re.findall('[a-zA-Z]', contents)
    count = 0
    for x in contents:
        count = count + 1

    print(count)

char_count()


