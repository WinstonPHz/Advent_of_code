import re
class blueprint():
    def __init__(self, line):
        self.id = 0
        self.need = {0: 0, 1: 0, 2: 0, 3: 0}
        # 0 = ore
        # 1 = clay
        # 2 = obsidian
        # 3 = Geode
        self.production = {0: 1, 1: 0, 2: 0, 3: 0}
        self.have = {0: 0, 1: 0, 2: 0, 3: 0}
        self.cost = {}
        self.weight = {0: 1, 1: 1, 2: 1, 3:1}
        components = line.split(". ")
        for i, comp in enumerate(components):
            if i == 0:
                bp, ore = comp.split(": ")
                self.id = int(bp.split(" ")[1])
                self.cost[i] = {0: int(ore.split("costs ")[1].split(" ")[0])}
                continue
            costs = re.findall("\d+", comp)
            if i == 1:
                self.cost[i] = {0: int(costs[0])}
            if i == 2:
                self.cost[i] = {0: int(costs[0]), 1: int(costs[1])}
            if i == 3:
                self.cost[i] = {0: int(costs[0]), 2: int(costs[1])}
        self.minute = 0
        self.min_max = 24
        self.quality_level = 0

    def calculate_need(self):
        # We always want to produce a geode robot
        # We need to produce Obsidean and Clay Robots
        # How much do we really need the other robots
        for material, cost in self.cost.items():
            # Set up the raw cost of each as a need
            for item, quatn in cost.items():
                if self.need[item] < quatn:
                    self.need[item] = quatn
        return

    def calculate_weight(self):
        for material, prod in self.production.items():
            self.weight[material] = (self.need[material] - prod - self.have[material])
            for m1 in self.cost[material]:
                if self.production[m1] == 0:
                    self.weight[material] = 0
        if self.production[2] != 0 and self.production[1] != 0:
            turns_to_geo = max([(self.cost[3][0]-self.have[0])/self.production[0], (self.cost[3][2]-self.have[2])/self.production[2]])
            print("Turns to geo", turns_to_geo)
            if turns_to_geo < 3:
                self.weight[3] = 100
        return

    def next_build(self):
        can_build = []
        for material, cost1 in self.cost.items():
            cb = True
            for req, cost in cost1.items():
                if cost > self.have[req]:
                    cb = False
                    break
            if cb:
                print("Can Build", material, cost1, self.have)
                can_build.append(material)
        if can_build == []:
            return -1
        if 3 in can_build:
            return 3
        # If building will slow down next building don't build, if it won't do build
        for test_build in can_build:
            sim_next = self.
turns_to_geo = max([(self.cost[3][0]-self.have[0])/self.production[0], (self.cost[3][2]-self.have[2])/self.production[2]])

            next_ingrediants = self.cost[test_build+1]
            for material, ingrediant in next_ingrediants:

            print("nxt", next_ingrediants)






        build_order_weight = {}
        for material, weight in self.weight.items():
            build_order_weight[weight] = material
        order = list(build_order_weight.keys())
        order.sort()
        to_build = build_order_weight[max(order)]
        print(can_build, to_build)
        if to_build in can_build:
            return to_build
        else:
            return -1

    def inc_time(self):
        self.minute += 1
        # Produce this many products
        for key in self.production:
            self.have[key] += self.production[key]

    def build_robot(self, robot_id):
        cost_to_build = self.cost[robot_id]
        for req, cost in cost_to_build.items():
            self.have[req] -= cost
        self.production[robot_id] += 1
        return

    def run_simulation(self):
        to_build = self.next_build()
        self.calculate_need()
        self.calculate_weight()
        while self.minute < self.min_max:
            print(self.minute, self.have, "Producing", self.production, "Weight", self.weight)
            self.inc_time()
            if to_build >= 0:
                print(f"Building a {to_build} robot, {self.weight}")
                self.build_robot(to_build)
            self.calculate_weight()
            to_build = self.next_build()
        print(self.minute, self.have, "Producing", self.production, "Weight", self.weight)


bp_list = []
with open("input.txt", "r") as file:
    for line in file:
        line = line.strip("\n")
        bp_list.append(blueprint(line))
bp_list[1].run_simulation()


