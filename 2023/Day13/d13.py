import math
import copy
class part1():
    def __init__(self):
        self.maps = {}
        self.ans_1 = 0
        self.ans_2 = 0

    def add_map(self, map):
        map_index = len(tuple(self.maps.keys())) +1
        self.maps[map_index] = map

    def mirror_horizon(self, grid):
        length = len(tuple(grid.keys()))
        possible_matches = []
        for row_id, row in grid.items():
            if row_id + 1 < length:
                if row == grid[row_id+1]:
                    possible_matches.append(row_id)
        for match in possible_matches:
            last = True
            for i in range(match+1):
                row_to_check = (match)*2 + 1 - i
                if row_to_check >= length:
                    continue
                if grid[i] != grid[row_to_check]:
                    last = False
                    break
            if last: return match
        return -1

    def get_colmub(self, col_id, grid):
        ret_row = ""
        for row_id, row in grid.items():
            ret_row += row[col_id]
        return ret_row

    def mirror_vertical(self, grid):
        length = len(grid[0])
        possible_matches = []
        for col_id in range(length+1):
            if col_id + 1 < length:
                if self.get_colmub(col_id, grid) == self.get_colmub(col_id+1, grid):
                    possible_matches.append(col_id)
        for match in possible_matches:
            last = True
            for i in range(match + 1):
                row_to_check = (match) * 2 + 1 - i
                if row_to_check >= length:
                    continue
                if self.get_colmub(i, grid) != self.get_colmub(row_to_check, grid):
                    last = False
                    break
            if last: return match
        return -1

    def get_diff(self, line1, line2):
        count = 0
        for i in range(len(line1)):
            if line1[i] != line2[i]:
                count += 1
        return count

    def fix_hoz(self, grid):
        length = len(tuple(grid.keys()))
        possible_matches = []
        for row_id, row in grid.items():
            if row_id + 1 < length:
                if self.get_diff(row, grid[row_id+1]) <= 1:
                    possible_matches.append(row_id)
        print(possible_matches)
        for match in possible_matches:
            last = True
            fixed = False
            for i in range(match+1):
                row_to_check = (match)*2 + 1 - i
                if row_to_check >= length:
                    continue
                print(match, i, grid[i], grid[row_to_check], last, fixed)
                diff =  self.get_diff(grid[i], grid[row_to_check])
                if diff == 1 and not fixed:
                    fixed = True
                    continue
                if fixed and diff > 0:
                    last = False
                    break
                if diff > 1:
                    last = False
                    break
            if last and fixed: return match
        return -1

    def fix_vert(self, grid):
        print("Fixing Vert")
        length = len(grid[0])
        possible_matches = []
        for col_id in range(length+1):
            if col_id + 1 < length:
                if self.get_diff(self.get_colmub(col_id, grid), self.get_colmub(col_id+1, grid)) <= 1:
                    possible_matches.append(col_id)
        print(possible_matches)
        for match in possible_matches:
            last = True
            fixed = False
            for i in range(match + 1):
                row_to_check = (match) * 2 + 1 - i
                if row_to_check >= length:
                    continue
                print(match, i, row_to_check, self.get_colmub(i, grid), self.get_colmub(row_to_check, grid), last, fixed)
                diff = self.get_diff(self.get_colmub(i, grid), self.get_colmub(row_to_check, grid))
                if diff == 1 and not fixed:
                    fixed = True
                    continue
                if fixed and diff > 0:
                    last = False
                    break
                if diff > 1:
                    last = False
                    break
            if last and fixed: return match
        print("returning")
        return -1

    def run(self):
        for map_id, map in self.maps.items():
            hoz_mirror_at = self.mirror_horizon(map)
            if hoz_mirror_at != -1:
                self.ans_1 += (hoz_mirror_at+1)*100
            vert_mirror_at = self.mirror_vertical(map)
            if vert_mirror_at != -1:
                self.ans_1 += (vert_mirror_at+1)
            if vert_mirror_at == -1 and hoz_mirror_at == -1:
                print("GOD HELP US ALL")

            #part2
            fixed_horizontal = self.fix_hoz(map)
            if fixed_horizontal != -1:
                self.ans_2 += (fixed_horizontal + 1) * 100
            fixed_vertical = self.fix_vert(map)
            if fixed_vertical != -1:
                self.ans_2 += (fixed_vertical + 1)
            if fixed_vertical > -1 and fixed_horizontal > -1:
                print(map_id, "GET THIS MAN FIXED", fixed_vertical, fixed_horizontal)

in_map = {}
offset = 0
obj = part1()
with open("input.txt", "r") as file:
    for j, line in enumerate(file):
        line = line.replace("\n", "")
        if line == "":
            obj.add_map(in_map)
            in_map = {}
            offset = j + 1
            continue
        if "end" in line:
            break
        in_map[j-offset] = line
obj.run()

print("Answer 1 :", obj.ans_1)
print("Answer 2 :", obj.ans_2)

# High
# 42710
