file1 = open("input.txt", "r")
inputs = ""
for line in file1:
    inputs += line
inputs_arr = inputs.split("\n")
indexes = []
for index in inputs_arr:
    indexes.append(int(index))

preamble = 25
curr_index = 0
check = False
weakness = 0
while True:
    array1 = indexes[curr_index:curr_index+preamble]
    for i in range(len(array1)):
        for j in range(len(array1)):
            if i != j:
                if array1[i]+array1[j] == indexes[curr_index+preamble]:
                    check = True
    if check == True:
        curr_index += 1
        check = False
        continue
    elif check == False:
        weakness = (indexes[curr_index+preamble])
        break
curr_range = 2
curr_index = 0
found_it = False
print("Answer 1:", weakness)
while not found_it:
    for i in range(len(indexes)):
        if sum(indexes[curr_index+i:curr_index+i+curr_range]) == weakness:
            print("Answer 2:", max(indexes[curr_index+i:curr_index+i+curr_range])+min(indexes[curr_index+i:curr_index+i+curr_range]))
            found_it = True
            print("Current Range:", curr_range)
            break
    curr_range += 1