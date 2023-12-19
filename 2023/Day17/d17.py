import heapq

class d17():
    def __init__(self, hash_map, max_x, max_y):
        self.map = hash_map
        self.max_x = max_x
        self.max_y = max_y
        self.goal = [max_x, max_y]
        self.max_move = 3
        #self.goal = [0,0]

    def look_around(self, position, low, high):
        around_me = [[1, 0, 0], [0, 1, 1], [-1, 0, 2], [0, -1, 3]]
        to_look = []
        for dx, dy, direction in around_me:
            for i in range(low, high + 1):
                nx = position[0] + dx*i
                ny = position[1] + dy*i
                if 0 <= nx <= self.max_x and 0 <= ny <= self.max_y:
                    to_look.append([nx, ny, direction, i])
        return to_look

    def dijk(self, low, high):
        avaialable_moves = []
        heapq.heappush(avaialable_moves, (0, [0,0], -50))
        visited = set()
        while True:
            cur_heat, best_move, direction = heapq.heappop(avaialable_moves)
            x, y = best_move
            if [x, y] == self.goal:
                return cur_heat
            if (tuple(best_move + [direction])) in visited:
                continue
            visited.add(tuple(best_move + [direction]))
            where_to_look = self.look_around([x,y], low, high)
            next_moves = []
            for nx, ny, ndir, move_dist in where_to_look:
                if abs(direction - ndir) == 2 or ndir == direction:
                    # Dont go the way you came, or the way you were going
                    continue
                nh = cur_heat
                for i in range(1, move_dist+1):
                    if ndir == 0:
                        nh += self.map[y][x+i]
                    elif ndir == 1:
                        nh += self.map[y+i][x]
                    elif ndir == 2:
                        nh += self.map[y][x-i]
                    elif ndir == 3:
                        nh += self.map[y-i][x]
                next_moves.append([[nx, ny], ndir, nh])
            for nm, ndir, next_heat in next_moves:
                heapq.heappush(avaialable_moves, (next_heat, nm, ndir))

    def print_path(self, path):
        for j, row in self.map.items():
            print()
            for i, char in enumerate(row):
                if [i, j] in path:
                    print(end = ".")
                else:
                    print(char, end = "")
        print()

puz_in = {}
with open("input.txt", "r") as file:
    for j, line in enumerate(file):
        line = line.replace("\n", "")
        to_append = []
        for i, char in enumerate(line):
            to_append.append(int(char))
        puz_in[j] = to_append

obj = d17(puz_in, i, j)


print("Answer 1:", obj.dijk(1, 3))
print("Answer 2:", obj.dijk(4, 10))