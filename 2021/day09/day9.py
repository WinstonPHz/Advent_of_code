def get_input():
    i = 0
    heatmap = {}
    for line in open("puz", "r+"):
        line = line.strip("\n")
        heatmap[i] = [9]
        for val in line:
            heatmap[i].append(int(val))
        heatmap[i].append(9)
        i += 1
        j = len(line)
    heatmap[-1] = [9]*(j+2)
    heatmap[i] = [9]*(j+2)
    return heatmap, i, j+2

def eval_low_point(heatmap, x, y):
    low_points = []
    basen_center={}
    basen_count = 0
    for j in range(x):
        for i in range(1, y-1):
            val = heatmap[j][i]
            check = [heatmap[j-1][i], heatmap[j+1][i], heatmap[j][i+1], heatmap[j][i-1]]
            ticks = 0
            for cv in check:
                if val < cv:
                    ticks += 1
            if ticks == 4:
                low_points.append(val + 1)
                basen_center[basen_count] = [j, i]
                basen_count += 1
    print("answer 1:", sum(low_points))
    return basen_center

def printpritty(array):
    for key, value in sorted(array.items()):
        print(key, value)

def sum_basen(basen, map):
    basen_points = [basen]
    while True:
        cur_len = len(basen_points)
        for j, i in basen_points:
            if map[j - 1][i] != 9 and [j-1, i] not in basen_points:
                basen_points.append([j-1, i])
            if map[j + 1][i] != 9 and [j + 1, i] not in basen_points:
                basen_points.append([j+1, i])
            if map[j][i+1] != 9 and [j, i+1] not in basen_points:
                basen_points.append([j, i+1])
            if map[j][i-1] != 9 and [j, i-1] not in basen_points:
                basen_points.append([j, i-1])
        if cur_len == len(basen_points): break
    return len(basen_points)


map, x, y = get_input()
#printpritty(map)
basens = eval_low_point(map, x, y)
basen_sizes = []
for key, basen in basens.items():
    basen_sizes.append(sum_basen(basen, map))

ans = 1
for i in range(3):
    maxim = max(basen_sizes)
    basen_sizes.remove(maxim)
    ans *= maxim
print("Answer 2:", ans)
