scaner_locals = []

with open("input2.txt","r") as puz:

    for line in puz:
        if "---" in line:
            break
        x, y, z = line.split("[")[1].split("]")[0].split(",")
        scaner_locals.append([int(x), int(y), int(z)])

mand_dist = []
for i, scan_a in enumerate(scaner_locals):
    for j, scan_b in enumerate(scaner_locals):
        if i == j:
            continue
        dx = abs(scan_a[0] - scan_b[0])
        dy = abs(scan_a[1] - scan_b[1])
        dz = abs(scan_a[2] - scan_b[2])
        mand_dist.append(abs(dx+dy+dz))
print(mand_dist)
print(max(mand_dist))
