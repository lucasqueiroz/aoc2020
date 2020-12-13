import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input')

input = open(filename, "r")

lines = input.readlines()

instructions = {}
acc = 0
i = 0
j = 0

def terminates_with_lines(updated_lines):
    ran = {}
    k = 0
    while k < len(updated_lines) - 1:
        line = updated_lines[k].strip()

        if k in ran.get(line, []):
            return False

        if ran.get(line):
            ran[line].append(k)
        else:
            ran[line] = [k]

        if line.startswith("jmp"):
            line = line.replace("jmp ", "")
            k += int(line.strip())

        k += 1

    return True


while i < len(lines):
    acc = 0

    line = lines[i].strip()

    if line.startswith("nop"):
        line = line.replace("nop", "jmp")
    elif line.startswith("jmp"):
        line = line.replace("jmp", "nop")

    lines_copy = lines.copy()
    lines_copy[i] = line

    terminates = terminates_with_lines(lines_copy)

    if terminates:
        while j < len(lines_copy):
            line = lines_copy[j].strip()

            if j in instructions.get(line, []):
                break

            if instructions.get(line):
                instructions[line].append(j)
            else:
                instructions[line] = [j]

            if line.startswith("nop"):
                j += 1
                continue

            if line.startswith("acc"):
                line = line.replace("acc ", "")
                acc += int(line.strip())
                j += 1

            if line.startswith("jmp"):
                line = line.replace("jmp ", "")
                j += int(line.strip())

    if terminates:
        break

    i += 1

print(acc)
