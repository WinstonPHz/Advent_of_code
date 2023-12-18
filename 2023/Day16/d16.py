import math
from copy import deepcopy
class d14():
    def __init__(self, hash_map):
        self.max_x = None
        self.map = hash_map
        self.ben_to = [] # [x, y, heading]
        self.light_map = {}
        self.heat_map = {}
        self.read_map()
        self.total_heat = 0

    def read_map(self):
        self.heat_map = {}
        for j, line in enumerate(self.map):
            self.heat_map[j] = []
            self.light_map[j] = []
            for i, char in enumerate(line):
                self.heat_map[j].append(0)
                self.light_map[j].append(char)
        self.max_x = i
        self.max_y = j

    def propigate_beam(self, x, y, heading, total_heat = 0):
        if tuple([x, y, heading]) in self.ben_to:
            return total_heat
        self.ben_to.append(tuple([x, y, heading]))
        nx = x
        ny = y
        for i in range(len(self.map[0])):
            if heading == 0:
                nx += 1
            elif heading == 1:
                ny += 1
            elif heading == 2:
                nx -= 1
            elif heading == 3:
                ny -= 1
            if not (0 <= nx <= self.max_x and 0 <= ny <= self.max_y):
                # Off the edge case
                return
            self.heat_map[ny][nx] = 1
            # Check the needed things
            if [nx, ny, heading] in self.ben_to:
                return
            if heading == 0:
                char = self.light_map[ny][nx]
                if char == "|":
                    self.propigate_beam(nx, ny, 1)
                    self.propigate_beam(nx, ny, 3)
                    return
                elif char == "/":
                    self.propigate_beam(nx, ny, 3)
                    return
                elif char == "\\":
                    self.propigate_beam(nx, ny, 1)
                    return
            elif heading == 1:
                char = self.light_map[ny][nx]
                if char == "-":
                    self.propigate_beam(nx, ny, 0)
                    self.propigate_beam(nx, ny, 2)
                    return
                elif char == "/":
                    self.propigate_beam(nx, ny, 2)
                    return
                elif char == "\\":
                    self.propigate_beam(nx, ny, 0)
                    return
            elif heading == 2:
                char = self.light_map[ny][nx]
                if char == "|":
                    self.propigate_beam(nx, ny, 3)
                    self.propigate_beam(nx, ny, 1)
                    return
                elif char == "/":
                    self.propigate_beam(nx, ny, 1)
                    return
                elif char == "\\":
                    self.propigate_beam(nx, ny, 3)
                    return
            elif heading == 3:
                char = self.light_map[ny][nx]
                if char == "-":
                    self.propigate_beam(nx, ny, 2)
                    self.propigate_beam(nx, ny, 0)
                    return
                elif char == "/":
                    self.propigate_beam(nx, ny, 0)
                    return
                elif char == "\\":
                    self.propigate_beam(nx, ny, 2)
                    return

    def get_heat(self):
        self.total_heat = 0
        for i, row in self.heat_map.items():
            self.total_heat += sum(row)


    def print_Heat(self):
        for j, row in self.heat_map.items():
            print()
            for i, char in enumerate(row):
                if char >= 1:
                    if self.light_map[j][i] in ["|", "-", "/", "\\"]:
                        print(end = self.light_map[j][i])
                    else:
                        print(end = f"{char}")
                else:
                    print(end = ".")
        print()


puz_in = []
ans_2 = []
with open("input.txt", "r") as file:
    for j, line in enumerate(file):
        line = line.replace("\n", "")
        puz_in.append(line)
obj = d14(puz_in)
obj.propigate_beam(-1, 0, 0)
obj.get_heat()
ans_2.append(obj.total_heat)
print("Ansewr 1:", obj.total_heat)
for j in range(obj.max_y):
    attempt_1 = d14(puz_in)
    attempt_1.propigate_beam(-1,j,0)
    attempt_1.get_heat()
    ans_2.append(attempt_1.total_heat)
    attempt_2 = d14(puz_in)
    attempt_2.propigate_beam(obj.max_y+1,j,2)
    attempt_2.get_heat()
    ans_2.append(attempt_2.total_heat)
for i in range(obj.max_x):
    attempt_1 = d14(puz_in)
    attempt_1.propigate_beam(i,-1,1)
    attempt_1.get_heat()
    ans_2.append(attempt_1.total_heat)
    attempt_2 = d14(puz_in)
    attempt_2.propigate_beam(i,obj.max_y+1,3)
    attempt_2.get_heat()
    ans_2.append(attempt_2.total_heat)
print("Ansewr 2:",max(ans_2))
