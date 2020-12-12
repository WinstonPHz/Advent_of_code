file1 = open("input.txt", "r")
inputs = ""
for line in file1:
    inputs += line
inputs_arr = inputs.split("\n")
indexes = []
for index in inputs_arr:
    indexes.append(int(index))
indexes.sort()
ones = 0
twos = 0
threes = 1
for i in range(len(indexes)):
    if i == 0:
        if indexes[i]== 1:
            ones += 1
        elif indexes[i] == 2:
            twos += 1
        elif indexes[i] == 3:
            threes += 1
    else:
        if indexes[i]-indexes[i-1] == 1:
            ones +=1
        elif indexes[i]-indexes[i-1] == 2:
            twos += 1
        elif indexes[i]-indexes[i-1] == 3:
            threes += 1

print("Answer 1:", ones*threes)
connections = 1
perms = {}
def permutations(value, set):
    if value in perms:
        return perms[value]
    if value == 0:
        perms[value] = 1
        return perms[value]
    if not (value in set):
        perms[value] = 0
        return 0
    perms[value] = permutations(value-1, set) + permutations(value-2, set)+permutations(value-3, set)
    return perms[value]

print("Answer 2:", permutations(max(indexes), indexes))