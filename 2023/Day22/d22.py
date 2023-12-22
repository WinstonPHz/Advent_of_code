import heapq
from functools import cache
from copy import deepcopy
class d22():
    def __init__(self):
        self.bricks = {}
        self.brick_heap = []
        self.supported = {}
        self.brick_locations = {}
        self.size = 10
        self.safes = []

    def add_brick(self, location):
        side_a, side_b = location.split("~")
        ax, ay, az = side_a.split(",")
        bx, by, bz = side_b.split(",")
        a_side = [int(ax), int(ay), int(az)]
        b_side = [int(bx), int(by), int(bz)]
        heapq.heappush(self.brick_heap, (min([a_side[2],b_side[2]]), a_side, b_side))

    def run(self):
        self.filter_area = {}
        block_id = 1
        while self.brick_heap:
            starting_z, a_side, b_side = heapq.heappop(self.brick_heap)
            self.lay_brick(a_side, b_side, block_id)
            self.supported[block_id] = {}
            block_id += 1

    def lay_brick(self, a_side, b_side, block_id):
        dx = abs(a_side[0]-b_side[0]) + 1
        dy = abs(a_side[1]-b_side[1]) + 1
        dz = abs(a_side[2]-b_side[2]) + 1
        low_x = min(a_side[0], b_side[0])
        low_y = min(a_side[1], b_side[1])
        low_z = min(a_side[2], b_side[2])
        high_z = max(a_side[2], b_side[2])
        for k in range(0, high_z+1):
            if k not in self.filter_area.keys():
                self.filter_area[k] = {}
                y = {}
                for j in range(self.size):
                    y[j] = [0] * self.size
                self.filter_area[k] = deepcopy(y)
        for k in range(low_z, 0, -1):
            if self.check_below([low_x, low_y, k], dx, dy):
                self.place_brick([low_x, low_y, k], dx, dy, dz, block_id)
                return

    def check_below(self, location, dx, dy):
        # if nothing below return False
        # return True if this is the end location of the brick
        if location[2] - 1 <= 0:
            return True
        locations = []
        for y in range(dy):
            for x in range(dx):
                lx = x + location[0]
                ly = y + location[1]
                locations.append([lx, ly, location[2]])
        blocks_below = []
        for x, y, z in locations:
            blocks_below.append(self.filter_area[z-1][y][x])
        for below in blocks_below:
            if below != 0:
                return True
        return False

    def place_brick(self, location, dx, dy, dz, block_id):
        locations = []
        for z in range(dz):
            for y in range(dy):
                for x in range(dx):
                    lx = x + location[0]
                    ly = y + location[1]
                    lz = z + location[2]
                    locations.append([lx, ly, lz])
        self.brick_locations[block_id] = locations
        for i, j, k in locations:
            if self.filter_area[k][j][i] != 0:
                print("Block", block_id, "is not where it should be", self.filter_area[k][j][i])
            self.filter_area[k][j][i] = block_id


    def print_z(self, z):
        for row in self.filter_area[z].values():
            print()
            for char in row:
                print(char, end = "")
        print("\n", z)

    def get_supported(self):
        self.supported = {}
        for brick_id, locations in self.brick_locations.items():
            supports = []
            supported = []
            for x, y, z in locations:
                if z > 1:
                    below = self.filter_area[z - 1][y][x]
                else:
                    below = 0
                above = self.filter_area[z + 1][y][x]
                if brick_id != self.filter_area[z][y][x]:
                    print("THERE IS AN ISSUE LAYING BRICKS")
                    print(brick_id, "should be where", self.filter_area[z][y][x], "is" )
                if brick_id != above:
                    if above != 0 and above not in supports:
                        supports.append(above)
                if brick_id != below:
                    if below != 0 and below not in supported:
                        supported.append(below)
            self.supported[brick_id] = {"supports": supports, "supported": supported}

    def count_removable_bricks(self):
        ans_1 = []
        for brick_id, values in self.supported.items():
            if self.is_removable(brick_id):
                if brick_id not in ans_1:
                    ans_1.append(brick_id)
        self.safes = ans_1
        print("Answer 1:", len(ans_1))

    def is_removable(self, brick_id):
        values = self.supported[brick_id]
        removable = False
        if len(values["supports"]) == 0:
            return True
        for value in values["supports"]:
            removable = True
            if len(self.supported[value]["supported"]) == 1:
                removable = False
                break
        return removable


    @cache
    def count_tumble_bricks(self, check_stable, fallen = []):
        crumbled = []
        for supported_brick in self.supported[check_stable]["supports"]:
            if len(self.supported[supported_brick]["supported"]) == 1:
                crumbled.append(supported_brick)
                continue
            crumbelable = True
            for under_above in self.supported[supported_brick]["supported"]:
                if under_above in fallen:
                    continue
                crumbelable = False
            if crumbelable:
                crumbled.append(supported_brick)
        fallen = list(set(crumbled+fallen))
        for next_brick in crumbled:
            fallen = self.count_tumble_bricks(next_brick, fallen)
        return list(set(fallen))

    def run2(self):
        ans_2 = 0
        for brick_id in self.brick_locations:
            ans_2 += len(self.count_tumble_bricks(brick_id))
        print("Answer 2:", ans_2)


map = {}
start = []
obj = d22()
with open("input.txt", "r") as file:
    for j, line in enumerate(file):
        line = line.replace("\n", "")
        obj.add_brick(line)

obj.run()
obj.get_supported()
obj.count_removable_bricks()
obj.run2()

# HIGH 531

