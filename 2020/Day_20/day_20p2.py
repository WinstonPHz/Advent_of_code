import math
from copy import deepcopy
file1 = open("input.txt", "r")
inputs = ""
for line in file1:
    inputs += line
tiles = inputs.split("\n\n")
file1.close()



def printpritty(tile):
    for i, row in enumerate(tile):
        for j, data in enumerate(row):
            print(data, end = "")
        print()
    print()

def flip(tile, times):
    if times == 0:
        return tile
    new_tile = deepcopy(tile)
    for k in range(times):
        for i, row in enumerate(tile):
            for j, data  in enumerate(row):
                new_tile[j][i] = data
    return new_tile


def rotate(tile, times):
    new_tile = deepcopy(tile)
    if times == 0:
        return tile
    for k in range(times):
        n = len(tile[0])
        for i in range(n // 2):
            for j in range(i, n-i-1):
                temp = new_tile[i][j]
                new_tile[i][j] = new_tile[n-1-j][i]
                new_tile[n - 1 - j][i] = new_tile[n - 1 - i][n - 1 - j]
                new_tile[n - 1 - i][n - 1 - j] = new_tile[j][n - 1 - i]
                new_tile[j][n - 1 - i] = temp
    return new_tile

# Matches Bot of tile1 to top of tile 2
def match(tile1, tile2):
    if tile1[len(tile2)-1] == tile2[0]:
        return True
    else:
        return False

# right of tile 1 to left of tile 2
def match_left(tile1, tile2):
    tile1_match = ""
    tile2_match = ""
    for data in tile1:
        tile1_match += data[-1]
    for data in tile2:
        tile2_match += data[0]
    if tile1_match == tile2_match:
        return True
    else:
        return False

def fits():
    print("Starting to find all the pieces that go together.")
    for key1 in tiles_dict:
        for key2 in tiles_dict:
            if key1 == key2:
                continue
            if key2 in pieces_found[key1]:
                continue
            for rk1 in range(4):
                for fk2 in range(2):
                    for rk2 in range(4):
                        test = match(flip(rotate(tiles_dict[key1],rk1),0),
                                     flip(rotate(tiles_dict[key2],rk2),fk2))
                        if test == True:
                            if key2 in pieces_found[key1]:
                                continue
                            pieces_found[key1].append(key2)
                            orientations[key1].append([key2,rk2,fk2,rk2])


    # Time to orient all the pieces and place them....
    for key in tiles_dict:
        if len(pieces_found[key]) == 2:
            composite[0][0] = key
            used.append(key)
            break
    tots = 1
    for key in tiles_dict:
        if len(pieces_found[key]) == 2:
            tots *= key
    print("Answer 1:", tots)

def place_pieces():
    print("Placing the pieces")
    # left row, and that is it for now.
    for i, key1 in enumerate(composite[0]):
        if i == len(composite[0])-1:
            break
        for key2 in pieces_found[key1]:
            if composite[0][i+1] != 0 or key2 in used:
                continue
            if i == 0:
                for fk1 in range(2):
                    for rk1 in range(4):
                        for fk2 in range(2):
                            for rk2 in range(4):
                                test = match_left(flip(rotate(tiles_dict[key1], rk1), fk1),
                                                  flip(rotate(tiles_dict[key2], rk2), fk2))
                                if test:
                                    tiles_dict[key1] = flip(rotate(tiles_dict[key1], rk1), fk1)
                                    tiles_cut[key1] = flip(rotate(tiles_cut[key1], rk1), fk1)
                                    tiles_dict[key2] = flip(rotate(tiles_dict[key2], rk2), fk2)
                                    tiles_cut[key2] = flip(rotate(tiles_cut[key2], rk2), fk2)
                                    composite[0][i + 1] = key2
                                    used.append(key2)
            else:
                for fk2 in range(2):
                    for rk2 in range(4):
                        test = match_left(tiles_dict[key1],
                                          flip(rotate(tiles_dict[key2], rk2), fk2))
                        if test:
                            tiles_dict[key2] = flip(rotate(tiles_dict[key2], rk2), fk2)
                            tiles_cut[key2] = flip(rotate(tiles_cut[key2], rk2), fk2)
                            composite[0][i+1] = key2
                            used.append(key2)
                            break

    for i, row in enumerate(composite):
        if i == len(composite) - 1:
            break
        for j, key1 in enumerate(row):
            for key2 in pieces_found[key1]:
                if composite[i+1][j] != 0 or key2 in used:
                    continue
                for fk2 in range(2):
                    for rk2 in range(4):
                        test = match(tiles_dict[key1],
                                    flip(rotate(tiles_dict[key2], rk2), fk2))
                        if test:
                            tiles_dict[key2] = flip(rotate(tiles_dict[key2], rk2), fk2)
                            tiles_cut[key2] = flip(rotate(tiles_cut[key2], rk2), fk2)
                            composite[i+1][j] = key2
                            used.append(key2)
                            break

def make_picture():
    print("Making Picture")
    p_row = []
    for i in range(size*len(tiles_cut[tile_keys[0]])):
        p_row.append(".")
    for i in range(size*len(tiles_cut[tile_keys[0]])):
        picture.append(p_row.copy())
    # Make the picture
    length = len(tiles_cut[tile_keys[0]])
    for ii, row in enumerate(composite):
        for jj, key in enumerate(row):
            for i, data_row, in enumerate(tiles_cut[key]):
                for j, col in enumerate(data_row):
                    picture[i + int(length*ii)][j + int(jj*length)] = col

def make_monster():
    file1 = open("Seamonster.txt", "r")
    inputs = ""
    for line in file1:
        inputs += line
    sea_row = inputs.split("\n")
    for i, sea_r in enumerate(sea_row):
        for j, sea_c in enumerate(sea_r):
            if sea_c == "#":
                monster.append([i, j])

def search_monster():
    loc_count = 0
    for pic_flip in range(2):
        for pic_rot in range(4):
            new_pic = flip(rotate(picture, pic_rot), pic_flip)
            for i in range(len(picture)-3):
                for j in range(len(picture[0])-20):
                    loc_truth = True
                    for loc in monster:
                        if new_pic[i+loc[0]][j+loc[1]] != "#":
                            loc_truth = False
                            break
                    if loc_truth:
                        loc_count += 1
            if loc_count > 0:
                break
    surface = 0
    for i, row in enumerate(picture):
        for j, col in enumerate(row):
            if col == "#":
                surface += 1

    print("Loc Count", loc_count)
    print("Answer 2:", surface-loc_count*len(monster))



monster = []
picture = []
tile_keys = []
tiles_dict = {}
tiles_cut = {}
orientations = {}
composite = []
used = []
size = int(math.sqrt(len(tiles)))
pieces_found = {}

for i in range(size):
    inside = []
    for j in range(size):
        inside.append(0)
    composite.append(inside)

for i, tile in enumerate(tiles):
    lines = tile.split("\n")
    key = 0
    for j, line in enumerate(lines):
        bits = []
        cut_bits = []
        if j == 0:
            key = int(line.split(":")[0].split(" ")[1])
            tile_keys.append(key)
            tiles_dict[key] = []
            pieces_found[key] = []
            orientations[key] = []
            tiles_cut[key] = []
        else:
            for k, digit in enumerate(line):
                bits.append(digit)
                if j == 1 or j == len(lines)-1:
                    continue
                else:
                    if k == 0 or k == len(line)-1:
                        continue
                    else:
                        cut_bits.append(digit)

        tiles_dict[key].append(bits)
        tiles_cut[key].append(cut_bits)
    tiles_dict[key].pop(0)
    tiles_cut[key].pop(0)
    tiles_cut[key].pop(0)
    tiles_cut[key].pop(-1)

fits()
place_pieces()
make_picture()
make_monster()
search_monster()