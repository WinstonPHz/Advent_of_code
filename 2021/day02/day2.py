depth = 0
horizon = 0
aim = 0
for line in open("puz", "r+"):
    if "forward" in line:
        horizon += int(line.split()[1])
    elif "down" in line:
        depth += int(line.split()[1])
    elif "up" in line:
        depth -= int(line.split()[1])
print("answer 1:", depth*horizon)

depth = 0
horizon = 0
aim = 0
for line in open("puz", "r+"):
    if "forward" in line:
        horizon += int(line.split()[1])
        depth += aim * int(line.split()[1])
    elif "down" in line:
        aim += int(line.split()[1])
    elif "up" in line:
        aim -= int(line.split()[1])
print("answer 2:", depth*horizon)
