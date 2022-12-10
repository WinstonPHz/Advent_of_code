class rope():
    def __init__(self, knots):
        self.pos = []
        self.knots = knots
        self.last_knot = knots-1
        for i in range(knots):
            self.pos.append([0,0])
        self.uniq_t = []

    def move(self, d, m):
        for i in range(int(m)):
            self.move_head(d)
            for j in range(1,self.knots):
                self.move_tail(j)

    def surounds(self, id):
        around_tail = []
        for i in range(-1,2):
            for j in range(-1,2):
                around_tail.append([self.pos[id][0]+i, self.pos[id][1]+j])
        if self.pos[id-1] in around_tail:
            return True
        return False

    def move_tail(self, id):
        if not self.surounds(id):
            if self.pos[id-1][0] > self.pos[id][0]:
                self.pos[id][0] += 1
            elif self.pos[id-1][0] < self.pos[id][0]:
                self.pos[id][0] -= 1
            if self.pos[id-1][1] > self.pos[id][1]:
                self.pos[id][1] += 1
            elif self.pos[id-1][1] < self.pos[id][1]:
                self.pos[id][1] -= 1
        if id == self.last_knot:
            self.uniq_t.append(str(self.pos[id]))

    def move_head(self, direct):
        if direct == "R":
            self.pos[0][0] += 1
        elif direct == "L":
            self.pos[0][0] -= 1
        elif direct == "U":
            self.pos[0][1] += 1
        elif direct == "D":
            self.pos[0][1] -= 1

    def get_uniq(self):
        self.uniq_t = list(dict.fromkeys(self.uniq_t))
        print(len(self.uniq_t))


r = rope(2)
r2 = rope(10)
with open("input.txt", "r") as file:
    for line in file:
        line = line.strip("\n")
        direction, magnitude = line.split(" ")
        r.move(direction, int(magnitude))
        r2.move(direction, int(magnitude))

print("Ans1:\n", end="")
r.get_uniq()
print("Ans2:\n", end="")
r2.get_uniq()