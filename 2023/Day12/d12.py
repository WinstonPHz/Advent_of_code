import math
import copy
from functools import cache


class part1():
    def __init__(self):
        self.ans_1 = 0
        self.ans_2 = 0

    def add_line(self, line):
        self.part_1_count = 0
        arangments = []
        order, arangements_string = line.split(" ")
        for num in arangements_string.split(","):
            arangments.append(int(num))
        self.ans_1 += self.go_deeper(order, tuple(arangments))
        p2_string = "?".join([order]*5)
        p2_arangments = arangments*5
        self.ans_2 += self.go_deeper(p2_string, tuple(p2_arangments))

    @cache
    def go_deeper(self, line, requirement, result = 0):
        if not requirement:
            # Add 1 if its a good line, no req lef and no # left is a good line
            return "#" not in line
        req, requirement = requirement[0], requirement[1:]
        # Increment over all possabilities for this requirement
        for i in range(len(line) - sum(requirement) - len(requirement) - req + 1):
            if "#" in line[:i]:
                # If there is a gear before this it is not an arragment
                break
            next_pos = i + req
            if not next_pos <= len(line):
                return result
            if "." in line[i:next_pos]:
                continue
            if line[next_pos:next_pos+1] != "#":
                result += self.go_deeper(line[next_pos+1:], requirement)
        return result

obj = part1()
with open("input.txt", "r") as file:
    for j, line in enumerate(file):
        line = line.replace("\n", "")
        obj.add_line(line)

print("Answer 1 :", obj.ans_1)
print("Answer 2 :", obj.ans_2)
