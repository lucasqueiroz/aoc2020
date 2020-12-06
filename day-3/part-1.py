import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input')

input = open(filename, "r")

with open(filename) as f:
   count = sum(1 for _ in f)

repeats = count * 3

i = 0
trees = 0

for line in input.readlines():
    line = line.strip()
    line = line * repeats
    c = line[i]
    if c == "#":
        trees += 1
    i += 3

print(trees)
