file1 = open("input.txt", "r")
from copy import deepcopy

inputs = ""
for line in file1:
    inputs += line
puzzle = inputs.split("\n")
buses = puzzle[0].split(",")
##### Part 1
mask = ""
memory = {}
value = ""
for i, puz in enumerate(puzzle):
    address = ""
    value = ""
    for i in range(36):
        value += "0"
    if puz[0:4] == "mask":
        mask = puz.split(" = ")[1]
    elif puz[0:3] == "mem":
        for j, v in enumerate(puz):
            if j > 3:
                if v == "]":
                    break
                address += v
        bin_value  = str(bin(int(puz.split(" = ")[1])))[2:]
        value = value[0:36-len(bin_value)]+bin_value
        for k, bi in enumerate(mask):
            if bi == "X":
                continue
            elif bi == "1":
                value = value[0:k]+"1"+value[k+1:]
            elif bi == "0":
                value = value[0:k] + "0" + value[k + 1:]
        memory[address] = value
sum = 0
for key in memory:
    sum += int(memory[key],2)
print("Answer 1: ",sum)


##### Part 2
def change_x(masks, xs):
    if len(xs) == 0:
        return masks
    x_loc = xs[0]
    xs.pop(0)
    new_masks = []
    for j, mask in enumerate(masks):
        new_masks.append(mask[0:x_loc]+"1"+mask[x_loc+1:])
        new_masks.append(mask[0:x_loc]+"0"+mask[x_loc+1:])
    return change_x(new_masks, xs)

mask = ""
addresses = []
dic_addresses = {}
for i, puz in enumerate(puzzle):
    address = ""
    value = ""
    for i in range(36):
        address += "0"
    if puz[0:4] == "mask":
        mask = puz.split(" = ")[1]
    elif puz[0:3] == "mem":
        result = ""
        for j, v in enumerate(puz):
            if j > 3:
                if v == "]":
                    break
                result += v
        bin_result = str(bin(int(result)))[2:]
        address = address[0:36-len(bin_result)]+bin_result
        xes = []
        for k, bi in enumerate(mask):
            if bi == "X":
                address = address[0:k]+"X"+address[k+1:]
                xes.append(k)
            elif bi == "1":
                address = address[0:k]+"1"+address[k+1:]
            elif bi == "0":
                continue
        addresses = change_x([address], xes)
        for ad in addresses:
            dic_addresses[ad] = puz.split(" = ")[1]

tots = 0
for key in dic_addresses:
    tots += int(dic_addresses[key])

print("Answer 2:", tots)
