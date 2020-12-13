import os
import re
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input')

input = open(filename, "r")

class Bag:
    def __init__(self):
        self.holders = []

    def add_bag(self, bag):
        self.holders.append(bag)

    def can_hold_bag(self, all_bags):
        for holder in self.holders:
            if (
                holder == "shiny gold" or
                all_bags[holder].can_hold_bag(all_bags)
            ):
                return True
        return False


lines = input.readlines()

bags = {}

for line in lines:
    regex = r"(.*) bags contain .*"
    match = re.match(regex, line)
    if match:
        bag_color = match.group(1)
        bags[bag_color] = Bag()

for line in lines:
    regex = r"(.*) bags contain (.*)"
    match = re.match(regex, line)
    if match:
        bag_color = match.group(1)
        contains = match.group(2)
        if contains == "no other bags.":
            continue
        contains = contains.split(", ")
        for contain in contains:
            regex = r"(?:\d+) (.*) (?:bag|bags)"
            match = re.match(regex, contain.replace(".", ""))
            if match:
                color = match.group(1)
                bag = bags[bag_color]
                bag.add_bag(color)

total = 0

for _, v in bags.items():
    if v.can_hold_bag(bags):
        total += 1

print(total)

