def check_decending(levels):
    unsorted_list = levels.copy()
    sorted_list = levels.copy()
    sorted_list.sort()
    if unsorted_list == sorted_list[::-1]:
        return check_adjacent(levels)
    else:
        return False

def check_ascending(levels):
    unsorted_list = levels.copy()
    sorted_list = levels.copy()
    sorted_list.sort()
    if unsorted_list == sorted_list:
        return check_adjacent(levels)
    else:
        return False

def check_adjacent(levels):
    for i in range(len(levels) -1):
        delta = abs(levels[i+1] - levels[i])
        if 1 <= delta <= 3:
            continue
        else:
            return False
    return True

def check_dampen(levels):
    possible_levels = []
    for i in range(1, len(levels)):
        possible_levels.append(levels[0:i-1] + levels[i:])
    possible_levels.append(levels[:-1])
    print(possible_levels)
    for level in possible_levels:
        if level[0] > level[1]:
            if check_decending(level):
                return True
        elif level[0] < level[1]:
            if check_ascending(level):
                return True
    return False


safe = 0
safe_2 = 0
with open("input.txt", "r") as file:
    for line in file:
        levels = [int(level) for level in line.split(" ")]
        if levels[0] > levels[1]:
            if check_decending(levels):
                safe += 1
                continue
        elif levels[0] < levels[1]:
            if check_ascending(levels):
                safe += 1
                continue
        if check_dampen(levels):
            print(levels)
            safe_2 += 1

safe_2 += safe
print("answer 1: ", safe)
print("answer 2: ", safe_2)
