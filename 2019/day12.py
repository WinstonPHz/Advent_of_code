import copy


def calc_lcm(period):
    a = copy.copy(period)
    a.sort()
    for i in range(2):
        lcm = ((a[i] * a[i + 1]) / calc_gcf(a[i], a[i + 1]))
        a[i + 1] = int(lcm)
    return a[-1]

def calc_gcf(n1, n2):
    A = []
    B = []
    C = []
    for i in range(1, max([n1, n2])):
        if n1 % i == 0:
            A.append(i)
        if n2 % i == 0:
            B.append(i)
    for num in A:
        if num in B:
            C.append(num)
    return max(C)

class planet():
    def __init__(self, x, y, z):
        self.vel = [0,0,0]
        self.pos = [int(x), int(y), int(z)]
        self.initial = copy.copy(self.pos)
        self.step = 0

    def calc_vel(self, others):
        delta_v = [0,0,0]
        for pl in others:
            for i in range(3):
                comp = pl.pos[i]
                if comp > self.pos[i]:
                    delta_v[i] += 1
                elif comp < self.pos[i]:
                    delta_v[i] -= 1
        for i in range(3):
            self.vel[i] += delta_v[i]

    def calc_pos(self):
        self.step += 1
        for i in range(3):
            self.pos[i] += self.vel[i]

    def calc_energy(self):
        x = 0
        y = 0
        for i in range(3):
            x += abs(self.pos[i])
            y += abs(self.vel[i])
        return x*y

planets = []
with open("d12in.txt", "r") as input:
    for line in input:
        line = line.strip("<").strip(">\n").replace(" ", "").split(",")
        a = []
        for j in line:
            a.append(int(j.split("=")[1]))
        planets.append(planet(a[0], a[1], a[2]))
cumsum = 0
i = 0
periods = [0,0,0]
found = [False, False, False]
while True:
    for j in range(4):
        a = [0,1,2,3]
        a.pop(j)
        using = [planets[a[0]],planets[a[1]],planets[a[2]]]
        planets[j].calc_vel(using)
    for j in range(4):
        planets[j].calc_pos()
    i += 1
    for j in range(3):
        starting = []
        current = []
        if periods[j] != 0:
            if i%periods[j] == 0:
                for k in range(4):
                    starting.append(planets[k].initial[j])
                    starting.append(0)
                    current.append(planets[k].pos[j])
                    current.append(planets[k].vel[j])
                if starting != current:
                    print("Last one was false?", starting, current, i)
                    periods[j] = 0
                else:
                    print("Actually Got one", starting, current, i)
                    found[j] = True

        for k in range(4):
            starting.append(planets[k].initial[j])
            starting.append(0)
            current.append(planets[k].pos[j])
            current.append(planets[k].vel[j])
        if starting == current and not found[j]:
            print("Got one?", starting, current, i)
            periods[j] = i
    if all(found):
        break
    if i==999:
        for j in range(4):
            cumsum += planets[j].calc_energy()



print("Ans 1:", cumsum)
print(periods)
print("Ans 2:", calc_lcm(periods))
print(periods)



"""
Day08_LCM List:
[28482, 174135, 185685]   435434667330
[111779, 170407, 181816]  33463217359620248
[28482, 165940, 190199]   449469059756460
[110544, 186028, 196787]  1011695704306896
"""