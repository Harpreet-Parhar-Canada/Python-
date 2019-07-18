import re

f = open("functions.js", "r")
src = f.read()
f.close()

scriptReadingElse = re.findall("else", src)
print(scriptReadingElse)

scriptReadingCharacters = re.findall("[a-z]", src)
print(scriptReadingCharacters)

