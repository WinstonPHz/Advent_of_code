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


    def find_area(self, instructions):
        # Set up a set of x, y, points
        points = [[0,0]]
        x, y = [0,0]
        for direction, ammount in instructions:
            ammount = int(ammount)
            if direction in ["R", 0]:
                x += ammount
            elif direction in ["D", 1]:
                y += ammount
            elif direction in ["L", 2]:
                x -= ammount
            elif direction in ["U", 3]:
                y -= ammount
            points.append([x, y])
        return self.find_area_2d(points)

    def find_area_2d(self, points):
        # Set up a 2d array that is NxM in size
        volume = 0
        p1 = points.pop(0)
        p2 = points.pop(0)
        while points:
            x1, y1 = p1
            x2, y2 = p2
            volume += ((x1)*(y2)) - ((x2)*(y1)) + abs(x2-x1) + abs(y2-y1)
            p1 = p2
            p2 = points.pop(0)
        x1, y1 = p1
        x2, y2 = p2
        volume += (x1 * y2) - (x2 * y1) + abs(x2-x1) + abs(y2-y1)
        return int(volume/2) + 1

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
