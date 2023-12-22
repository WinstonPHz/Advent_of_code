import heapq
from functools import cache
class d21():
    def __init__(self, hash_map, xmax, ymax):
        self.map = hash_map
        self.max_x = xmax
        self.max_y = ymax
    def look_around(self, position):
        around_me = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        to_look = []
        for dx, dy in around_me:
            nx = position[0] + dx
            ny = position[1] + dy
            to_look.append([nx, ny])
        return to_look

    @cache
    def dijk(self, start, steps, offset = 1):
        avaialable_moves = []
        heapq.heappush(avaialable_moves, (0, start))
        visited = set()
        count = []
        return_count = 0
        while True:
            if not avaialable_moves:
                return count, return_count
            distance, best_move = heapq.heappop(avaialable_moves)
            x, y = best_move
            if distance > steps:
                return count, return_count
            if (distance + offset) % 2:
                if tuple(best_move) not in count:
                    count.append(tuple(best_move))
                    return_count += 1
            if (tuple(best_move)) in visited:
                continue
            visited.add(tuple(best_move))
            where_to_look = self.look_around([x,y])
            next_moves = []
            for nx, ny in where_to_look:
                if ny not in self.map.keys():
                    continue
                if not (0 <= nx <= self.max_x):
                    continue
                if self.map[ny][nx] == "#":
                    continue

                next_moves.append([nx, ny])
            for nm in next_moves:
                next_distance = distance + 1
                heapq.heappush(avaialable_moves, (next_distance, nm))

    def print_path(self, path):
        count = 0
        for j, row in self.map.items():
            print()
            for i, char in enumerate(row):
                if tuple([i, j]) in path:
                    print(end = "O")
                    count += 1
                else:
                    print(char, end = "")
        print()


map = {}
start = []
with open("input.txt", "r") as file:
    for j, line in enumerate(file):
        line = line.replace("\n", "")
        map[j] = []
        for i, char in enumerate(line):
            if char == "S":
                start = [i,j]
            map[j].append(char)

obj = d21(map, i, j)
girth = i + 1
path, a = obj.dijk(tuple(start), 64, 1)
print("Answer 1:", a)
new_steps = 26501365
edge_offset_a = (int(new_steps - start[0])+1) % 2
edge_offset_b = (int(new_steps - start[0])) % 2
#
remainder = ((new_steps - start[0]) % girth)
if remainder == 0:
    remainder = girth

# Tips
left_most_path, lm_a   = obj.dijk(tuple([i, start[1]]), remainder, edge_offset_a)
top_most_path,  tm_a   = obj.dijk(tuple([start[0], i]), remainder, edge_offset_a)
right_most_path, rm_a  = obj.dijk(tuple([0, start[1]]), remainder, edge_offset_a)
bottom_most_path, bm_a = obj.dijk(tuple([start[0], 0]), remainder, edge_offset_a)
# Edges A
left_up, lu_a           = obj.dijk(tuple([i, i]), remainder-girth/2, edge_offset_a)
left_down, ld_a         = obj.dijk(tuple([i, 0]), remainder-girth/2, edge_offset_a)
right_up, ru_a          = obj.dijk(tuple([0, i]), remainder-girth/2, edge_offset_a)
right_down, rd_a        = obj.dijk(tuple([0, 0]), remainder-girth/2, edge_offset_a)
# Edges B
left_up_b, lu_b         = obj.dijk(tuple([i, i]), remainder+girth/2, edge_offset_b)
left_down_b, ld_b       = obj.dijk(tuple([i, 0]), remainder+girth/2, edge_offset_b)
right_up_b, ru_b        = obj.dijk(tuple([0, i]), remainder+girth/2, edge_offset_b)
right_down_b, rd_b      = obj.dijk(tuple([0, 0]), remainder+girth/2, edge_offset_b)

# inners
inner_0, i = obj.dijk(tuple(start), girth*2, 0)
inner_1, j = obj.dijk(tuple(start), new_steps, 1)

# Math time
n = int(new_steps/girth)
number_1 = (n)**2
number_0 = (n-1)**2
number_edges = n
print("number of edge tiles", number_edges, "n0", number_0 , "n1", number_1)
ans_2 = 0
ans_2 += number_edges*(lu_a + ld_a + ru_a + rd_a) + (number_edges-1)*(lu_b + ld_b + ru_b + rd_b)
ans_2 += number_0*i
ans_2 += number_1*j
ans_2 += lm_a + rm_a + tm_a + bm_a

print("Answer 2:", ans_2)
# ... 608603023105276 - Correct
