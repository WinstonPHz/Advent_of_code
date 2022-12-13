import copy
class map():
    def __init__(self):
        self.raw_map = []
        self.start = [0,0]
        self.end = [0,0]
        self.cur_height = 0
        codex = "abcdefghijklmnopqrstuvwxyz"
        self.decode = {}
        for i, c in enumerate(codex):
            self.decode[c] = i+1
        with open("input.txt", "r") as file:
            j = 0
            for line in file:
                line = line.strip("\n")
                row = []
                for i, char in enumerate(line):
                    if char == "E":
                        self.end = [i, j]
                        row.append(25+1)
                        continue
                    if char == "S":
                        self.start = [i, j]
                        row.append(0)
                        continue
                    row.append(self.decode[char])

                self.raw_map.append(copy.copy(row))
                j += 1

    def printmap(self):
        for row in self.raw_map:
            print(row)

    def find_min(self, pos_list):
        cur_low = 10000
        for key, item in pos_list.items():
            if item < cur_low:
                cur_low = item
        for key, item in pos_list.items():
            if item == cur_low:
                return key, item

    def get_wall(self, current_node, next_node):
        a = self.raw_map[current_node[1]][current_node[0]]
        b = self.raw_map[next_node[1]][next_node[0]]
        return b <= a + 1


    def propigate(self, start, end):
        abs_min = {}
        cur_pos = copy.copy(start)
        abs_min[tuple(cur_pos)] = 0
        pos_min = {}
        dist_from_origin = 0
        x_max = len(self.raw_map[0])
        y_max = len(self.raw_map)
        while True:
            x = cur_pos[0]
            y = cur_pos[1]
            connecting_nodes = [[x+1, y], [x, y+1], [x-1, y], [x, y-1]]
            for nx, ny in connecting_nodes:
                if 0 <= nx < x_max and 0 <= ny < y_max:
                    # Make sure the connecting node is in the graph
                    if self.get_wall([x,y], [nx, ny]):
                        #Is this a wall?
                        if tuple([nx, ny]) not in pos_min.keys() and tuple([nx, ny]) not in abs_min.keys():
                            # Have we been here before? No then:
                            pos_min[tuple([nx, ny])] = dist_from_origin + 1
                        elif tuple([nx, ny]) in pos_min.keys():
                            # We have been there, is this one better?
                            if pos_min[tuple([nx, ny])] > dist_from_origin+1:
                                # This one is better lets add it to the list
                                pos_min[tuple([nx, ny])] = dist_from_origin+1
            # Now lets get our next check point
            cur_pos, dist_from_origin = self.find_min(pos_min)
            # Our next check point is the lowest to that point
            abs_min[cur_pos] = dist_from_origin
            # We dont want to come back here
            del pos_min[cur_pos]
            if cur_pos == tuple(end):
                # Found it!
                return dist_from_origin

    def part1(self):
        new =  a.propigate(self.start, self.end)
        print("Ans 1:", new)
        return new

    def part2(self, p1):
        old = p1
        for i in range(40):
            self.start = [0,i]
            new = a.propigate(self.start, self.end)
            if new <= old:
                old = new
        print("Ans 2:", old)

a = map()
b = a.part1()
a.part2(b)
