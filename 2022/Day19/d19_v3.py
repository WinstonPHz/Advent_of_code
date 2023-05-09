import math
import copy
class Geodecracker:
    def __init__(self, blueprint, duration):
        self.bp_id = int(blueprint.split(":")[0].split("Blueprint ")[1])
        self.production = [1, 0, 0, 0]
        self.stored = [0, 0, 0, 0]
        self.costs = self.decodebp(blueprint)
        self.maximum_cost = [0,0,0,0]
        self.max_cost()
        #print(self.maximum_cost)
        self.duration = duration
        #print(self.costs)
        self.states = []
        self.current_max = 0
        self.test()
        # Current time, production, stored

    def max_cost(self):
        for material, costs in self.costs.items():
            for mat, quant in costs.items():
                if quant > self.maximum_cost[mat]:
                    self.maximum_cost[mat] = quant
    def decodebp(self, line):
        ore, clay, obsidian, geode = line.split(". ")
        costs = {}
        costs[0] = {}
        costs[0][0] = int(ore.split('costs ')[1].split(' ore')[0])
        costs[1] = {}
        costs[1][0] = int(clay.split('costs ')[1].split(' ore')[0])
        costs[2] = {}
        costs[2][0] = int(obsidian.split('costs ')[1].split(' ore')[0])
        costs[2][1] = int(obsidian.split('and ')[1].split(' clay')[0])
        costs[3] = {}
        costs[3][0] = int(geode.split('costs ')[1].split(' ore')[0])
        costs[3][2] = int(geode.split('and ')[1].split(' obsidian')[0])
        return costs

    def time_to_build(self, state):
        curent_time, production, stored = state
        # Returns the amount of time until we have enough to build a robot
        ttb_robots = {}
        for robot, cost in self.costs.items():
            ttb = []
            for material, quant in cost.items():
                if production[material] == 0:
                    ttb_robots[robot] = -1
                    break
                else:
                    top = quant-stored[material] if quant-stored[material] >= 0 else 0
                    ttb.append(math.ceil(top/production[material]))
            if robot not in ttb_robots.keys():
                ttb_robots[robot] = max(ttb)
        return ttb_robots

    def build_next_robot(self, robot, build_time, state):
        curent_time, production, stored = copy.deepcopy(state)
        # Go to the next node point
        delta_time = 1 + build_time
        curent_time += delta_time
        for i, quant in enumerate(production): # Gain all the resources at once
            stored[i] += quant*delta_time
        for material, quant in self.costs[robot].items(): # Build the robot
            stored[material] -= quant
        production[robot] += 1
        return (copy.copy(curent_time), copy.copy(production), copy.copy(stored))

    def node_hop(self, state):
        start_state = copy.deepcopy(state)
        next_nodes_at = self.time_to_build(state)
        for robot, time in next_nodes_at.items():
            if time < 0: # skip the ones we can not build
                continue
            if robot != 3:
                if start_state[1][robot] >= self.maximum_cost[robot]:
                    # skip the ones that we don't need
                    continue
            #print(start_state, "Trying", robot, next_nodes_at)
            next_state = copy.deepcopy(self.build_next_robot(robot, time, start_state))
            if not (self.max_check(next_state) >= self.current_max):
                # if the next state can not increase our current max, don't bother
                continue
            if next_state[0] >= self.duration:
                self.update_current_max(start_state)
            else:
                self.node_hop(next_state)

    def update_current_max(self, state):
        curent_time, production, stored = state
        fake_stored = stored[3]
        if curent_time == self.duration:
            if stored[3] > self.current_max:
                self.current_max = stored[3]
        elif curent_time > self.duration:
            print("I think you should never see this message")
            return
        elif curent_time < self.duration:
            for i in range(curent_time, self.duration):
                fake_stored += production[3]
            if fake_stored > self.current_max:
                self.current_max = fake_stored


    def max_check(self, state):
        curent_time, production, stored = state
        fake_store = stored[3]
        fake_prod = production[3]
        for i in range(curent_time, self.duration):
            # If we make a geode robot every turn from now on how many will we get?
            fake_store += fake_prod
            fake_prod += 1
        return fake_store



    def test(self):
        production = [1, 0, 0, 0]
        stored = [0, 0, 0, 0]
        curent_time = 0
        state = (curent_time, production, stored)
        self.final_state = self.node_hop(state)




with open("input.txt") as file:
    total = 0
    for line in file:
        a = Geodecracker(line, 24)
        total += a.bp_id*a.current_max
        print("Blueprint", a.bp_id, "totaling in", a.current_max, "Geodes")
    print("Answer 1:", total)

with open("input.txt") as file:
    total = 1
    for line in file:
        if "Blueprint 4" in line:
            print("Answer 2:", total)
            break
        a = Geodecracker(line, 32)
        total *= a.current_max
        print("Blueprint", a.bp_id, "totaling in", a.current_max, "Geodes")

#1190 is low