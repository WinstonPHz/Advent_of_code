import math
from copy import deepcopy
import copy
import heapq
from functools import cache

class d18():
    def __init__(self):
        self.map = {}
        self.cur_location = [0, 0]
        self.blocks_x = {}
        self.blocks_y = {}


    def decode_color(self, color):
        number = int(color[2:-2], 16)
        dir = int(color[-2])
        return number, dir

    def add_line_p1(self, line):
        direction, amount, color = line.split(" ")
        cur_x, cur_y = self.cur_location
        if direction in ["R", 0]:
            new_x = cur_x + int(amount)
            if cur_y not in self.blocks_x.keys():
                self.blocks_x[cur_y] = []
            self.blocks_x[cur_y].append([cur_x, new_x])
            self.cur_location[0] = new_x
        elif direction in ["L", 2]:
            new_x = cur_x - int(amount)
            if cur_y not in self.blocks_x.keys():
                self.blocks_x[cur_y] = []
            self.blocks_x[cur_y].append([new_x, cur_x])
            self.cur_location[0] = new_x
        elif direction in ["D", 1]:
            new_y = cur_y + int(amount)
            if cur_x not in self.blocks_y.keys():
                self.blocks_y[cur_x] = []
            self.blocks_y[cur_x].append([cur_y, new_y])
            self.cur_location[1] = new_y
        elif direction in ["U", 3]:
            new_y = cur_y - int(amount)
            if cur_x not in self.blocks_y.keys():
                self.blocks_y[cur_x] = []
            self.blocks_y[cur_x].append([new_y, cur_y])
            self.cur_location[1] = new_y

    def find_bounding_boxes(self):
        print(self.blocks_x)
        print(self.blocks_y)




puz_in = {}
obj = d18()
with open("input.txt", "r") as file:
    for j, line in enumerate(file):
        line = line.replace("\n", "")
        obj.add_line_p1(line)


print(obj.find_bounding_boxes())

print("Answer 1:")


#15196