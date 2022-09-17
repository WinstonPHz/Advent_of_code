
def get_input():
    for line in open("puz", "r+"):
        line = line.strip("\n")
        if line != "":
            out = line.split(",")
            print(line)
    output = {}
    for i in range(9):
        output[i] = 0
    for number in out:
        output[int(number)]+=1
    return output

def get_sum(population):
    cum_sum = 0
    for key, number in population.items():
        cum_sum += number
    return cum_sum

curr_pop = get_input()
print(curr_pop)
for i in range(256):
    new_lf = curr_pop[0]
    for j in range(8):
        curr_pop[j] = curr_pop[j+1]
        if j == 6:
            curr_pop[j] += new_lf
    curr_pop[8] = new_lf
    if i == 79: print("Answer 1:", get_sum(curr_pop))

print("Answer 2:", get_sum(curr_pop))
