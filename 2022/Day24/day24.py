import copy
import heapq

class blizard():
    def __init__(self):
        self.blizards_starting = {0:{}, 1:{}, 2:{}, 3:{}}
        self.bliz_code = {0:">", 1:"v", 2:"<", 3:"^"}
        self.bliz_code_get = {}
        for key, item in self.bliz_code.items():
            self.bliz_code_get[item] = key
        self.walls = []
        # X, Y
        self.starting = [1, 0]
        with open("input.txt", "r") as file:
            for j, line in enumerate(file):
                line = line.strip("\n")
                for i, char in enumerate(line):
                    if char == "#":
                        self.walls.append([i,j])
                        continue
                    if char == ".":
                        continue
                    blizard_code = self.bliz_code_get[char]
                    if blizard_code in [0,2]:
                        if j not in self.blizards_starting[blizard_code].keys():
                            self.blizards_starting[blizard_code][j] = []
                        self.blizards_starting[blizard_code][j].append(i)
                    elif blizard_code in [1,3]:
                        if i not in self.blizards_starting[blizard_code].keys():
                            self.blizards_starting[blizard_code][i] = []
                        self.blizards_starting[blizard_code][i].append(j)

        self.x_length = i
        self.y_length = j
        self.goal = [i-1,j]
        self.Started = False
        self.best_goal = 0
        self.repeat = 700 # LCM of the lengths 700 for input

    def blizard_move(self, step, x, y):
        if y < 0 or x < 0:
            return False
        if [x,y] in self.walls:
            return False
        for i in range(4):
            if i == 0:
                #Right blizards
                if y in self.blizards_starting[i].keys():
                    for blizard in self.blizards_starting[i][y]:
                        bliz_pos = 1+(blizard+step-1)%(self.x_length-1)
                        if bliz_pos == x:
                            return False
            if i == 1:
                # down blizards
                if x in self.blizards_starting[i].keys():
                    for blizard in self.blizards_starting[i][x]:
                        bliz_pos = 1+(blizard+step-1)%(self.y_length-1)
                        if bliz_pos == y:
                            return False
            if i == 2:
                # Left Blizards
                if y in self.blizards_starting[i].keys():
                    for blizard in self.blizards_starting[i][y]:
                        bliz_pos = 1+(blizard - step - 1) % (self.x_length-1)
                        if bliz_pos == x:
                            return False
            if i == 3:
                # up blizards
                if x in self.blizards_starting[i].keys():
                    for blizard in self.blizards_starting[i][x]:
                        bliz_pos = 1 + (blizard - step - 1) % (self.y_length - 1)
                        if bliz_pos == y:
                            return False
        return True

    def look_around(self, position):
        around_me = [[1, 0], [0, 1], [-1, 0], [0, -1], [0, 0]]
        to_look = []
        for dx, dy in around_me:
            nx = position[0] + dx
            ny = position[1] + dy
            to_look.append([nx, ny])
        return to_look

    def dijk(self, start, goal, cur_step):
        avaialable_moves = []
        heapq.heappush(avaialable_moves, (0, start, cur_step))
        visited = set()
        while True:
            _, best_move, step_num = heapq.heappop(avaialable_moves)
            if (tuple(best_move), step_num) not in visited:
                visited.add((tuple(best_move), step_num))
                x, y = best_move
                if [x, y] == goal:
                    print("Shortest path go goal is", step_num)
                    self.best_goal = step_num
                    return
                step_num += 1
                where_to_look = self.look_around([x,y])
                next_moves = []
                for nx, ny in where_to_look:
                    if self.blizard_move(step_num, nx, ny): next_moves.append([nx, ny])
                for nm in next_moves:
                    man_dist_to_end = abs(nm[0]-goal[0]) + abs(nm[1] - goal[1])
                    heapq.heappush(avaialable_moves, (man_dist_to_end+step_num-1, nm, step_num))

    def part2(self):
        self.dijk(self.starting, self.goal, 0)
        print("Answer 1:", self.best_goal)
        self.dijk(self.goal, self.starting, self.best_goal)
        self.dijk(self.starting, self.goal, self.best_goal)
        print("Answer 2:", self.best_goal)



bz = blizard()
bz.part2()

