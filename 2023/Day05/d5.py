puz_in = {}
with open("input.txt", "r") as file:
    current = ""
    for line in file:
        line = line.replace("\n", "")
        if "seeds" in line:
            puz_in["seeds"] = line.split(": ")[-1].split(" ")
            puz_in["path"] = []
            continue
        if line == "":
            continue
        if "map" in line:
            current = line.split(" ")[0]
            puz_in["path"].append(current)
            puz_in[current] = []
            continue
        line = line.split(" ")
        to_do = []
        for a in line:
            to_do.append(int(a))
        puz_in[current].append(to_do)

class part1():
    def __init__(self, input):
        self.input = input
        self.part1_ans = []
        self.part2_locations = []
        self.part2_ans = []

# destination start, Source Range Start, Source Range Length
    def find_destination(self, start, dest):
        # Does a single step, a-to-b
        for dest_start, range_start, range_length in self.input[dest]:
            if range_start <= start <= range_start + range_length:
                return dest_start+start-range_start
        return start

    def find_seed_location(self, a):
        # does all the steps a-b-c-...-n
        local = a
        for locations in self.input["path"]:
            local = self.find_destination(local, locations)
            if locations == "humidity-to-location":
                self.part1_ans.append(local)
                return local

    def run(self):
        for seed in self.input["seeds"]:
            seed = int(seed)
            self.find_seed_location(seed)

    def find_any_location(self, number, start):
        # starts at n and does steps until end, n-...-x-y-z
        local = number
        start_index = self.input["path"].index(start)
        for locations in self.input["path"][start_index:]:
            local = self.find_destination(local, locations)
            if locations == "humidity-to-location":
                self.part2_locations.append(local)
                return local

    def find_previous_location(self, start, location):
        # Does a single back step b-a
        for dest_start, range_start, range_length in self.input[location]:
            if dest_start <= start <= dest_start + range_length:
                return start + range_start - dest_start
        return start

    def location_to_seed(self, location_id):
        # Does from z to a z-y-x-...c-b-a
        local = location_id
        for locations in self.input["path"][::-1]:
            local = self.find_previous_location(local, locations)
            if locations == "seed-to-soil":
                return local

    def run2(self):
        # Finds the answer for part 2
        numbers_to_check = {}
        # Get a list of all the source range_starts, its going to be at one of these
        for location in self.input["path"]:
            numbers_to_check[location] = []
            for _, number, _ in self.input[location]:
                numbers_to_check[location].append(number)
        # Find the end location for every source_range_start
        for local, numbers in numbers_to_check.items():
            for number in numbers:
                self.find_any_location(number, local)
        # Find the corresponding seed id
        seeds = {}
        for location in self.part2_locations:
            seed_id = self.location_to_seed(location)
            seeds[seed_id] = location
        # Figure out the ranges for the seeds
        seed_ranges = []
        while True:
            a = self.input["seeds"].pop(0)
            b = self.input["seeds"].pop(0)
            seed_ranges.append([int(a), int(a)+int(b)])
            if not self.input["seeds"]:
                break
        # Figure out if each seed_id is in a seed range, if it is, adds its end location to the final list
        for seed in seeds.keys():
            for a, b in seed_ranges:
                if a <= seed <= b:
                    self.part2_ans.append(seeds[seed])

a = part1(puz_in)
a.run()
a.run2()
print("Answer 1 :", min(a.part1_ans))
print("Answer 2 :", min(a.part2_ans))
