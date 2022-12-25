import copy
class elf_map():
    def __init__(self):
        self.map = {}
        self.number_of_elves = 0
        with open("input.txt", "r") as file:
            for j, line in enumerate(file):
                line = line.strip("\n")
                row = {}
                for i, char in enumerate(line):
                    row[i] = char
                    if char == "#":
                        self.number_of_elves += 1
                self.map[j] = row
        self.xbound = [0, len(self.map[0])]
        self.ybound = [0, len(self.map)]
        self.check = {
            0: [[-1,-1], [0,-1], [1,-1]],
            3: [[1,-1],  [1,0],  [1,1]],
            1: [[1,1],   [0,1],  [-1,1]],
            2: [[-1,1],  [-1,0], [-1,-1]]
        }
        self.check_suround = [[-1,-1], [0,-1], [1,-1],[1,0],[1,1],[0,1],[-1,1],[-1,0]]
        self.cur_check_dir = 0
        self.itterations = 0
        self.number_moving_to = {}


    def see_move(self, actually_move = False):
        move_map = {}
        non_move_count = 0
        for j, row in self.map.items():
            for i, char in row.items():
                if char == "#":
                    do_move = False
                    for dx, dy in self.check_suround:
                        x = i + dx
                        y = j + dy
                        if y not in self.map.keys():
                            continue
                        if x not in self.map[y].keys():
                            continue

                        if self.map[y][x] == "#":
                            do_move = True
                            #print(f"{i},{j} it in contact with {x},{y}")
                            break
                    if do_move:
                        #print("We are moving")
                        for m in range(4):
                            check_dir = (self.cur_check_dir + m) % 4
                            to_move = True
                            for dx, dy in self.check[check_dir]:
                                x = i + dx
                                y = j + dy
                                if y not in self.map.keys():
                                    continue
                                if x not in self.map[y].keys():
                                    continue
                                if self.map[y][x] == "#":
                                    #print(f"Not moving {i},{j} in {check_dir} {x},{y} in way")
                                    to_move = False
                                    break
                            if to_move:
                                dx, dy = self.check[check_dir][1]
                                x = i + dx
                                y = j + dy
                                if tuple([x, y]) not in move_map:
                                    move_map[tuple([x,y])] = []
                                move_map[tuple([x, y])].append([i,j])
                                break
                    else:
                        non_move_count += 1
        self.number_moving_to = move_map
        return non_move_count

    def actually_move(self):
        #print("actually Moving")
        move_map = self.number_moving_to
        #print(move_map)
        for moving_to, elf_from in move_map.items():
            if len(elf_from) > 1:
                continue
            #print(f"Moving {elf_from} to {moving_to}")
            elf_from = elf_from[0]
            if moving_to[1] not in self.map.keys():
                self.map[moving_to[1]] = {}
            self.map[moving_to[1]][moving_to[0]] = "#"
            self.map[elf_from[1]][elf_from[0]] = "."
            #print(moving_to[1])
        self.number_moving_to = {}
        return

    def rum_sim(self):
        self.itterations = 0
        while True:

            nmc = self.see_move()
            self.actually_move()
            self.cur_check_dir += 1
            self.itterations += 1
            if nmc == self.number_of_elves:
                print("Answer 2:", self.itterations)
                break
            if self.itterations == 10:
                self.get_answer_1()

    def print_graph(self):
        print()
        for y, row in self.map.items():
            for x, char in row.items():
                print(end=f"{char}")
            print()


    def get_answer_1(self):
        x_min = 5
        x_max = 5
        y_min = 5
        y_max = 5
        for y, row in self.map.items():
            for x, char in row.items():
                if char == "#":
                    if x < x_min:
                        x_min = x
                    if x > x_max:
                        x_max = x
                    if y < y_min:
                        y_min = y
                    if y > y_max:
                        y_max = y

        print("answer 1:", abs(x_max+1-x_min)*abs(y_max+1-y_min)-self.number_of_elves)
        return

ef = elf_map()
ef.rum_sim()
