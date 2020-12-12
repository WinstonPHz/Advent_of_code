file1 = open("input.txt", "r")
from copy import deepcopy
inputs = ""
for line in file1:
    inputs += line
inputs_arr = inputs.split("\n")
puzzle = []
dots = [".", "."]
for i, data in enumerate(inputs_arr[0]):
    dots.append(".")

for i, row in enumerate(inputs_arr):
    line = []
    if i == 0:
        puzzle.append(dots)
    line.append(".")
    for item in row:
        line.append(item)
    line.append(".")
    puzzle.append(line)
puzzle.append(dots)
current_seat_state = deepcopy(puzzle)
new_seat_state = []

def count_fulls(current_state):
    look_at = [-1,0,1]
    seats_count = deepcopy(current_state)
    for i, row in enumerate(current_state):
        for j, column in enumerate(row):
            if column == ".":
                continue
            count = 0
            for ii, x in enumerate(look_at):
                for jj, y in enumerate(look_at):
                    if current_state[i+x][j+y] == "#":
                        if x == 0 and y == 0:
                            continue
                        else:
                            count += 1
            seats_count[i][j] = count
    return seats_count

def count_occupide(current_occ):
    count = 0
    for i, column in enumerate(current_occ[0]):
        for j, row in enumerate(current_occ):
            if current_occ[i][j] == "#":
                count += 1
    return count

def change_seat_state(current_state, seat_count):
    new_state = deepcopy(current_state)
    for i, row in enumerate(seat_count):
        for j, column in enumerate(row):
            if column == ".":
                continue
            if (column > 3) and (new_state[i][j] == "#"):
                new_state[i][j] = "L"
            elif (column == 0) and (new_state[i][j] == "L"):
                new_state[i][j] = "#"
    return new_state



curr_count = -1
prev_count = 1
while curr_count != prev_count:
    current_count = count_fulls(current_seat_state)
    new_seat_state = change_seat_state(deepcopy(current_seat_state), current_count)
    current_seat_state = deepcopy(new_seat_state)
    prev_count = curr_count
    curr_count = count_occupide(current_seat_state)
print(curr_count)

## Part 2
def count_fulls2(current_state):
    seats_count = deepcopy(current_state)
    for i, row in enumerate(current_state):
        for j, column in enumerate(row):
            if current_state[i][j] == ".":
                continue
            count = 0
            up = range(1, i)
            down = range(1, len(current_state)-i-1)
            left = range(1, j)
            right = range(1, len(current_state[i])-j-1)
            if up == range(1, 1): up = [1]
            if down == range(1, 1): down = [1]
            if left == range(1, 1): left = [1]
            if right == range(1, 1): right = [1]
            ul = range(1, min([i, j]))
            ur = range(1, min([i, len(current_state[i])-j-1]))
            dl = range(1, min([len(current_state)-i-1, j]))
            dr = range(1, min([len(current_state)-i-1, len(current_state[i])-j-1]))
            if ul == range(1, 1): ul = [1]
            if ur == range(1, 1): ur = [1]
            if dl == range(1, 1): dl = [1]
            if dr == range(1, 1): dr = [1]
            for ii in up:
                if current_state[i-ii][j] == "#":
                    count += 1
                    break
                elif current_state[i-ii][j] == "L":
                    break
            # Looking Down
            for ii in down:
                if current_state[i+ii][j] == "#":
                    count += 1
                    break
                elif current_state[i+ii][j] == "L":
                    break
            # looking Right
            for ii in right:
                if current_state[i][j+ii] == "#":
                    count += 1
                    break
                elif current_state[i][j+ii] == "L":
                    break
            # looking Left
            for ii in left:
                if current_state[i][j-ii] == "#":
                    count += 1
                    break
                elif current_state[i][j-ii] == "L":
                    break
            # Diagon Ally
            # ul

            for ii in ul:
                if current_state[i-ii][j-ii] == "#":
                    count += 1
                    break
                elif current_state[i-ii][j - ii] == "L":
                    break
            for ii in ur:
                if current_state[i-ii][j + ii] == "#":
                    count += 1
                    break
                elif current_state[i-ii][j+ii] == "L":
                    break
            for ii in dl:
                if current_state[i+ii][j-ii] == "#":
                    count += 1
                    break
                elif current_state[i+ii][j-ii] == "L":
                    break
            for ii in dr:
                if current_state[i+ii][j+ii] == "#":
                    count += 1
                    break
                elif current_state[i+ii][j+ii] == "L":
                    break
            seats_count[i][j] = count
    return seats_count


def change_seat_state2(current_state, seats_count):
    new_state = deepcopy(current_state)
    for i in range(1,len(new_state[0])-1):
        for j in range(1,len(new_state)-1):
            if current_state[i][j] == ".":
                continue
            if (seats_count[i][j] > 4) and (current_state[i][j] == "#"):
                new_state[i][j] = "L"
            elif (seats_count[i][j] == 0) and (current_state[i][j] == "L"):
                new_state[i][j] = "#"
    return new_state

curr_count = -1
prev_count = 1
current_seat_state = deepcopy(puzzle)
while curr_count != prev_count:
    current_count = count_fulls2(current_seat_state)
    new_seat_state = change_seat_state2(deepcopy(current_seat_state), current_count)
    current_seat_state = deepcopy(new_seat_state)
    prev_count = curr_count
    curr_count = count_occupide(current_seat_state)

print(curr_count)

