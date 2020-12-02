import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input')

input = open(filename, "r")

subtractions = {}

for line in input.readlines():
    int_line = int(line)
    subtractions[str(2020 - int_line)] = int_line

input.seek(0, 0)

for line in input.readlines():
    int_line = int(line)
    if str(int_line) in subtractions:
        print(int_line * subtractions[str(int_line)])
        break
