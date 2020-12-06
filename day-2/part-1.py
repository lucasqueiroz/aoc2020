import os
import re

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input')

input = open(filename, "r")

valid = 0

for line in input.readlines():
    match = re.search(r"(\d+)-(\d+) (.+): (.+)", line)
    min, max, char, password = match.groups()
    count = password.count(char)
    if (count >= int(min) and count <= int(max)):
        valid += 1

print(valid)
