from copy import copy

class cups():
    def __init__(self):
        self.walls = []
        self.x_point = []
        self.y_point = []
        self.sand = []
        with open("input.txt", "r") as file:
            for line in file:
                line = line.strip("\n")
                cordinates = line.split(" -> ")
                for i in range(len(cordinates)-1):
                    sx1, sy1 = cordinates[i].split(",")
                    sx2, sy2 = cordinates[i+1].split(",")
                    dx = [int(sx1), int(sx2)]
                    dx.sort()
                    dy = [int(sy1), int(sy2)]
                    dy.sort()
                    for x in range(dx[0], dx[1]+1):
                        for y in range(dy[0], dy[1]+1):
                            if [x,y] not in self.walls:
                                self.walls.append([x, y])
                                self.x_point.append(x)
                                self.y_point.append(y)

            self.x_range = [min(self.x_point) - 1, max(self.x_point) + 2]
            self.y_range = [0, max(self.y_point) + 2]
            self.max_sand = 0
            self.num_walls = len(self.walls)


    def print_graph(self):
        print(self.x_range, self.y_range)
        for x in range(self.x_range[0], self.x_range[1]):
            print(x%10, end="")
        print()
        for y in range(self.y_range[0], self.y_range[1]):
            for x in range(self.x_range[0], self.x_range[1]):
                if [x,y] in self.walls:
                    print(end="#")
                elif [x,y] in self.sand:
                    print(end="O")
                elif [x,y] in self.path:
                    print(end="~")
                else:
                    print(end = ".")
            print(y)

    def sim_sand(self):
        # This is one sand falling from 500 down:
        sand_x = 500
        self.path = []
        for y in range(0, self.y_range[1]):
            below = y+1
            self.path.append([sand_x,y])
            if [sand_x, below] in self.sand+self.walls:
                # Something directly below
                if [sand_x-1, below] not in self.sand+self.walls:
                    # Nothing to the left, lets continue
                    sand_x -= 1
                    continue
                if [sand_x+1, below] not in self.sand+self.walls:
                    # Nothing to the right, lets continue
                    sand_x += 1
                    continue
                # If we get here can't go to the left or right so it stays where it is
                self.sand.append([sand_x, y])
                return

    def full_sim(self):
        while True:
            lenOld = len(self.sand)
            self.sim_sand()
            if lenOld == len(self.sand):
                self.print_graph()
                break
        print("Answer 1:", len(c.sand))


    def add_big_cup(self):
        for i in range(self.y_range[1]):
            self.walls.append([self.x_range[0] - 1, i])
            self.walls.append([self.x_range[1] + 1, i])

    def calc_max_sand(self):
        point_in_cur_line = [[500,0]]
        total_sand = 1
        for j in range(self.y_range[1]-1):
            next_points = []
            for px, py in point_in_cur_line:
                new_points = [[px-1, py+1], [px, py+1], [px+1, py+1]]
                for point in new_points:
                    if point not in self.walls+next_points:
                        next_points.append(point)
            point_in_cur_line = copy(next_points)
            total_sand += len(next_points)
        print("Ans 2:", total_sand)



# 26769 is too high
c = cups()
c.full_sim()
c.calc_max_sand()

