import math
from copy import deepcopy
import copy
import heapq
from functools import cache

class d17():
    def __init__(self, hash_map, max_x, max_y):
        self.map = hash_map
        self.max_x = max_x
        self.max_y = max_y
        self.min_path = []
        self.best_goal = max_x*100+max_y*100
        #self.goal = [max_x, max_y]
        self.goal = [0,0]

    def look_around(self, position):
        around_me = [[1, 0, 0], [0, 1, 1], [-1, 0, 2], [0, -1, 3]]
        to_look = []
        for dx, dy, direction in around_me:
            nx = position[0] + dx
            ny = position[1] + dy

            if 0 <= nx <= self.max_x and 0 <= ny <= self.max_y:
                to_look.append([nx, ny, direction])
        return to_look

    def man_dist_end(self, location):
        return abs(location[0] - self.goal[0]) + abs(location[1] - self.goal[1])

    def dfs(self, current_location, cur_heat, past_steps, direction = -1, count = 0):
        #print(current_location, cur_heat, past_steps)
        past_steps = deepcopy(past_steps)
        x, y = current_location
        past_steps.append([x, y])
        if current_location == self.goal:
            if cur_heat < self.best_goal:
                print("Got", cur_heat, "old", self.best_goal)
                self.best_goal = cur_heat
            self.print_path(past_steps)
            return
        cur_heat += self.map[y][x]
        where_to_look = self.look_around([x, y])
        next_moves = []
        for nx, ny, next_direction in where_to_look:
            cur_count = count
            if [nx, ny] in past_steps:
                continue
            if next_direction == direction:
                next_count = cur_count + 1
            else:
                next_count = 0
            if next_count > 2:
                continue
            next_heat = self.map[ny][nx]
            heapq.heappush(next_moves, (self.man_dist_end([nx, ny]) + cur_heat + next_heat, [nx, ny], next_direction, next_count))
        while next_moves:
            check, nm, next_direction, next_count = heapq.heappop(next_moves)
            #print(next_moves)
            self.dfs(nm, cur_heat, deepcopy(past_steps), next_direction, next_count)

    def print_path(self, path):
        for j, row in self.map.items():
            print()
            for i, char in enumerate(row):
                if [i, j] in path:
                    print(end = ".")
                else:
                    print(char, end = "")
        print()

puz_in = {}
with open("input.txt", "r") as file:
    for j, line in enumerate(file):
        line = line.replace("\n", "")
        to_append = []
        for i, char in enumerate(line):
            to_append.append(int(char))
        puz_in[j] = to_append

obj = d17(puz_in, i, j)
obj.dfs([i,j], 0, [])

print("Answer 1:", obj.best_goal)