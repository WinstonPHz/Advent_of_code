
from copy import deepcopy
file1 = open("input.txt", "r")
inputs = ""
for line in file1:
    inputs += line
tiles = inputs.split("\n\n")

tile_keys = []
tile_left = {}
tile_right = {}
tile_top = {}
tile_bot = {}
tiles_dict = {}
unmached = {}
matched_with = {}
for i, tile in enumerate(tiles):
    lines = tile.split("\n")
    key = 0
    for j, line in enumerate(lines):
        if j == 0:
            key = int(line.split(":")[0].split(" ")[1])
            tile_keys.append(key)
            unmached[key] = 4
            matched_with[key] = []
        else:
            if j == 1:
                tile_top[key] = line
                tile_left[key] = line[0]
                tile_right[key] = line[len(line) - 1]
            elif j == len(lines)-1:
                tile_bot[key] = line
                tile_left[key] += line[0]
                tile_right[key] += line[len(line) - 1]
            else:
                tile_left[key] += line[0]
                tile_right[key] += line[len(line)-1]

def found(a, b, note = ""):
    if not(str(b)+note in matched_with[a]):
        matched_with[a].append(str(b) + note)
        unmached[a] -= 1
    if not(str(a)+note in matched_with[b]):
        unmached[b] -= 1
        matched_with[b].append(str(a)+note)


for key1 in tile_keys:
    for key2 in tile_keys:
        if key1 == key2:
            continue
        else:
            # Current orientation
            if tile_top[key1] == tile_top[key2][::-1]:
                found(key1, key2, "fTT")
            if tile_top[key1] == tile_bot[key2][::-1]:
                found(key1, key2, "fTB")
            if tile_top[key1] == tile_right[key2][::-1]:
                found(key1, key2, "fTR")
            if tile_top[key1] == tile_left[key2][::-1]:
                found(key1, key2, "fTL")
            if tile_bot[key1] == tile_bot[key2][::-1]:
                found(key1, key2, "fBB")
            if tile_bot[key1] == tile_right[key2][::-1]:
                found(key1, key2, "fBR")
            if tile_bot[key1] == tile_left[key2][::-1]:
                found(key1, key2, "fBL")
            if tile_left[key1] == tile_right[key2][::-1]:
                found(key1, key2, "fLF")
            if tile_left[key1] == tile_left[key2][::-1]:
                found(key1, key2, "fLL")
            if tile_right[key1] == tile_right[key2][::-1]:
                found(key1, key2, "fRR")
            # reversed orientation
            if tile_top[key1] == tile_top[key2]:
                found(key1, key2, "TT")
            if tile_top[key1] == tile_bot[key2]:
                found(key1, key2, "TB")
            if tile_top[key1] == tile_right[key2]:
                found(key1, key2, "TR")
            if tile_top[key1] == tile_left[key2]:
                found(key1, key2, "TL")
            if tile_bot[key1] == tile_bot[key2]:
                found(key1, key2, "BB")
            if tile_bot[key1] == tile_right[key2]:
                found(key1, key2, "BR")
            if tile_bot[key1] == tile_left[key2]:
                found(key1, key2, "BL")
            if tile_left[key1] == tile_right[key2]:
                found(key1, key2, "LR")
            if tile_left[key1] == tile_left[key2]:
                found(key1, key2, "LL")
            if tile_right[key1] == tile_right[key2]:
                found(key1, key2, "RR")

tots = 1
for key in matched_with:
    if len(matched_with[key]) == 2:
        tots*=key

print(tots)

for key2 in tile_keys:
    if key1 == key2:
        continue
    else:
        # Current orientation
        if tile_top[key1] == tile_top[key2][::-1]:
            found(key1, key2, 0, 4)  # fTT
        if tile_top[key1] == tile_bot[key2][::-1]:
            found(key1, key2, 0, 1)  # fTB
        if tile_top[key1] == tile_right[key2][::-1]:
            found(key1, key2, 0, 5)  # fTR
        if tile_top[key1] == tile_left[key2][::-1]:
            found(key1, key2, 0, 7)  # "fTL"
        if tile_bot[key1] == tile_bot[key2][::-1]:
            found(key1, key2, 2, 6)  # "fBB"
        if tile_bot[key1] == tile_right[key2][::-1]:
            found(key1, key2, 2, 5)  # "fBR"
        if tile_bot[key1] == tile_left[key2][::-1]:
            found(key1, key2, 2, 7)  # "fBL"
        if tile_left[key1] == tile_right[key2][::-1]:
            found(key1, key2, 3, 5)  # "fLF"
        if tile_left[key1] == tile_left[key2][::-1]:
            found(key1, key2, 3, 7)  # "fLL"
        if tile_right[key1] == tile_right[key2][::-1]:
            found(key1, key2, 1, 5)  # "fRR"
        # reversed orientation
        if tile_top[key1] == tile_top[key2]:
            found(key1, key2, 0, 0)
        if tile_top[key1] == tile_bot[key2]:
            found(key1, key2, 0, 2)
        if tile_top[key1] == tile_right[key2]:
            found(key1, key2, 0, 1)
        if tile_top[key1] == tile_left[key2]:
            found(key1, key2, 0, 3)
        if tile_bot[key1] == tile_bot[key2]:
            found(key1, key2, 2, 2)
        if tile_bot[key1] == tile_right[key2]:
            found(key1, key2, 2, 1)
        if tile_bot[key1] == tile_left[key2]:
            found(key1, key2, 2, 3)
        if tile_left[key1] == tile_right[key2]:
            found(key1, key2, 3, 1)
        if tile_left[key1] == tile_left[key2]:
            found(key1, key2, 3, 3)
        if tile_right[key1] == tile_right[key2]:
            found(key1, key2, 1, 1)