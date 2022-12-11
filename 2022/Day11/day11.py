class monkey():
    def __init__(self):
        self.items = []
        self.operation = ""
        self.oper2 = ""
        self.test = 0
        self.false_to = 0
        self.true_to = 0
        self.num_inspected = 0
        self.devide = 1

    def add_item(self, item):
        self.items.append(int(item))

    def add_opertation(self, op, value2):
        self.operation = op
        self.oper2 = value2

    def add_test(self, test_num):
        self.test = test_num

    def add_conditional(self, t, f):
        self.true_to = t
        self.false_to = f

    def inspect(self):
        self.num_inspected += 1
        item_to_inspect = self.items[0]
        if self.oper2 == "old":
            v2 = int(item_to_inspect)
        else:
            v2 = int(self.oper2)

        if self.operation == "*":
            item_to_inspect *= v2
        if self.operation == "+":
            item_to_inspect += v2
        item_to_inspect = int(item_to_inspect/3)
        self.items[0] = item_to_inspect

    def throw(self):
        tossed = []
        while self.items != []:
            self.inspect()
            item = self.items.pop(0)
            if item % self.test == 0:
                destination = self.true_to
            else:
                destination = self.false_to
            tossed.append([destination, item])
        return tossed

    def inspect2(self):
        self.num_inspected += 1
        item_to_inspect = self.items[0]
        if self.oper2 == "old":
            v2 = int(item_to_inspect)
        else:
            v2 = int(self.oper2)

        if self.operation == "*":
            item_to_inspect *= v2
        if self.operation == "+":
            item_to_inspect += v2
        self.items[0] = item_to_inspect

    def throw2(self):
        tossed = []
        while self.items != []:
            self.inspect2()
            item = self.items.pop(0)
            item %= self.devide
            if item % self.test == 0:


                destination = self.true_to
            else:
                destination = self.false_to
            tossed.append([destination, item])
        return tossed

monkeys = []
monkeys2 = []
true = 0
false = 0
to_dev = 1
with open("input.txt", "r") as file:
    for line in file:
        line = line.strip("\n")
        if "Monkey" in line:
            monkeys.append(monkey())
            monkeys2.append(monkey())
        if "Starting items:" in line:
            line = line.strip("Starting items: ")
            items = line.split(", ")
            for item in items:
                monkeys[-1].add_item(item)
                monkeys2[-1].add_item(item)
        if "Operation" in line:
            if "*" in line:
                val = line.split("* ")[1]
                monkeys[-1].add_opertation("*", val)
                monkeys2[-1].add_opertation("*", val)
            if "+ " in line:
                val = line.split("+ ")[1]
                monkeys[-1].add_opertation("+", val)
                monkeys2[-1].add_opertation("+", val)
        if "Test" in line:
            test = int(line.split("by ")[1])
            to_dev *= int(test)
            monkeys[-1].add_test(test)
            monkeys2[-1].add_test(test)
        if "throw to " in line:
            if "true" in line:
                true = int(line.split("monkey ")[1])
            if "false" in line:
                false = int(line.split("monkey ")[1])
                monkeys[-1].add_conditional(true, false)
                monkeys2[-1].add_conditional(true, false)

for monk in monkeys2:
    monk.devide = to_dev

for i in range(20):
    for monk in monkeys:
        thrown = monk.throw()
        if thrown != []:
            for to_m, item in thrown:
                monkeys[to_m].add_item(item)

business = []
for monk in monkeys:
    business.append(monk.num_inspected)
max1 = max(business)
business.remove(max1)
max2 = max(business)
print("Ans 1:", max1*max2)

for i in range(10000):
    for monk in monkeys2:
        thrown = monk.throw2()
        if thrown != []:
            for to_m, item in thrown:
                monkeys2[to_m].add_item(item)

business = []
for monk in monkeys2:
    business.append(monk.num_inspected)
max1 = max(business)
business.remove(max1)
max2= max(business)
print("Ans 2:", max1*max2)