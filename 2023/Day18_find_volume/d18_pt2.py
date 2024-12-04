class d18():
    def __init__(self):
        self.map = {}
        self.cur_location = [0, 0]
        self.instructions_1 = []
        self.instructions_2 = []
        self.blocks_x = {}
        self.blocks_y = {}


    def decode_color(self, color):
        number = int(color[2:-2], 16)
        dir = int(color[-2])
        self.instructions_2.append([dir, number])

    def add_line_p1(self, line):
        direction, amount, color = line.split(" ")
        self.decode_color(color)
        self.instructions_1.append([direction, amount])


    def print_map(self, to_print):
        for j, row in to_print.items():
            for char in row:
                print(end = char)
            print()

    def find_area(self, instructions):
        # Set up a set of x, y, points
        x_breaks = []
        y_breaks = []
        x, y = [0,0]
        for direction, ammount in instructions:
            ammount = int(ammount)
            if direction in ["R", 0]:
                x_breaks += [x-1, x, x+1, x+ammount, x+ammount+1, x+ammount-1]
                x += ammount
            elif direction in ["D", 1]:
                y_breaks += [y-1, y, y+1, y+ammount, y+ammount+1, y+ammount-1]
                y += ammount
            elif direction in ["L", 2]:
                x_breaks += [x+1, x, x-1, x-ammount, x-ammount+1, x-ammount-1]
                x -= ammount
            elif direction in ["U", 3]:
                y_breaks += [y+1, y, y-1, y-ammount, y-ammount+1, y-ammount-1]
                y -= ammount
        x_breaks = list(set(x_breaks))
        y_breaks = list(set(y_breaks))
        x_breaks.sort()
        y_breaks.sort()
        return self.find_area_2d(x_breaks, y_breaks, instructions)

    def find_area_2d(self, x_breaks, y_breaks, instructions):
        # Set up a 2d array that is NxM in size
        new_map = {}
        for j, number in enumerate(y_breaks):
            new_map[j] = ["0"] * len(x_breaks)
        # Set the paremiter to find the volume, Question Specific
        x, y = [0, 0]
        for direction, ammount in instructions:
            ammount = int(ammount)
            if direction in ["R", 0]:
                low = x
                high = x + ammount
                y_index = y_breaks.index(y)
                for i, num in enumerate(x_breaks):
                    if low <= num <= high:
                        new_map[y_index][i] = "1"
                x += ammount
            elif direction in ["D", 1]:
                low = y
                high = y + ammount
                x_index = x_breaks.index(x)
                for i, num in enumerate(y_breaks):
                    if low <= num <= high:
                        new_map[i][x_index] = "1"
                y += ammount
            elif direction in ["L", 2]:
                low = x - ammount
                high = x
                y_index = y_breaks.index(y)
                for i, num in enumerate(x_breaks):
                    if low <= num <= high:
                        new_map[y_index][i] = "1"
                x -= ammount
            elif direction in ["U", 3]:
                low = y - ammount
                high = y
                x_index = x_breaks.index(x)
                for i, num in enumerate(y_breaks):
                    if low <= num <= high:
                        new_map[i][x_index] = "1"
                y -= ammount
        # Once the paremeter if found, find the volume
        volume_1 = 0
        for j, row in new_map.items():
            count = 0
            for i, char in enumerate(row):
                if char == "1":
                    dx = abs(x_breaks[i + 1] - x_breaks[i])
                    dy = abs(y_breaks[j + 1] - y_breaks[j])
                    volume_1 += dx * dy
                if j+1 >= len(y_breaks):
                    continue
                check_array = [str(new_map[j][i]), str(new_map[j+1][i])]
                if check_array == ["1", "1"]:
                    # Switch to inside the shape
                    count += 1
                    continue
                if check_array == ["1", "0"]:
                    # Don't count the tops twice
                    continue
                if count % 2:
                    dx = abs(x_breaks[i + 1] - x_breaks[i])
                    dy = abs(y_breaks[j + 1] - y_breaks[j])
                    volume_1 += dx * dy
                    new_map[j][i] = "."
        return volume_1

    def run(self):
        print("Answer 1:", self.find_area(self.instructions_1))
        print("Answer 2:", self.find_area(self.instructions_2))


puz_in = {}
obj = d18()
with open("input.txt", "r") as file:
    for j, line in enumerate(file):
        line = line.replace("\n", "")
        obj.add_line_p1(line)


obj.run()
