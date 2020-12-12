import os
import re
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input')

input = open(filename, "r")

class Group:

    def __init__(self):
        self.answers = []

    def add_answer(self, answer=""):
        self.answers.append(answer)

    def count_answers(self):
        total = 0
        all_answers = "".join(self.answers)
        for answer in self.answers:
            for ch in answer:
                if all_answers.count(ch) == len(self.answers):
                    total += 1
                    all_answers = all_answers.replace(ch, "")

        return total



current = ""

lines = input.readlines()
total = 0
current_group = Group()

for line in lines:
    if line == "\n":
        total += current_group.count_answers()
        current_group = Group()
    else:
        current_group.add_answer(line.strip())

print(total)
