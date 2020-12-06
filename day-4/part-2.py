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
        regex = r".*(?=.*pid:\d{9}(?:$|\n|\D|[bieh]))"
        regex += r"(?=.*byr:(?:200[0-2]|19[2-9][0-9]))"
        regex += r"(?=.*iyr:20(?:1[0-9]|20))"
        regex += r"(?=.*eyr:20(?:2[0-9]|30))"
        regex += r"(?=.*hgt:(?:1(?:[5-8][0-9]|9[0-3])cm|(?:59|6[0-9]|7[0-6])in))"
        regex += r"(?=.*hcl:#[0-9a-f]{6}[\D^a-f\n]?)"
        regex += r"(?=.*ecl:(?:amb|blu|brn|gry|grn|hzl|oth)[\D\n]?).*"
        if re.match(regex, current):
            valid += 1
        current = ""
    else:
        current += line.strip()

print(valid)
