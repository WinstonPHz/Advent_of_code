import re
import copy

class forceField():
    def __init__(self):
        self.map = []
        self.commands = []
        self.heading = 0
        # X, Y
        self.start = [0,0]
        self.delta_move = [[1,0], [0,1], [-1,0], [0,-1]]
        with open("input.txt", "r") as file:
            commands_found = False
            start_found = False
            for line in file:
                if line == "\n":
                    commands_found = True
                    continue
                line = line.strip("\n")
                row = [" "]
                if not commands_found:
                    for i, char in enumerate(line):
                        if not start_found and char == ".":
                            start_found = True
                            self.start = [i+1,1]
                        row.append(char)
                    row.append(" ")
                    self.map.append(row)
                else:
                    for char in line:
                        self.commands.append(char)
        self.map = [[" "]*(len(self.map[0])+2)] + self.map
        self.map.append([" "]*len(self.map[-1]))
        self.path = {}

    def compress_commands(self):
        new_commandments = []
        integer = ""
        for i, char in enumerate(self.commands):
            if char != "L" and char != "R":
                integer += char
            if char == "L" or char == "R":
                if integer != "": new_commandments.append(int(integer))
                new_commandments.append(char)
                integer = ""
        if integer != "": new_commandments.append(int(integer))
        self.commands = new_commandments

    def extend_map(self):
        new_map = []
        max_x = len(self.map[0])
        for row in self.map:
            if max_x < len(row): max_x = len(row)
        for row in self.map:
            new_row = [" "] * (max_x+2)
            for i, char in enumerate(row):
                new_row[i] = char
            new_map.append(new_row)
        self.map = new_map

    def rotate(self, dir):
        if dir == "R":
            self.heading += 1
            if self.heading > 3:
                self.heading = 0
        elif dir == "L":
            self.heading -= 1
            if self.heading < 0:
                self.heading = 3

    def p1move(self, distance):
        dx, dy = self.delta_move[self.heading]
        old_x, old_y = self.start
        for i in range(distance):
            cur_x = old_x + dx
            cur_y = old_y + dy
            if self.map[cur_y][cur_x] == " ":
                while self.map[cur_y][cur_x] == " ":
                    if cur_x >= len(self.map[cur_y])-1:
                        cur_x = 0
                    elif cur_x < 0:
                        cur_x = len(self.map[cur_y])-1
                    if cur_y >= len(self.map)-1:
                        cur_y = 0
                    elif cur_y < 0:
                        cur_y = len(self.map)-1
                    cur_x += dx
                    cur_y += dy
            if self.map[cur_y][cur_x] == "#":
                self.start = [old_x, old_y]
                return
            old_x = cur_x
            old_y = cur_y
        self.start = [old_x, old_y]

    def get_answer(self):
        x, y = self.start
        print("Anwer>?", y, x, self.heading)
        ans = 1000*(y) + 4*(x) + self.heading
        print("answer", ans)


    def run(self):
        self.extend_map()
        self.compress_commands()
        for command in self.commands:
            if type(command) == type(0):
                self.p1move(command)
            else:
                self.rotate(command)
        self.get_answer()

    def run2(self):
        self.compress_commands()
        for command in self.commands:
            if type(command) == type(0):
                self.p2move(command)
            else:
                self.rotate(command)
        self.get_answer()

    def teleport(self, x, y, dir):
        zone_row = int((y-1)/50)
        zone_column = int((x-1)/50)
        print("Teleporting", x, y, dir, "zr", zone_row, "zc", zone_column)
        if zone_row == 0 and zone_column == 0:
            # XYZ
            # Only 1 border enters row 0 col 1
            new_dir = 0
            new_x = 1
            new_y = 151 - y
        elif zone_row == 2 and x == 0:
            # ZYX part 2
            new_dir = 0
            new_x = 51
            new_y = 51-y%50
            if y == 150:
                new_y = 1
        elif zone_row == 3 and x == 0:
            # RQP
            new_dir = 1
            new_x = y-100
            new_y = 1
        elif zone_row == 1 and zone_column == 0:
            # DEF all in same cube
            if dir == 2:
                # came from row 1 col 1
                new_dir = 1
                new_x = y - 50
                new_y = 101
            if dir == 3:
                # came from col 0 row 2
                new_dir = 0
                new_x = 51
                new_y = x + 50
        elif y == 0 and zone_column == 1:
            # RQP p2
            new_dir = 0
            new_x = 1
            new_y = 100 + x
        elif zone_row == 1 and zone_column == 2:
            # ABC
            if dir == 1:
                new_dir = 2
                new_x = 100
                new_y = x - 50
            if dir == 0:
                new_dir = 3
                new_x = y + 50
                new_y = 50
        elif zone_row == 3 and zone_column == 1:
            # GHI
            if dir == 1:
                new_dir = 2
                new_x = 50
                new_y = 100+x
            if dir == 0:
                new_dir = 3
                new_x = y-100
                new_y = 150
        elif zone_row == 2 and zone_column == 2:
            # ONM
            new_dir = 2
            new_x = 150
            new_y = 51-y%50
            if y == 150:
                new_y = 1
        elif zone_row == 0 and zone_column == 3:
            # ONM part 2
            new_dir = 2
            new_x = 100
            new_y = 151-y
        elif zone_row == 4 and zone_column == 0:
            # jkl
            new_dir = dir
            new_x = x + 100
            new_y = 1
        elif zone_column == 2 and y == 0:
            #jkl p2
            new_dir = dir
            new_x = x-100
            new_y = 200
        print(f"Teleported to {new_x} {new_y} {new_dir}")
        return new_x, new_y, new_dir

    def p2move(self, distance):
        print("Moving", distance, "in", self.heading)
        dx, dy = self.delta_move[self.heading]
        old_x, old_y = self.start
        old_heading = self.heading
        cur_heading = old_heading
        for i in range(distance):
            dx, dy = self.delta_move[old_heading]
            cur_x = old_x + dx
            cur_y = old_y + dy
            if self.map[cur_y][cur_x] == " ":
                cur_x, cur_y, cur_heading = self.teleport(cur_x, cur_y, old_heading)
            if self.map[cur_y][cur_x] == "#":
                print(f"hit a wall at {cur_x} {cur_y}")
                self.start = [old_x, old_y]
                self.heading = old_heading
                return
            self.path[tuple([cur_x, cur_y])] = cur_heading
            old_heading = cur_heading
            old_x = cur_x
            old_y = cur_y
        print("Ended at", old_x, old_y)
        self.heading = old_heading
        self.start = [old_x, old_y]

    def save_path(self):
        direction = {0:">", 1:"v", 2:"<", 3:"^"}
        with open("logs.txt", "w") as log:
            for y, row in enumerate(self.map):
                for x, col in enumerate(row):
                    if tuple([x, y]) in self.path:
                        log.write(direction[self.path[tuple([x,y])]])
                    else:
                        log.write(col)
                log.write("\n")




ff = forceField()
ff2 = forceField()
#ff.run()
ff2.extend_map()
ff2.run2()
ff2.save_path()

# too high 138400
# not right 135036
# too low 85238

