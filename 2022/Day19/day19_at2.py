import re
import math
import copy
import json

class blueprint():
    def __init__(self, line):
        self.id = 0
        self.need = [0, 0, 0, 0]
        # 0 = ore
        # 1 = clay
        # 2 = obsidian
        # 3 = Geode
        self.production = [1, 0, 0, 0]
        self.have = [0, 0, 0, 0]
        self.cost = {}
        self.weight = [1, 1, 1, 1]
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
        self.cur_state = str([self.minute]+self.production+self.have)
        self.saved_states = {}
        self.max_geodes = []

    def calculate_need(self):
        # We need to produce Obsidean and Clay Robots
        # How much do we really need the other robots
        for material, cost in self.cost.items():
            # Set up the raw cost of each as a need
            for item, quatn in cost.items():
                if self.need[item] < quatn:
                    self.need[item] += quatn
        return

    def time_to_build(self, robot, production, stored):
        times = []
        for material, quant in self.cost[robot].items():
            mat_need = quant - stored[material]
            times.append(math.ceil(mat_need/production[material]))
        if max(times) <= 0:
            return 1
        else:
            return max(times)

    def calc_new_storage(self, time_diff, production, stored, built_bot = -1):
        for i in range(4):
            stored[i] += time_diff*production[i]
        if built_bot >= 0:
            for material, cost in self.cost[built_bot].items():
                stored[material] -= cost
            production[built_bot] += 1
        return production, stored


    def search(self, state):
        if state in self.saved_states:
            return self.saved_states[state]
        state = json.loads(state)
        minute = state[0]
        production = copy.deepcopy(state[1:5])
        stored = copy.deepcopy(state[5:])
        print(minute, production, stored)
        max_geo = 0
        can_build_list = []
        for robot, requirements in self.cost.items():
            if production[robot] >= self.need[robot]:
                # Don't waste time if we have more production per min and needed
                continue
            can_build = True
            for material in requirements.keys():
                if production[material] == 0:
                    # Can't even build this thing, break
                    can_build = False
                    break
            if can_build:
                can_build_list.append(robot)

        print(f"Can build these: {can_build_list}")
        can_build_list.sort()
        for robot in can_build_list[::-1]:
            time_taken = self.time_to_build(robot, production, stored)
            print(f"It will take {time_taken}")
            new_min = minute + time_taken
            if new_min >= self.min_max:
                new_prod, new_stored = self.calc_new_storage(self.min_max - minute, production, stored)
                self.saved_states[str([new_min] + new_prod + new_stored)] = new_stored[3]
                self.max_geodes.append(new_stored[3])
                print("Got to a max min!")
                continue
        new_prod, new_stored = self.calc_new_storage(time_taken, production, stored, robot)
        max_geo += self.search(str([new_min] + new_prod + new_stored))
        self.saved_states[str(state)] = max_geo
        return max_geo



    def run(self):
        self.calculate_need()
        ans = self.search(self.cur_state)
        print("Max Geodes", ans, self.id)

bp_list = []
with open("input.txt", "r") as file:
    for line in file:
        line = line.strip("\n")
        bp_list.append(blueprint(line))
bp_list[0].run()
print("=========================================================================================================")
#bp_list[1].run()


