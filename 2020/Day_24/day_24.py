from copy import deepcopy
file1 = open("input.txt", "r")
inputs = ""
for line in file1:
    inputs += line
puzzle = inputs.split("\n")

flipped = []
for i, tile_set in enumerate(puzzle):
    x = 0
    y = 0
    to_flip = tile_set
    while True:
        if to_flip[0] == "s":
            if to_flip[1] == "e":
                y -= 2
                x += 1
                to_flip = to_flip[2:]
            elif to_flip[1] == "w":
                y -= 2
                x -= 1
                to_flip = to_flip[2:]
        elif to_flip[0] == "n":
            if to_flip[1] == "e":
                y += 2
                x += 1
                to_flip = to_flip[2:]
            elif to_flip[1] == "w":
                y += 2
                x -= 1
                to_flip = to_flip[2:]
        elif to_flip[0] == "e":
            x += 2
            to_flip = to_flip[1:]
        elif to_flip[0] == "w":
            x -= 2
            to_flip = to_flip[1:]
        if to_flip == "":
            break
    flipped.append([x,y])

have = []
for i, flip in enumerate(flipped):
    if flip in have:
        have.remove(flip)

    else:
        have.append(flip)

print("Answer 1: ", len(have))
adjacents = [[-1, 2], [1, 2], [-2, 0], [2, 0],
            [-1, -2], [1, -2]]

blacks = deepcopy(have)
whites = []
print("This Part Takes a While")
for i in range(100):
    to_change_b = []
    to_change_w = []
    # Making Sure all whites are present
    for tile in blacks:
        for adj in adjacents:
            if [tile[0]+adj[0], tile[1]+adj[1]] not in blacks and [tile[0]+adj[0], tile[1]+adj[1]] not in whites:
                whites.append([tile[0]+adj[0], tile[1]+adj[1]])
    # Counting the blacks around black
    for tile in blacks:
        count = 0
        for adj in adjacents:
            if [tile[0]+adj[0], tile[1]+adj[1]] in blacks:
                count += 1
        if count == 0 or count > 2:
            to_change_b.append(tile)
    # Counting the blacks around whites
    for tile in whites:
        count = 0
        for adj in adjacents:
            if [tile[0] + adj[0], tile[1] + adj[1]] in blacks:
                count += 1
        if count == 2:
            to_change_w.append(tile)

    for c_white in to_change_w:
        blacks.append(c_white)
        whites.remove(c_white)
    for c_black in to_change_b:
        whites.append(c_black)
        blacks.remove(c_black)
    if i % 10 == 0:
        print(f"Day {i+1}:", len(blacks))
print("Answer 2:", len(blacks))