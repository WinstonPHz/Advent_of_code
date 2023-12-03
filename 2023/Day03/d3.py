puz_string = []


with open("input.txt", "r") as file:
  for line in file:
    line = line.strip('\n')
    puz_string.append(line)


def parse_input(puz):
    grid = {}
    for j, line in enumerate(puz):
        grid[j] = []
        for i, char in enumerate(line):
            grid[j].append(char)
    return grid

class part1():
    def __init__(self, matrix):
        self.grid = matrix
        self.sum_part_number = 0
        self.part2_ans = 0
        self.number = "0,1,2,3,4,5,6,7,8,9".split(",")

    def count_number(self, x, y):
        while True:
            if self.grid[y][x] in self.number:
                x -= 1
                continue
            if x < 0:
                x += 1
                break
            if self.grid[y][x] not in self.number:
                x += 1
                break
        num_string = ""
        while True:
            num_string += self.grid[y][x]
            self.grid[y][x] = "."
            x += 1
            if x >= len(self.grid[y]):
                break
            if self.grid[y][x] not in self.number:
                break
        return int(num_string)

    def look_around(self, x, y, char):
        test_tables = [[-1, -1], [-1, 0], [-1, 1],
                       [0, -1],           [0, 1],
                       [1, -1], [1, 0],   [1, 1]]
        found = []
        for dx, dy in test_tables:
            nx = x + dx
            ny = y + dy
            if not (0 <= nx <= len(self.grid[0])):
                continue
            if not (0 <= ny <= len(self.grid.keys())):
                continue
            if self.grid[ny][nx] in self.number:
                found.append(self.count_number(nx, ny))
        self.sum_part_number += sum(found)
        if char == "*":
            if len(found) == 2:
                self.part2_ans += found[0]*found[1]

    def scan_grid(self):
        symbols = "1,2,3,4,5,6,7,8,9,0,.".split(",")
        for y, row in enumerate(self.grid.keys()):
            row = self.grid[y]
            for x, char in enumerate(row):
                if char not in symbols:
                    self.look_around(x, y, char)

a = part1(parse_input(puz_string))
a.scan_grid()
print("Answer 1 :", a.sum_part_number)
print("Answer 2 :", a.part2_ans)







