elf_sum = []
with open("input.txt", "r") as puz:
    total = 0
    for line in puz:
        if line == "\n":
            elf_sum.append(total)
            total = 0
        else:
            total += int(line)

print("Ans 1:", max(elf_sum))

ans_2 = 0
for i in range(3):
    ans_2 += max(elf_sum)
    elf_sum.remove(max(elf_sum))

print("Ans 2:", ans_2)
