import math
from copy import deepcopy
class d14():
    def __init__(self):
        self.maps = {}
        self.ans_1 = 0
        self.ans_2 = 0
        self.cycle_number = 1
        self.states = {}
        self.times_reaped = 0
        self.found = False

    def add_map(self, map):
        self.maps = map
        self.height = len(tuple(self.maps.keys()))
        self.width  = len(self.maps[0])
        if self.height != self.width:
            print("NOT SQUARE")
            quit()

    def calc_load(self):
        load = 0
        for j, row in self.maps.items():
            for i, char in enumerate(row):
                if char == "O":
                    load += self.height - j
        return load

    def push_north(self):
        for j, row in self.maps.items():
            for i, char in enumerate(row):
                if char == "O":
                    balls_up = 0
                    wall_at = 0
                    for y in range(j):
                        check_location = j - y - 1
                        char_at_check = self.maps[check_location][i]
                        if char_at_check == "O":
                            balls_up += 1
                        elif char_at_check == "#":
                            wall_at = check_location + 1
                            break
                    new_j = wall_at + balls_up
                    self.maps[j][i] = "."
                    self.maps[new_j][i] = "O"
                    continue

    def get_colmub(self, col_id):
        ret_row = []
        for row_id, row in self.maps.items():
            ret_row.append(row[col_id])
        return ret_row[::-1]

    def rotate_map(self):
        # Rotate map CCW
        new_map = {}
        for j, row in self.maps.items():
            new_map[j] = self.get_colmub(j)
        self.maps = deepcopy(new_map)

    def get_id(self):
        id_sum = 0
        for j, row in self.maps.items():
            for i, char in enumerate(row):
                if char == "O":
                    id_sum += i + 10000*j
        return id_sum

    def add_state(self):
        state_id = self.get_id()
        if state_id in self.states.keys():
            if not self.found:
                self.found = True
                first_cyle = self.states[state_id]
                print(state_id, first_cyle, self.cycle_number, self.states, 1000000000%(self.cycle_number-first_cyle))
                self.remaining_cyles = (1000000000-first_cyle)%(self.cycle_number-first_cyle)
            return
        else:
            self.states[state_id] = self.cycle_number

    def cycle(self):
        for i in range(4):
            self.push_north()
            self.rotate_map()
        self.cycle_number += 1

    def run(self):
        self.push_north()
        print("Answer 1 :", self.calc_load())
        self.rotate_map()
        self.remaining_cyles = 100000000
        for i in range(3):
            self.push_north()
            self.rotate_map()
        while self.remaining_cyles > 0:
            self.cycle()
            self.remaining_cyles -= 1
            self.add_state()
        print("Answer 2 :", self.calc_load())

in_map = {}
obj = d14()
row = []
with open("input.txt", "r") as file:
    for j, line in enumerate(file):
        row = []
        line = line.replace("\n", "")
        for char in line:
            row.append(char)
        in_map[j] = row
obj.add_map(in_map)
obj.run()

# High
# 102979
# 42710
