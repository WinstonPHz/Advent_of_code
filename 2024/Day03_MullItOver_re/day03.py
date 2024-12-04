import re

answer1 = 0
answer2 = 0
with open("input.txt", "r") as file:
    for line in file:
        all_multies = re.findall("mul\(\d+,\d+\)|do\(\)|don't\(\)", line)
        print(all_multies)
        toggle = 1
        for multi in all_multies:
            if multi == "do()":
                toggle = 1
                continue
            elif multi == "don't()":
                toggle = 0
                continue

            x, y = re.findall("\d+", multi)
            answer1 += int(x)*int(y)
            if toggle:
                answer2 += int(x)*int(y)
print("Answer 1:", answer1)
print("Answer 2:", answer2)
