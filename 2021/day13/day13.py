def get_input():
    bits = []
    folds = []
    for line in open("puz", "r+"):
        line = line.strip("\n")
        if "," in line:
            cords = line.split(",")
            bits.append([int(cords[0]), int(cords[1])])
        elif "along" in line:
            comps = line.split(" ")[2].split("=")
            folds.append([comps[0], int(comps[1])])
    return bits, folds

def fold(cord_list, fold_dir, fold_local):
    new_cord_list = []
    if fold_dir == "y":
        for x, y in cord_list:
            new_y = y
            if y > fold_local:
                new_y = fold_local - (y - fold_local)
            if [x, new_y] not in new_cord_list:
                new_cord_list.append([x, new_y])
    if fold_dir == "x":
        for x, y in cord_list:
            new_x = x
            if x > fold_local:
                new_x = fold_local - (x - fold_local)
            if [new_x, y] not in new_cord_list:
                new_cord_list.append([new_x, y])

    return new_cord_list

def printpritty(cord_list):
    max_x = 0
    max_y = 0
    for x, y in cord_list:
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
    to_print = {}
    for j in range(max_y+1):
        to_print[j] = ["."]*(max_x+1)

    for x, y in cord_list:
        to_print[y][x] = "#"

    for key, term in to_print.items():
        for char in term:
            print(char, end="")
        print("")





cords, fs = get_input()
new_list = cords.copy()
for dir, num in fs:
    new_list = fold(new_list.copy(), dir, num)
printpritty(new_list)


