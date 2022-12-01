
def get_input():
    for line in open("puz", "r+"):
        line = line.strip("\n")
        if line != "":
            out = line.split(",")
            print(line)

    output = []
    for number in out:
        output.append(int(number))
    return output

def calc_fuel(tpos, all_pos):
    fuel = 0
    for pos in all_pos:
        fuel += abs(tpos - pos)
    return fuel

def calc_fuel2(tpos, all_pos):
    fuel = 0
    for pos in all_pos:
        fuel += (1+abs(tpos - pos))*abs(tpos - pos)/2
    return fuel

crab_initial = get_input()
fuel_per_pos = []
fuel_per_pos2 = []
for i in range(max(crab_initial)):
    fuel_per_pos.append(calc_fuel(i,crab_initial))

for i in range(max(crab_initial)):
    fuel_per_pos2.append(calc_fuel2(i,crab_initial))

print("Answer 1:", min(fuel_per_pos))
print("Answer 2:", min(fuel_per_pos2))
