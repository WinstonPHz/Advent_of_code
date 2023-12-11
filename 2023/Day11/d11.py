import math
import copy
class part1():
    def __init__(self, map):
        self.added_x = []
        self.added_y = []
        self.file = map
        self.expand_map_x()
        self.expand_map_y()
        self.ans_1 = 0
        self.ans_2 = 0


    def expand_map_y(self):
        to_add = []
        for j, line in self.file.items():
            if "#" not in line:
                to_add.append(j)
        self.added_y = to_add

    def expand_map_x(self):
        y_expanded = self.file
        to_add = []
        for i in range(len(y_expanded[0])):
            test_line = []
            for j in range(len(list(y_expanded.keys()))):
                test_line.append(y_expanded[j][i])
            if "#" not in test_line:
                to_add.append(i)
        self.added_x = to_add

    def manhatten_dist_n(self, start, end, n):
        x1, y1 = start
        x2, y2 = end
        to_add = 0
        for x in self.added_x:
            if x1 > x2:
                if x2 <= x <= x1:
                    to_add += 1
            else:
                if x1 <= x <= x2:
                    to_add += 1
        for y in self.added_y:
            if y1 > y2:
                if y2 <= y <= y1:
                    to_add += 1
            else:
                if y1 <= y <= y2:
                    to_add += 1

        l = abs(x2-x1)
        w = abs(y2-y1)
        return l+w + (n-1)*to_add

    def find_pt1(self):
        galaxies = []
        for j in self.file.keys():
            for i, char in enumerate(self.file[j]):
                if char == "#":
                    galaxies.append([i, j])
        for gal1 in galaxies:
            for gal2 in galaxies:
                if gal1 == gal2:
                    continue
                self.ans_1 += self.manhatten_dist_n(gal1, gal2, 2) # empty rows are 2 times larger
                self.ans_2 += self.manhatten_dist_n(gal1, gal2, 1000000) # empty rows are 1M times larger


map = {}
added_y = []
with open("input.txt", "r") as file:
    for j, line in enumerate(file):
        line = line.replace("\n", "")
        map[j] = []
        for char in line:
            map[j].append(char)

obj = part1(map)
obj.find_pt1()
print("Answer 1 :", int(obj.ans_1/2))
print("Answer 2 :", int(obj.ans_2/2))

# 15248332 to low
