import os
import re
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input')

input = open(filename, "r")

class Bag:
    def __init__(self):
        self.holders = []

    def add_bag(self, bag, times):
        for _ in range(0, times):
            self.holders.append(bag)

    def total_bags(self, bags):
        total = len(self.holders)
        for holder in self.holders:
            total += bags[holder].total_bags(bags)

        return total


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
        bag = bags[bag_color]
        if contains == "no other bags.":
            continue
        contains = contains.split(", ")
        for contain in contains:
            regex = r"(\d+) (.*) (?:bag|bags)"
            match = re.match(regex, contain.replace(".", ""))
            if match:
                times = int(match.group(1))
                color = match.group(2)
                bag.add_bag(color, times)

print(bags["shiny gold"].total_bags(bags))

