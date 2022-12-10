class computer():
    def __init__(self, check_intervals):
        self.checks = check_intervals
        self.cycle = 0
        self.total = 0
        self.register = 1
        self.img = []

    def noop(self):
        self.cycle += 1
        self.check()

    def addx(self, X):
        self.cycle += 1
        self.check()
        self.cycle += 1
        self.check()
        self.register += X

    def check(self):
        if self.cycle in self.checks:
            self.total += self.cycle*self.register

        if self.register - 1 <= (self.cycle-1)%40 <= self.register + 1:
            self.img.append("#")
        else:
            self.img.append(" ")


    def display(self):
        for i, char in enumerate(self.img):
            if i%40 == 0:
                print()
            print(char, end="")


c1 = computer([20,60,100,140,180,220])
with open("input.txt") as file:
    for line in file:
        line = line.strip("\n")
        if "noop" in line:
            c1.noop()
        if "add" in line:
            trash, value = line.split(" ")
            c1.addx(int(value))


print("Ans 1:" , c1.total)
c1.display()