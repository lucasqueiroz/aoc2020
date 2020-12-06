import os
import re
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input')

input = open(filename, "r")

current = ""

lines = input.readlines()
last = lines[-1]
valid = 0

for line in lines:
    if line == last:
        current = line

    if line == "\n" or line == last:
        regex = r".*(?=.*pid:)(?=.*byr:)(?=.*iyr:)(?=.*eyr:)(?=.*hgt:)(?=.*hcl:)(?=.*ecl:).*"
        if re.match(regex, current):
            valid += 1
        current = ""
    else:
        current += line.strip()

print(valid)
