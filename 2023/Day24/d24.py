import heapq
from functools import cache
from copy import deepcopy
import math

class d24():
    def __init__(self):
        self.hail = {}
        self.hail_id = 0
        self.ans_1 = 0

    def add_range(self, range_start, range_end):
        self.range_start = range_start
        self.range_end = range_end

    def add_hail(self, initial_contintions):
        possition, velocity = initial_contintions.split(" @ ")
        x, y, z = possition.split(", ")
        dx, dy, dz =velocity.split(", ")
        self.hail[self.hail_id] = {"pos":[int(x),int(y),int(z)], "vel":[int(dx),int(dy),int(dz)]}
        self.hail_id += 1

    def find_slope_intersect(self, a_pos, a_vel, b_pos, b_vel):
        ax, ay = a_pos
        adx, ady = a_vel
        bx, by = b_pos
        bdx, bdy = b_vel
        ma = ady/adx
        mb = bdy/bdx
        if ma == mb:
            return False
        a_y_intercept = ay-ax*ma
        b_y_intercept = by-bx*mb
        x_cross = (b_y_intercept - a_y_intercept)/(ma - mb)
        y_cross = ma*x_cross + a_y_intercept
        time_a = (x_cross - ax)/adx
        time_b = (x_cross - bx)/bdx

        if time_a < 0 or time_b < 0:
            return False
        if self.range_start <= x_cross <= self.range_end and self.range_start <= y_cross <= self.range_end:
            return True
        return False


    def find_velocity(self, a):
        possible_vel = set()
        for i in range(-1000, 1000):
            possible_vel.add(i)
        velocity_pairs = {}
        for i in range(self.hail_id):
            hail_velocity = self.hail[i]["vel"][a]
            hail_pos = self.hail[i]["pos"][a]
            if hail_velocity not in velocity_pairs.keys():
                velocity_pairs[hail_velocity] = [hail_pos]
            else:
                velocity_pairs[hail_velocity].append(hail_pos)
        for vel in velocity_pairs.keys():
            if len(velocity_pairs[vel]) == 1:
                # Method does not work if there is one ice chunk
                continue
            new_possible_vel = set()
            p0 = velocity_pairs[vel].pop(0)
            while velocity_pairs[vel]:
                p1 = velocity_pairs[vel].pop(0)
                for rock_vel in range(-1000, 1000):
                    if rock_vel - vel == 0:
                        # Rock and Ice Velocities can't be equal
                        continue
                    equation = abs(p0-p1)%(rock_vel - vel)
                    if equation == 0:
                        new_possible_vel.add(rock_vel)
                p0 = p1

            possible_vel = new_possible_vel.intersection(possible_vel)
        if len(possible_vel) > 1:
            print("Didn't get it right")
        if len(possible_vel) == 1:
            return list(possible_vel)[0]
        return list(possible_vel)[0]

    def find_start_time(self, vel):
        found = [0,0,0]
        rock_start = 0
        start_dir = 0
        for i in range(self.hail_id):
            for j, val in enumerate(vel):
                if val == self.hail[i]["vel"][j]:
                    rock_start = self.hail[i]["pos"][j]
                    start_dir = j
                    found[start_dir] = rock_start


        hail_velocity = self.hail[0]["vel"][start_dir]
        hail_pos = self.hail[0]["pos"][start_dir]
        time = (rock_start - hail_pos)/(hail_velocity - vel[start_dir])

        ans_2 = 0
        for i in range(3):
            x0 = self.hail[0]["pos"][i]
            dx0 = self.hail[0]["vel"][i]
            dr = vel[i]
            next_find = time*(dx0-dr)+x0
            if found[i] == 0:
                found[i] = next_find
            elif found[i] != next_find:
                print("This is corrects")
            ans_2 += int(found[i])
        print("Answer 2:", ans_2)
                    




    def run(self):
        collisions = set()
        faileds = set()
        for i in range(self.hail_id):
            for j in range(self.hail_id):
                if i == j:
                    continue
                pair = [i,j]
                pair.sort()
                if tuple(pair) in collisions or tuple(pair) in faileds:
                    continue
                i_inital = self.hail[i]
                j_inital = self.hail[j]
                i_pos = i_inital["pos"]
                i_vel = i_inital["vel"]
                j_pos = j_inital["pos"]
                j_vel = j_inital["vel"]

                if self.find_slope_intersect(i_pos[:2],i_vel[:2], j_pos[:2], j_vel[:2]):
                    collisions.add(tuple(pair))
                else:
                    faileds.add(tuple(pair))
        print("Answer 1:", len(collisions))


obj = d24()
map = {}
with open("input.txt", "r") as file:
    for j, line in enumerate(file):
        line = line.replace("\n", "")
        obj.add_hail(line)

if j <= 5:
    obj.add_range(7,28)
else:
    obj.add_range(200000000000000, 400000000000000)

obj.run()
ans_2 = 0
v_rock = []
for i in range(3):
    v_rock.append(obj.find_velocity(i))
time = obj.find_start_time(v_rock)
# pt1: 20336

# 677656046662771 is too high