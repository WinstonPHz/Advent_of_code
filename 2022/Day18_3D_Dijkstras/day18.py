import copy
class cubes():
    def __init__(self):
        self.cube_field = []
        self.surface_total = 0
        for i in range(22):
            grid1 = []
            for j in range(22):
                grid1.append(copy.deepcopy([0] * 22))
            self.cube_field.append(copy.deepcopy(grid1))
        around = []
        for i in range(-1, 2):
            if i == 0:
                continue
            around.append([0, 0, i])
            around.append([0, i, 0])
            around.append([i, 0, 0])
        self.around = around
        self.perim_total = 0

    def add_cube(self, x, y, z):
        # Have to add 1 to every number because there is lava on the edge
        self.cube_field[z+1][y+1][x+1] = 1

    def look_around(self):
        # Look at each point in the cube, if its a zero, look around it, each 1 is a surface
        # X, Y, Z
        for k, z_row in enumerate(self.cube_field):
            for j, y_row in enumerate(z_row):
                for i, x_row in enumerate(y_row):
                    if not x_row:
                        for dx, dy, dz in self.around:
                            x = i + dx
                            y = j + dy
                            z = k + dz
                            if x == 22 or y == 22 or z == 22:
                                continue
                            if self.cube_field[z][y][x]:
                                self.surface_total += 1
        print("Answer 1:", self.surface_total)

    def find_min(self, pos_list):
        cur_low = 5000
        for key, dist in pos_list.items():
            if len(dist) < cur_low:
                cur_low = len(dist)
        for key, dist in pos_list.items():
            if len(dist) == cur_low:
                return key, dist

    def propigate(self, start):
        abs_min = {}
        cur_pos = copy.copy(start)
        abs_min[tuple(cur_pos)] = [cur_pos]
        pos_min = {}
        dist_from_origin = []
        x_max = len(self.cube_field[0][0])
        y_max = len(self.cube_field[0])
        z_max = len(self.cube_field)
        while True:
            x = cur_pos[0]
            y = cur_pos[1]
            z = cur_pos[2]
            connecting_nodes = []
            for dx, dy, dz in self.around:
                x1 = x + dx
                y1 = y + dy
                z1 = z + dz
                connecting_nodes.append([x1,y1,z1])
            for nx, ny, nz in connecting_nodes:
                if 0 <= nx < x_max and 0 <= ny < y_max and 0 <= nz < z_max:
                    # Make sure the connecting node is in the graph
                    if not self.cube_field[nz][ny][nx]:
                        #Is this a wall? if no continue
                        if tuple([nx, ny, nz]) not in pos_min.keys() and tuple([nx, ny, nz]) not in abs_min.keys():
                            # Have we been here before? No then:
                            pos_min[tuple([nx, ny, nz])] = dist_from_origin + [[nx, ny, nz]]
                        elif tuple([nx, ny, nz]) in pos_min.keys():
                            # We have been there, is this one better?
                            if pos_min[tuple([nx, ny, nz])] > dist_from_origin:
                                # This one is better lets add it to the list
                                pos_min[tuple([nx, ny, nz])] = dist_from_origin + [[nx, ny, nz]]
            # Now lets get our next check point
            if pos_min == {}:
                return abs_min
            cur_pos, dist_from_origin = self.find_min(pos_min)
            # Our next check point is the lowest to that point
            abs_min[cur_pos] = dist_from_origin
            # We don't want to come back here
            del pos_min[cur_pos]

    def search_paremiter(self):
        all_perem_nodes = self.propigate([0,0,0])
        for i, j, k in all_perem_nodes:
            if self.cube_field[k][j][i]:
                print("Something is wrong here")
            for dx, dy, dz in self.around:
                x = i + dx
                y = j + dy
                z = k + dz
                if x == 22 or y == 22 or z == 22:
                    continue
                if self.cube_field[z][y][x]:
                    self.perim_total += 1
        print("Answer 2:", self.perim_total)


c = cubes()
with open("input.txt", "r") as file:
    for line in file:
        line = line.strip("\n")
        x, y, z = line.split(",")
        c.add_cube(int(x), int(y), int(z))

c.look_around()
c.search_paremiter()
