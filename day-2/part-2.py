import os
import re

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input')

input = open(filename, "r")

valid = 0

for line in input.readlines():
    match = re.search(r"(\d+)-(\d+) (.+): (.+)", line)
    first, second, char, password = match.groups()
    first_char = password[int(first)-1]
    second_char = password[int(second)-1]
    if (first_char == char and not second_char == char) or (
        second_char == char and not first_char == char
    ):
        valid += 1

print(valid)
