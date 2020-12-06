import os
from functools import reduce
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input')

input = open(filename, "r")

with open(filename) as f:
   count = sum(1 for _ in f)

repeats = count * 3

i = 0
j = 0
k = 0
l = 0
m = 0
ln = 0
trees = [0, 0, 0, 0, 0]

for line in input.readlines():
    line = line.strip()
    line = line * repeats

    # Right 1
    c = line[i]
    if c == "#":
        trees[0] += 1
    i += 1

    # Right 3
    c = line[j]
    if c == "#":
        trees[1] += 1
    j += 3

    # Right 5
    c = line[k]
    if c == "#":
        trees[2] += 1
    k += 5

    # Right 7
    c = line[l]
    if c == "#":
        trees[3] += 1
    l += 7

    if ln % 2 == 0:
        c = line[m]
        if c == "#":
            trees[4] += 1
        m += 1
    ln += 1

print(reduce((lambda x, y: x * y), trees))
