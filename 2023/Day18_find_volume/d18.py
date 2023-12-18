import math
from copy import deepcopy
import copy
import heapq
from functools import cache

class d18():
    def __init__(self):
        self.map = {}
        self.cur_location = [0, 0]
        self.min_x = 0
        self.max_x = 0
        self.min_y = 0
        self.max_y = 0

    def add_line(self, line):
        direction, amount, color = line.split(" ")
        for i in range(int(amount)):
            if direction == "R":
                self.cur_location[0] += 1
            elif direction == "L":
                self.cur_location[0] -= 1
            elif direction == "U":
                self.cur_location[1] -= 1
            elif direction == "D":
                self.cur_location[1] += 1
            if self.cur_location[1] not in self.map.keys():
                self.map[self.cur_location[1]] = {}

            self.map[self.cur_location[1]][self.cur_location[0]] = 1
        self.set_maxes()

    def set_maxes(self):
        x, y = self.cur_location
        if x < self.min_x:
            self.min_x = x
        if x > self.max_x:
            self.max_x =x
        if y > self.max_y:
            self.max_y = y
        if y < self.min_y:
            self.min_y = y


    def crosses(self, point, grid):
        x, y1, = point
        y2 = y1 + 1
        count = 0
        i = x
        y_max = max(grid.keys())
        while True:
            if y2 > y_max:
                return count
            check_array = [str(grid[y1][i]), str(grid[y2][i])]
            if check_array == ["1", "1"]:
                count += 1
            i -= 1
            if i < 0:
                return count


    def find_volume(self):
        new_map = {}
        ans_1 = 0
        for j, row in self.map.items():
            new_map[j] = [0] * (self.max_x+abs(self.min_x)+1)
            for i, value in row.items():
                new_map[j][i+abs(self.min_x)] = 1
        for j, row in new_map.items():
            for i, char in enumerate(row):
                if self.crosses([i, j], new_map)%2:
                    if str(new_map[j][i]) == "1":
                        continue
                    new_map[j][i] = "."
        for j, row in new_map.items():
            for char in row:
                if str(char) != "0":
                    ans_1 += 1
        return ans_1






puz_in = {}
obj = d18()
with open("input.txt", "r") as file:
    for j, line in enumerate(file):
        line = line.replace("\n", "")
        obj.add_line(line)


print(obj.map)

print("Answer 1:", obj.find_volume())


#15196