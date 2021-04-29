import os

file = os.path.abspath("test.txt")
f = open(file, 'r')
data = f.read()
f.close()
print(data)