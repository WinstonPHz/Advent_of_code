import math
import copy
class part1():
    def __init__(self, map):
        self.raw_map = map
        self.ans_2 = 0

    def find_min(self, pos_list):
        cur_low = 10000
        for key, item in pos_list.items():
            if item < cur_low:
                cur_low = item
        for key, item in pos_list.items():
            if item == cur_low:
                return key, item

    def get_wall(self, current_node, next_node):
        next = self.raw_map[next_node[1]][next_node[0]]
        dx = next_node[0] - current_node[0]
        dy = next_node[1] - current_node[1]
        if dy != 0:
            if dy > 0:
                if next in "-,7,F".split(","):
                    return False
            else:
                if next in "-,L,J".split(","):
                    return False
        if dx != 0:
            if dx > 0:
                if next in "|,L,F".split(","):
                    return False
            else:
                if next in "|,7,J".split(","):
                    return False
        if next == ".":
            return False
        return True

    def get_connecting(self, x, y):
        all_connecting = [[x + 1, y], [x, y + 1], [x - 1, y], [x, y - 1]]
        cur = self.raw_map[y][x]
        if   cur == "-":
            return [[x-1, y], [x+1, y]]
        elif cur == "|":
            return [[x, y-1], [x, y+1]]
        elif cur == "F":
            return [[x, y+1], [x+1, y]]
        elif cur == "J":
            return [[x, y-1], [x-1, y]]
        elif cur == "7":
            return [[x-1, y], [x, y+1]]
        elif cur == "L":
            return [[x, y-1], [x+1, y]]
        elif cur == "S":
            return all_connecting

    def propigate(self, start):
        abs_min = {}
        cur_pos = copy.copy(start)
        abs_min[tuple(cur_pos)] = 0
        pos_min = {}
        dist_from_origin = 0
        x_max = len(self.raw_map[0])
        y_max = len(self.raw_map.keys())
        while True:
            x = cur_pos[0]
            y = cur_pos[1]
            connecting_nodes = self.get_connecting(x, y)
            for nx, ny in connecting_nodes:
                if 0 <= nx < x_max and 0 <= ny < y_max:
                    # Make sure the connecting node is in the graph
                    if self.get_wall([x, y], [nx, ny]):
                        # Is this a wall?
                        if tuple([nx, ny]) not in pos_min.keys() and tuple([nx, ny]) not in abs_min.keys():
                            # Have we been here before? No then:
                            pos_min[tuple([nx, ny])] = dist_from_origin + 1
                        elif tuple([nx, ny]) in pos_min.keys():
                            # We have been there, is this one better?
                            if pos_min[tuple([nx, ny])] > dist_from_origin + 1:
                                # This one is better lets add it to the list
                                pos_min[tuple([nx, ny])] = dist_from_origin + 1
            # Now lets get our next check point
            cur_pos, dist_from_origin = self.find_min(pos_min)
            # Our next check point is the lowest to that point
            abs_min[cur_pos] = dist_from_origin
            # We dont want to come back here
            del pos_min[cur_pos]
            if not pos_min:
                self.path = abs_min
                return abs_min

    def print_map(self, hm):
        print()
        for j in self.raw_map.keys():
            for i, char in enumerate(self.raw_map[j]):
                if tuple([i,j]) in hm.keys():
                    tp = f"{hm[tuple([i,j])]}"
                    print(end = tp[-1])
                    continue
                print(end = f"{char}")
            print()

    def in_loop(self, x, y):
        crosses = 0
        nx = x-1
        ny = y
        x_max = len(self.raw_map[0])
        y_max = len(self.raw_map.keys())
        while True:
            # Only Going left FL7J-|
            if 0 <= nx < x_max and (0 <= ny < y_max and 0 <= ny+1 < y_max):
                if tuple([nx,ny]) in self.heat_map.keys():
                    cur_icons = [self.raw_map[ny][nx], self.raw_map[ny+1][nx]]
                    #print(crosses, cur_icons, " ", end = "")
                    if cur_icons[0] == "|":
                        crosses += 1
                    elif cur_icons == ["F", "J"]:
                        crosses += 1
                    elif cur_icons == ["F", "L"]:
                        crosses += 1
                    elif cur_icons == ["F", "|"]:
                        crosses += 1
                    elif cur_icons == ["7", "|"]:
                        crosses += 1
                    elif cur_icons == ["7", "L"]:
                        crosses += 1
                    elif cur_icons == ["7", "J"]:
                        crosses += 1
            else:
                return crosses % 2
            nx -= 1

    def find_inside(self, hm):
        self.heat_map = hm
        for j in self.raw_map.keys():
            for i, char in enumerate(self.raw_map[j]):
                if tuple([i,j]) not in self.heat_map.keys():
                    if self.in_loop(i, j):
                        self.ans_2 += 1




map = {}
start = []
with open("input.txt", "r") as file:
    for j, line in enumerate(file):
        map[j] = []
        line = line.replace("\n", "")
        for i, char in enumerate(line):
            if char == "S":
                start = [i, j]
                map[j].append("J")
                continue
            map[j].append(char)

obj = part1(map)
heat_map = obj.propigate(start)
all_values = []
for key, value in heat_map.items():
    all_values.append(value)
obj.find_inside(heat_map)
print("Answer 1 :", max(all_values))
print("Answer 2 :", obj.ans_2)

# 34 is not correct