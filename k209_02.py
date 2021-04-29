import os

file = os.path.abspath("input.txt")
f = open(file, 'w')

f = open(file, 'w')
text = ""

while text != "exit":
    text = input("入力してください")
    f.write(text + "\n")
f.close()

