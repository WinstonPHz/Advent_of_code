file1 = open("input.txt", "r")
Current_pos = 0
hit_trees = 0
rows = []
for line in file1:
    rows.append(line.split("\n")[0])
for row in rows:
    if Current_pos >= len(row):
        Current_pos -= len(row)
    if row[Current_pos] == "#":
        hit_trees += 1
    Current_pos = (Current_pos + 3)

def slope(right, down):
    vert = down-1
    Current_pos = 0
    hit_trees = 0
    for row in rows:
        vert += 1
        if vert == down:
            if Current_pos >= len(row):
                Current_pos -= len(row)
            if row[Current_pos] == "#":
                hit_trees += 1
            Current_pos = (Current_pos + right)
            vert -= down
    return hit_trees
print("Trees hit 1: ", hit_trees)
cases = [[1,1],[3,1],[5,1],[7,1],[1,2]]
var = 1
for case in cases:
    print(slope(case[0],case[1]))
    var = var*slope(case[0],case[1])

print("Testing hit 1:", slope(3,1))
print("Multiple of Trees hit 2: ", var)