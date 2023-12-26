import heapq
from functools import cache
from copy import deepcopy

class d23():
    def __init__(self, map, xmax, ymax):
        self.raw_map = map
        self.xmax = xmax
        self.ymax = ymax
        self.goal = [xmax-1, ymax]
        self.possible_paths = []
        self.lpp = {}
        self.nodes = []
        self.connections ={}
        self.nodes.append(self.goal)
        self.nodes.append([1, 0])
        self.ans_2 = 0

    def look_around(self, position):
        around_me = [[1, 0, 0], [0, 1, 1], [-1, 0, 2], [0, -1, 3]]
        to_look = []
        for dx, dy, direction in around_me:
            nx = position[0] + dx
            ny = position[1] + dy
            to_look.append([nx, ny, direction])
        return to_look


    def find_longest_path(self, current_position, cur_path = []):
        while True:
            if current_position not in cur_path:
                cur_path.append(current_position)
            if current_position == self.goal:
                self.possible_paths.append(len(cur_path)-2) # one for off grid start, one for start
                #self.print_path(cur_path)
                return
            possible_steps = self.look_around(current_position)
            to_look = []
            count = 0
            for step in possible_steps:
                x, y, dir = step
                if y < 0:
                    continue
                if self.raw_map[y][x] == "#":
                    continue
                if [x, y] in cur_path:
                    continue
                count += 1
                if dir == 0 and self.raw_map[y][x] == "<":
                    continue
                if dir == 1 and self.raw_map[y][x] == "^":
                    continue
                if dir == 2 and self.raw_map[y][x] == ">":
                    continue
                if dir == 3 and self.raw_map[y][x] == "v":
                    continue
                to_look.append([x, y])
            if (current_position not in self.nodes) and count >= 2:
                self.nodes.append(current_position)
            if len(to_look) == 1:
                current_position = to_look[0]
                continue

            for step in to_look:
                self.find_longest_path(step, deepcopy(cur_path))
            return

    def find_node_connections(self, current_position, starting_node, cur_path = []):
        cur_path = deepcopy(cur_path)
        while True:
            if current_position not in cur_path:
                cur_path.append(tuple(current_position))

            if current_position in self.nodes and current_position != starting_node:
                if tuple(starting_node)    not in self.connections.keys():
                    self.connections[tuple(starting_node)] = []
                if current_position + [len(cur_path)-1] not in self.connections[tuple(starting_node)]:
                    self.connections[tuple(starting_node)].append(current_position + [len(cur_path)-1])
                if tuple(current_position) not in self.connections.keys():
                    self.connections[tuple(current_position)] = []
                if starting_node + [len(cur_path)-1] not in self.connections[tuple(current_position)]:
                    self.connections[tuple(current_position)].append(starting_node + [len(cur_path)-1])
                return

            possible_steps = self.look_around(current_position)
            to_look = []
            for step in possible_steps:
                x, y, dir = step
                if not(0 <= y <= self.ymax):
                    continue
                if self.raw_map[y][x] == "#":
                    continue
                if tuple([x, y]) in cur_path:
                    continue
                to_look.append([x, y])
            if len(to_look) == 1:
                current_position = to_look[0]
                continue
            for step in to_look:
                self.find_node_connections(step, starting_node, deepcopy(cur_path))
            return

    def search_nodes(self, current_node, path = set(), distance = 0):
        if current_node == tuple(self.goal):
            if distance > self.ans_2:
                self.ans_2 = distance
            return
        for x, y, l in self.connections[current_node]:
            if (x, y) not in path:
                self.search_nodes((x,y), path|{(x,y)}, distance + l)


    def part2(self):
        self.dynamic_programing = {}
        for node in self.nodes:
            self.find_node_connections(node, node)
        for key, value in self.connections.items():
            print(key, "connects to", value)
        self.search_nodes((1,0))
        print("Answer 2:", self.ans_2)


    def print_path(self, path):
        count = 0
        for j, row in self.raw_map.items():
            print()
            for i, char in enumerate(row):
                if [i, j] in path:
                    print(end = "O")
                else:
                    print(char, end = "")
        print()
        print(len(path))

map = {}
with open("input.txt", "r") as file:
    for j, line in enumerate(file):
        line = line.replace("\n", "")
        map[j] = []
        for i, char in enumerate(line):
            map[j].append(char)

obj = d23(map, i, j)
obj.find_longest_path(tuple([1,-1]))
print("Answer 1:", max(obj.possible_paths))
obj.part2()
