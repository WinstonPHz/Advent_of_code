import re
import math
import copy
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
            self.weight[material] = self.need[material] - prod
        self.weight[3] = 100
        return

    def can_build(self):
        can_build = []
        for material, cost1 in self.cost.items():
            cb = True
            for req, cost in cost1.items():
                if cost > self.have[req]:
                    cb = False
                    break
            if cb:
                can_build.append(material)
        return can_build

    def cant_build(self):
        cant_build = []
        for item, cost in self.cost.items():
            for material, quant in cost.items():
                if self.production[material] == 0:
                    cant_build.append(item)
        return cant_build

    def next_build(self):
        can_build = self.can_build()  # Have the materials
        cant_build = self.cant_build()# Not producing the materials needed
        if can_build == []:
            return -1
        if 3 in can_build:
            return 3
        # Which building do we actually really want based on the weight?
        self.calculate_weight()
        build_order_weight = {}
        for material, weight in self.weight.items():
            if material not in cant_build:
                build_order_weight[weight] = material
        order = list(build_order_weight.keys())
        order.sort()
        to_build = build_order_weight[max(order)]
        # If we want to build it and we can, we should
        if to_build in can_build:
            return to_build
        # we can build some things, but should we, will it slow down what we want or speed it up?
        reduced_time = [25,25,25,25]
        for test_build in can_build:
            cur_build_time = []
            # get the max of the current cost - what we have / production
            for item, quant in self.cost[to_build].items():
                # The costs of the next time
                if self.production[item] == 0:
                    # Cant build the next thing at all
                    break
                cur_build_time.append((quant-self.have[item])/self.production[item])
            time_to_build_current = math.ceil(max(cur_build_time))
            # Now time to get the future build time if we build this thing
            test_have = copy.deepcopy(self.have)
            test_prod = copy.deepcopy(self.production)
            for item, quant in self.cost[test_build].items():
                test_have[item] -= quant
            test_prod[test_build] += 1

            nxt_build_time = []
            # get the max of the current cost - what we have / production
            for item, quant in self.cost[to_build].items():
                # The costs of the next time
                if test_prod[item] == 0:
                    # Cant build the next thing at all
                    break
                nxt_build_time.append((quant - test_have[item]) / test_prod[item])
            time_to_build_future = math.ceil(max(nxt_build_time))
            print(f"if I build a {test_build} Next build time for {to_build} is {time_to_build_future} but current build time is {time_to_build_current}")
            if time_to_build_future <= time_to_build_current and self.weight[test_build] > 0:
                print("Adding to build list", test_build, time_to_build_future)
                reduced_time[test_build] = time_to_build_future
        if min(reduced_time) != 25:
            return reduced_time.index(min(reduced_time))
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
        while self.minute < self.min_max:
            print(self.minute, self.have, "Producing", self.production, "Weight", self.weight)
            self.inc_time()
            if to_build >= 0:
                print(f"Building a {to_build} robot, {self.weight}")
                self.build_robot(to_build)
            to_build = self.next_build()
        print(self.minute, self.have, "Producing", self.production, "Weight", self.weight)


bp_list = []
with open("input.txt", "r") as file:
    for line in file:
        line = line.strip("\n")
        bp_list.append(blueprint(line))
bp_list[0].run_simulation()
print("=========================================================================================================")
bp_list[1].run_simulation()
for bp in bp_list:
    print(bp.have, bp.production)


