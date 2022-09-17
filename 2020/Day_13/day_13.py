file1 = open("input.txt", "r")
from copy import deepcopy

inputs = ""
for line in file1:
    inputs += line
puzzle = inputs.split("\n")
buses = puzzle[0].split(",")
id = []
for i, bus in enumerate(buses):
    if not bus == "x":
        id.append(int(bus))
    else:
        id.append(0)

def part_one(): # not called ever it will fail.
    next_bus = {}
    for i, sched in enumerate(id):
        next_time = 0
        while True:
            next_time += sched
            if next_time > time:
                print(next_time)
                next_bus[sched] = next_time - time
                break

print(id)
time = 0
found_it = True
while found_it:
    freq_found = 1
    for i, freq in enumerate(id):
        if freq == 0:
            continue
        if (time + i) % freq == 0:
            freq_found *= freq
            if freq == id[-1]:
                print(time)
                found_it = False
            continue
        else:
            time += freq_found
            break



