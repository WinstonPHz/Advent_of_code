import copy
alf_list = "abcdefghijklmnopqrstuvwkyz"
itm_list = ["0"]
for char in alf_list.lower():
    itm_list.append(char)
for char in alf_list.upper():
    itm_list.append(char)

duplicates = []
groups = []
group = []
with open("input.txt", "r") as file:
    for line in file:
        line = line.strip("\n")
        n = int(len(line)/2)
        bag_a = []
        bag_b = []
        for i, char in enumerate(line):
            if i < n:
                bag_a.append(itm_list.index(char))
            else:
                bag_b.append(itm_list.index(char))
                if itm_list.index(char) in bag_a:
                    duplicates.append(itm_list.index(char))
                    break
        group.append(line)
        if len(group) == 3:
            groups.append(group)
            group = []

print("ans1:", sum(duplicates))
badge_nums = []
for gp in groups:
    g0 = gp[0]
    g1 = gp[1]
    g2 = gp[2]
    for char in g0:
        if char in g1 and char in g2:
            badge_nums.append(itm_list.index(char))
            break
print("ans2:", sum(badge_nums))

