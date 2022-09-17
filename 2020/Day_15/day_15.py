inputs = "10,16,6,0,1,17"
inputs = inputs.split(",")

tries = [2020,30000000]
for j, tri in enumerate(tries):
    Input = {}
    for i, input in enumerate(inputs):
        Input[int(input)] = i
    cur_number = 0
    i = len(inputs)
    while i < tri-1:
        if cur_number in Input:
            Interval = i-Input[cur_number]
            Input[cur_number] = i
            cur_number = Interval
        else:
            Input[cur_number] = i
            cur_number = 0

        i += 1
    print(f"Answer {j+1}: {cur_number}")

# Original Part 1
# Part 1
# while True:
#    cur_number = Input[-1]
#    new_input = Input.copy()
#    new_input.pop(-1)
#    occurences = []
#
#    if cur_number in new_input:
#        for i,number in enumerate(Input):
#            if cur_number == number:
#                occurences.append(i)
#        Input.append(occurences[-1]-occurences[-2])
#    else:
#        Input.append(0)
#    if len(Input) == 2020:
#        print("Answer: ", Input[-1])
#        break

