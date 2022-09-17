input = []
for line in open("puz", "r+"):
    input.append(int(line))
cur_depth = sum(input[0:3])
counter = 0
for i, value in enumerate(input[1:-1]):
    depth = sum(input[i:i+3])
    print(depth)
    if int(depth) > int(cur_depth):
        counter += 1
    cur_depth = depth
print(counter)
