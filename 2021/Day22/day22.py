import copy

x_points = []
y_points = []
z_points = []

with open("input.txt","r") as puz:
    for line in puz:
        if "----" in line:
            break
        components = line.split(",")
        x1, x2 = components[0].split("=")[1].split("..")
        y1, y2 = components[1].split("=")[1].split("..")
        z1, z2 = components[2].split("=")[1].split("..")
        x_points += [int(x1), int(x2)+1]
        y_points += [int(y1), int(y2)+1]
        z_points += [int(z1), int(z2)+1]

x_points.sort()
y_points.sort()
z_points.sort()
x_points = list(dict.fromkeys(x_points))
y_points = list(dict.fromkeys(y_points))
z_points = list(dict.fromkeys(z_points))

grid = []
lx = len(x_points)
ly = len(y_points)
lz = len(z_points)
print(lx, ly, lz)
for i in range(len(x_points)):
    grid1 = []
    for j in range(len(y_points)):
        grid1.append(copy.deepcopy([0]*(len(z_points))))
    grid.append(copy.deepcopy(grid1))

with open("input.txt","r") as puz:
    for line in puz:
        if "----" in line:
            break
        components = line.split(",")
        x1, x2 = components[0].split("=")[1].split("..")
        y1, y2 = components[1].split("=")[1].split("..")
        z1, z2 = components[2].split("=")[1].split("..")
        for i in range(x_points.index(int(x1)), x_points.index(int(x2)+1)):
            for j in range(y_points.index(int(y1)), y_points.index(int(y2)+1)):
                for k in range(z_points.index(int(z1)), z_points.index(int(z2)+1)):
                    if "on" in line:
                        grid[i][j][k] = 1
                    elif "off" in line:
                        grid[i][j][k] = 0

# Now I need to just get the answer
cumsum = 0
for i in range(lx):
    for j in range(ly):
        for k in range(lz):
            if grid[i][j][k] == 1:
                dx = (x_points[i+1] - x_points[i])
                dy = (y_points[j+1] - y_points[j])
                dz = (z_points[k+1] - z_points[k])
                cumsum += dx*dy*dz

print("Answer:", cumsum)


