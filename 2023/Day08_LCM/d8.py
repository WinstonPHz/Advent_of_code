import math
class part1():
    def __init__(self, puz_in):
        self.input = puz_in
        self.part1_ans = 0
        self.part2_ans = 1

    def part_1(self, start, end):
        step = 0
        current_room = start
        while True:

            command = self.input["steps"][step%len(self.input["steps"])]
            options = self.input[current_room]
            if command == "L":
                current_room = options[0]
            else:
                current_room = options[1]
            step += 1
            if current_room == end:
                return step

    def get_starting_nodes(self):
        self.starting_nodes = []
        for chamber in self.input.keys():
            if chamber[-1] == "A":
                self.starting_nodes.append(chamber)
        print(self.starting_nodes)

    def get_ending_nodes(self):
        self.ending_nodes = []
        for chamber in self.input.keys():
            if chamber[-1] == "Z":
                self.ending_nodes.append(chamber)
        print(self.ending_nodes)

    def run_all(self):
        step = 0
        steps_to_end = [0,0,0,0,0,0]
        found = 0
        current_room = self.starting_nodes
        while True:
            command = self.input["steps"][step%len(self.input["steps"])]
            for i, room in enumerate(current_room):
                options = self.input[room]
                if command == "L":
                    room = options[0]
                else:
                    room = options[1]
                current_room[i] = room
            step += 1
            for i, room in enumerate(current_room):
                if room in self.ending_nodes:
                    if steps_to_end[i] == 0:
                        steps_to_end[i] = step
                        found += 1

            if found == len(self.starting_nodes):
                for count in steps_to_end:
                    self.part2_ans *= count
                self.part2_ans = math.lcm(steps_to_end[0], steps_to_end[1], steps_to_end[2], steps_to_end[3], steps_to_end[4], steps_to_end[5])
                break

    def part_2(self):
        self.get_starting_nodes()
        self.get_ending_nodes()
        self.run_all()


puz_in = {}
puz_in["steps"] = []
with open("input.txt", "r") as file:
    for line in file:
        line = line.replace("\n", "").replace("(", "").replace(")", "")
        if line == "":
            continue
        if "=" not in line:
            for char in line:
                puz_in["steps"].append(char)
            continue
        else:
            chamber, doors = line.split(" = ")
            puz_in[chamber] = doors.split(", ")

a = part1(puz_in)
print("Answer 1 :", a.part_1("AAA", "ZZZ"))

#a.part_1("AAA", "ZZZ")
a.part_2()
print("Answer 2 :", a.part2_ans)
