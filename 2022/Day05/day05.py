
crates = {}
num_index = []
with open("input.txt", "r") as file:
    for line in file:
        line = line.strip("\n")
        if "1" in line:
            for i, char in enumerate(line):
                if char != " ":
                    crates[int(char)] = []
                    num_index.append(i)
            break
    print(num_index)
with open("input.txt", "r") as file:
    for line in file:
        if "[" in line:
            for i in range(9):
                box = line[num_index[i]]
                if box != " ":
                    crates[i+1].append(box)
        if line == "\n":
            break
start = False
instructions = []
with open("input.txt", "r") as file:
    for line in file:
        if line == "\n":
            start = True
            continue
        if start:
            # Replace to from with commas
            a,b,c = line.split(",")
            instructions.append([int(a), int(b), int(c)])


def move_crate_p1(num_to_move, From, To):
    for i in range(num_to_move):
        box = crates[From].pop(0)
        crates[To] = [box] + crates[To]
    return

def move_crate_p2(num_to_move, From, To):
    box = []
    for i in range(num_to_move):
        popped = crates[From].pop(0)
        box.append(popped)
    crates[To] = box + crates[To]

for inst in instructions:
    a,b,c = inst
    move_crate_p2(a,b,c)

def read_tops():
    for key in crates.keys():
        print(crates[key][0], end="")
    print()



read_tops()