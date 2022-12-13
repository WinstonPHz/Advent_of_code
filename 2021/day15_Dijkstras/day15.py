class caves():
    def __init__(self):
        cavern = {}
        i = 0
        for line in open("puz", "r+"):
            line = line.strip("\n")
            cavern[i] = []
            for digit in line:
                cavern[i].append(int(digit))
            i += 1
        line_length = len(cavern[1])
        self.cave_system = cavern.copy()
        self.x_max = i
        self.y_max = line_length
        self.real_map = {}

    def printpritty(self, array):
        for key, value in array.items():
            print(key, value)

    def find_min(self, pos_list):
        cur_low = 10000
        for key, item in pos_list.items():
            if item < cur_low:
                cur_low = item
        for key, item in pos_list.items():
            if item == cur_low:
                return key, item

    def propigate(self, graph):
        abs_min = {}
        cur_pos = [0, 0]
        abs_min[tuple(cur_pos)] = 0
        pos_min = {}
        dist_from_origin = 0
        x_max = len(graph[0])
        y_max = len(graph)
        while True:
            x = cur_pos[0]
            y = cur_pos[1]
            connecting_nodes = [[x+1, y], [x, y+1], [x-1, y], [x, y-1]]
            for nx, ny in connecting_nodes:
                if 0 <= nx < x_max and 0 <= ny < y_max:
                    if tuple([nx, ny]) not in pos_min.keys() and tuple([nx, ny]) not in abs_min.keys():
                        pos_min[tuple([nx, ny])] = dist_from_origin + graph[nx][ny]
                    elif tuple([nx, ny]) in pos_min.keys():
                        if pos_min[tuple([nx,ny])] > dist_from_origin+graph[nx][ny]:
                            pos_min[tuple([nx, ny])] = dist_from_origin+graph[nx][ny]
            cur_pos, dist_from_origin = self.find_min(pos_min)
            abs_min[cur_pos] = dist_from_origin
            removed = pos_min.pop(cur_pos)
            if cur_pos == tuple([x_max-1, y_max-1]):
                return dist_from_origin

    def add_one(self, value):
        new_val = value + 1
        if new_val >= 10:
            new_val = 1
        return new_val

    def get_real_map(self, graph):
        new_map = graph.copy()
        for key, item in graph.copy().items():
            i = 0
            for digit in item:
                new_val = self.add_one(digit)
                new_map[key].append(new_val)
                i += 1
                if i > self.x_max*4 - 1:
                    break
        for i in range(self.x_max, self.x_max*5):
            new_map[i] = []
            for digit in new_map[i-self.x_max]:
                new_map[i].append(self.add_one(digit))
        self.real_map = new_map.copy()

cs = caves()
print(cs.x_max, cs.y_max)
print("Ans 1:", cs.propigate(cs.cave_system))
cs.get_real_map(cs.cave_system)
print("Ans 2:", cs.propigate(cs.real_map))
