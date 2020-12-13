import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input')

input = open(filename, "r")

current = ""

lines = input.readlines()
last = len(lines) - 1
total = 0
i = 0

for line in lines:
    if line == "\n" or i == last:
        total += len(set(current.strip()))
        current = ""
    else:
        current += line.strip()

    i += 1

print(total)
