from bible import Bible
import os

file = os.path.abspath("bible.txt")
f = open(file, 'r')
data = f.read()

print(data)