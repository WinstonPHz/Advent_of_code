from copy import deepcopy
file1 = open("input.txt", "r")
inputs = ""
for line in file1:
    inputs += line
puzzle = inputs.split("\n")


def count_fulls(current_state):
    look_at = [-1,0,1]
    counts = deepcopy(current_state)
    for l in range(-size, size + 1):
        for k in range(-size, size+1):
            for j in range(-size, size+1):
                for i in range(-size, size+1):
                    count = 0
                    for ii, x in enumerate(look_at):
                        for jj, y in enumerate(look_at):
                            for kk, z in enumerate(look_at):
                                for ll, w in enumerate(look_at):
                                    try:
                                        if current_state[l+w][k+z][j+y][i+x] == 1:
                                            if w == 0 and x == 0 and y == 0 and z == 0:
                                                continue
                                            else:
                                                count += 1
                                    except:
                                        continue
                    counts[l][k][j][i] = count
    return counts

def change_state(current_state, current_count):
    counts = deepcopy(current_count)
    for l in range(-size, size+1):
        for k in range(-size, size+1):
            for j in range(-size, size+1):
                for i in range(-size, size+1):
                    if current_state[l][k][j][i] == 1 and 2<=counts[l][k][j][i]<=3:
                        continue
                    elif current_state[l][k][j][i] == 0 and counts[l][k][j][i] == 3:
                        current_state[l][k][j][i] = 1
                    else:
                        current_state[l][k][j][i] = 0
    return current_state

def sum_active(current_state):
    actives = 0
    for l in range(-size, size + 1):
        for k in range(-size, size + 1):
            for j in range(-size, size + 1):
                for i in range(-size, size + 1):
                    if current_state[l][k][j][i] == 1:
                        actives += 1
    return actives

def print_pritty(current_state, depth):
    for j in range(-size, size + 1):
        for i in range(-size, size + 1):
            print(current_state[depth][depth][j][i], end="")
        print()
##### Part 1
cycles = 6
layer = {}
x = {}
size = cycles+len(puzzle)
for i in range(size+1):
    if i == 0:
        x[i] = 0
    else:
        x[-i] = 0
        x[i] = 0
y = {}
for i in range(size+1):
    if i == 0:
        y[i] = deepcopy(x)
    else:
        y[-i] = deepcopy(x)
        y[i] = deepcopy(x)
z = {}
for i in range(size+1):
    if i == 0:
        z[i] = deepcopy(y)
    else:
        z[-i] = deepcopy(y)
        z[i] = deepcopy(y)

w = {}
for i in range(size+1):
    if i == 0:
        w[i] = deepcopy(z)
    else:
        w[-i] = deepcopy(z)
        w[i] = deepcopy(z)

for j, row in enumerate(puzzle):
    for i, col in enumerate(row):
        if col == "#":
            w[0][0][j][i] = 1



for i in range(6):
    c = count_fulls(deepcopy(w))
    w = change_state(deepcopy(w),c)


print("Answer 2:", sum_active(w))