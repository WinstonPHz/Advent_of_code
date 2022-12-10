import dis

from intcode import computer
import copy
import os

def get_code(filename):
    code = []
    with open(filename) as file:
        for line in file:
            if line == "\n":
                break
            components = line.split(",")
            for value in components:
                code.append(int(value))
    return code

def day2():
    ## Day 02 Testing
    code = get_code("d02in.txt")
    code[1] = 12
    code[2] = 2
    c1 = computer(code)
    while True:
        out = c1.run_computer(1)
        if out == 99:
            break
    print("Answer for day 2 pt1 2692315:")
    print(">>", c1.address[0])

def day5():
    code = get_code("d05in.txt")
    c2 = computer(code)
    out = c2.run_computer(1)
    print("Answer for Day 5 Part 1: ")
    print("0 0 0 0 0 0 0 0 0 7259358 99\n>> ", end="")
    print(out, end = " ")
    while out != 99:
        out = c2.run_computer()
        print(out, end=" ")
    print()
    print("Answer for Day 5 Part 2: ")
    c2 = computer(code)
    out = c2.run_computer(5)
    print("Should be 11826654")
    print(">>", out)


def day9():
    code = get_code("d09in.txt")
    c1 = computer(code)
    out = c1.run_computer(1)
    print("Answer for Day 9 Part 1: ")
    print("2171728567 99\n>> ", end="")
    print(out, end = " ")
    while out != 99:
        out = c1.run_computer()
        print(out, end=" ")
    print()
    c2 = computer(code)
    out = c2.run_computer(2)
    print("Answer for Day 9 Part 2: ")
    print(f"49815\n>>{out}", end = "")

class display():
    def __init__(self, initial_state):
        x_max = tile_array[-1][0]
        y_max = tile_array[-1][1]
        game_display = []
        for j in range(y_max+1):
            game_display.append(copy.copy([0] * (x_max+1)))
        self.gd = copy.deepcopy(game_display)
        self.score = 0
        self.set_display(initial_state)
        self.length_of_array = len(initial_state)
        self.paddle_pos = 0
        self.ball_pos = 0
        self.user_input = 0

    def set_display(self, new_state):
        for tile in new_state:
            x = tile[0]
            y = tile[1]
            s = tile[2]
            if x == -1 and y == 0:
                self.score = s
                continue
            self.gd[y][x] = s
            if s == 3:
                self.paddle_pos = x
            if s == 4:
                self.ball_pos = x
        if self.paddle_pos < self.ball_pos:
            self.user_input = 1
        elif self.paddle_pos == self.ball_pos:
            self.user_input = 0
        elif self.paddle_pos > self.ball_pos:
            self.user_input = -1

    def show_display(self):
        os.system('cls')
        print(f"---------------{self.score}---------------")
        for row in self.gd:
            for val in row:
                if val == 0:
                    print(" ", end="")
                elif val == 1:
                    print("|", end="")
                elif val == 2:
                    print("#", end="")
                elif val == 3:
                    print("_", end="")
                elif val == 4:
                    print("O", end="")
            print()




code = get_code("d13in.txt")
c1 = computer(code)
tile_array = []
out = c1.run_computer()
tiles = []
while out != 99:
    tiles.append(out)
    if len(tiles) == 3:
        tile_array.append(tiles)
        tiles = []
    out = c1.run_computer()
tile_count = 0
for tile in tile_array:
    if tile[2] == 2:
        tile_count += 1

print("Ans1:", tile_count)

code[0] = 2
c2 = computer(code)
disp = display(tile_array)
j = 0
tile_array = []
tiles = []
while True:
    for i in range(3):
        out = c2.run_computer(disp.user_input)
        tiles.append(out)
    if [99,99,99] == tiles:
        disp.show_display()
        break
    disp.set_display([tiles])
    tiles = []
    j += 1
    if j % 60 == 0:
        disp.show_display()


