import copy
buffer = []
puz = []
with open("input.txt", "r") as file:
    for line in file:
        line = line.strip("\n")
        for char in line:
            puz.append(char)
first = False
for i, char in enumerate(puz):
    if i > 3:
        if not first:
            buffer = puz[i-4:i]
            buffer = list(dict.fromkeys(buffer))
            if len(buffer) == 4:
                first = True
                print("Part 1:", i)
        if first and i > 13:
            buffer = puz[i - 14:i]
            buffer = list(dict.fromkeys(buffer))
            if len(buffer) == 14:
                print("Part 2:", i)
