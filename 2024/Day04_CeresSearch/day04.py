import re
check_strings = []
file_strings = {}

with open("input.txt", "r") as file:
    for i, line in enumerate(file):
        line = line.strip("\n")
        file_strings[i] = line
        check_strings.append(line)
# Normal info
width = len(file_strings[0])
height = len(check_strings)

def check_a(x, y):
    if not 0 < x < width-1:
        return False
    if not 0 < y < height-1:
        return False
    down = [[x-1, y-1], [x, y], [x+1, y+1]]
    up = [[x-1, y+1], [x, y], [x+1, y-1]]
    down_string = ""
    up_string = ""
    for i, j in down:
        down_string += file_strings[j][i]
    for i, j in up:
        up_string += file_strings[j][i]
    checker = ["MAS", "SAM"]
    #print(x, y, down_string, up_string)
    if down_string in checker and up_string in checker:
        return True
    return False
# up down
for j in range(width):
    to_add = ""
    for i in range(height):
        to_add += file_strings[i][j]
    check_strings.append(to_add)

# Diagnal up
for j in range(height):
    to_add_up = ""
    start_y = j
    start_x = 0
    while start_y >= 0:
        to_add_up += file_strings[start_y][start_x]
        start_y -= 1
        start_x += 1
    check_strings.append(to_add_up)

for j in range(1, width):
    to_add_up = ""
    start_x = j
    start_y = height-1
    while start_y >= 0 and start_x < width:
        to_add_up += file_strings[start_y][start_x]
        start_y -= 1
        start_x += 1
    check_strings.append(to_add_up)

# editing for part 2
# Diaganal Down
a_locations = []

for j in range(height):
    to_add_up = ""
    start_y = j
    start_x = 0
    while start_y < height:
        to_add_up += file_strings[start_y][start_x]
        if file_strings[start_y][start_x] == "A":
            a_locations.append([start_x, start_y])
        start_y += 1
        start_x += 1
    check_strings.append(to_add_up)

for j in range(1, width):
    to_add_up = ""
    start_x = j
    start_y = 0
    while start_y < height and start_x < width:
        to_add_up += file_strings[start_y][start_x]
        if file_strings[start_y][start_x] == "A":
            a_locations.append([start_x, start_y])
        start_y += 1
        start_x += 1
    check_strings.append(to_add_up)


total = 0

for row in check_strings:
    total += len(re.findall("XMAS", row))
    total += len(re.findall("SAMX", row))

total_2 = 0
for a, b, in a_locations:
    if check_a(a, b):
        total_2 += 1
print("Anwer 1:", total)
print("Anwer 2:", total_2)

