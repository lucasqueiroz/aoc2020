import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input')

input = open(filename, "r")

lines = input.readlines()

instructions = {}
acc = 0
i = 0

while i < len(lines):
    line = lines[i].strip()

    if i in instructions.get(line, []):
        break

    if instructions.get(line):
        instructions[line].append(i)
    else:
        instructions[line] = [i]

    if line.startswith("nop"):
        i += 1
        continue

    if line.startswith("acc"):
        line = line.replace("acc ", "")
        acc += int(line.strip())
        i += 1

    if line.startswith("jmp"):
        line = line.replace("jmp ", "")
        i += int(line.strip())

print(acc)
