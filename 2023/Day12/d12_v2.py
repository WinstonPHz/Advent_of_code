import math
import copy
class part1():
    def __init__(self):
        self.part_1_count = 0
        self.ans_1 = 0
        self.part_2_count = 0
        self.ans_2 = 0

    def add_line(self, line):
        self.part_1_count = 0
        arangments = []
        order, arangements_string = line.split(" ")
        for num in arangements_string.split(","):
            arangments.append(int(num))
        self.go_deeper(order, arangments)
        self.ans_1 += self.part_1_count
        self.part2(order, arangments)

    def go_deeper(self, line, requirement):
        if "?" not in line:
            if self.partial_check(line, requirement):
                self.part_1_count += 1
            return
        dot_line = line.replace("?", ".", 1)
        self.go_deeper(dot_line, requirement)
        hash_line = line.replace("?", "#", 1)
        self.go_deeper(hash_line, requirement)

    def partial_check(self, line, requirement):
        got_one = False
        count_a = 0
        count_b = 0
        for char in line:
            if got_one:
                if char == ".":
                    got_one = False
                    if count_b >= len(requirement):
                        return False
                    if count_a != requirement[count_b]:
                        return False
                    count_a = 0
                    count_b += 1
                else:
                    count_a += 1
            else:
                if char == "#":
                    got_one = True
                    count_a += 1
        if char == "#":
            if count_b >= len(requirement):
                return False
            if count_a != requirement[count_b]:
                return False
            count_b += 1
        if count_b < len(requirement):
            return False
        return True

    def go_deeper_2(self, line, requirement):
        if "?" not in line:
            if self.partial_check(line, requirement):
                self.part_2_count += 1
            return
        dot_line = line.replace("?", ".", 1)
        self.go_deeper_2(dot_line, requirement)
        hash_line = line.replace("?", "#", 1)
        self.go_deeper_2(hash_line, requirement)

    def part2(self, line, requirement):
        self.part_2_count = 0
        line = line + "?" + line
        requirement = requirement*2
        self.go_deeper_2(line, requirement)
        if self.part_1_count == 1 and line[-1] == "#":
            self.ans_2 += 1
        else:
            self.ans_2 += int((self.part_1_count*(self.part_2_count/self.part_1_count)**4))







obj = part1()
with open("input.txt", "r") as file:
    for j, line in enumerate(file):
        line = line.replace("\n", "")
        obj.add_line(line)


print("Answer 1 :", obj.ans_1)
print("Answer 2 :", obj.ans_2)

