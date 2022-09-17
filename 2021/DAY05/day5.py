
def get_input():
    vents = {}
    i = 0
    for line in open("puz", "r+"):
        line = line.strip("\n")
        number_list = line.split(" -> ")
        vents[i] = []
        for number in number_list:
            for n in number.split(","):
                vents[i].append(int(n))
        i += 1
    return vents

def get_space(n):
    space = {}
    for i in range(n):
        space[i] = [0] * n
    return space

def add_vent_to_space(x1, y1, x2, y2, space):
    x_dif = abs(x1-x2)
    y_dif = abs(y1-y2)
    x_min = min([x1,x2])
    y_min = min([y1,y2])
    if x_dif == 0:
        for i in range(y_dif+1):
            space[y_min+i][x1] += 1
    elif y_dif == 0:
        for i in range(x_dif+1):
            space[y1][x_min+i] += 1
    else:
        # got a diagonal
        for i in range(x_dif+1):
            if x2 > x1 and y2 > y1: # Right (+) Down (+)
                space[y1 + i][x1 + i] += 1
            elif x2 > x1 and y2 < y1: # Right (+) Up (-)
                space[y1 - i][x1 + i] += 1
            elif x2 < x1 and y2 > y1: # Left (-) Down (+)
                space[y1 + i][x1 - i] += 1
            elif x2 < x1 and y2 < y1: # Left (-) Up (-)
                space[y1 - i][x1 - i] += 1
    return space

def printpritty(space):
    print("y x0, 1, 2, 3, 4, 5, 6, 7, 8, 9")
    for key in space:

        print(key, space[key])

def get_ans_1(space):
    cum_sum = 0
    for key in space:
        for pos in space[key]:
            if pos > 1:
                cum_sum += 1
    print("answer 1:", cum_sum)

hvents = get_input()
space = get_space(1000)
for key, item in hvents.items():
    space = add_vent_to_space(item[0], item[1], item[2], item[3], space)
#printpritty(space)
get_ans_1(space)
