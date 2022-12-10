import math
# Structure:
# { FUEL : {components:[[A, 7][E, 1]], quant : 1}}
class factory():
    def __init__(self, chem_list):
        self.left_over = {}
        self.made = {}
        self.chemicals = chem_list
        self.ore_needed = 0
        self.test = 0

    def refine(self, chemical, batches_needed):
        A = "components"
        # We want quant of chemical
        for chem, needed in self.chemicals[chemical][A]:
            # need a needed of chem to make chemical
            if "ORE" == chem:
                self.test += batches_needed*needed
                return
            else:
                if chem in self.left_over.keys():
                    lo = self.left_over[chem]
                    if lo >= batches_needed*needed:
                        self.left_over[chem] -= batches_needed*needed
                        lo = batches_needed*needed
                    else:
                        self.left_over[chem] = 0
                else:
                    self.left_over[chem] = 0
                    lo = 0
                to_make = batches_needed*needed - lo
                #print(f"Making {to_make} of {chem}, requested {batches_needed} {chemical}")
                made_per_batch = self.chemicals[chem]["make"]
                batches = math.ceil(to_make/made_per_batch)
                self.left_over[chem] += made_per_batch*batches-to_make
                if chem not in self.made.keys():
                    self.made[chem] = 0
                self.made[chem] += needed*batches_needed
                self.refine(chem,  batches)

    def calc_ore(self):
        for chem in self.made:
            if "ORE" in self.chemicals[chem]["components"][0][0]:
                needed = self.made[chem] + self.left_over[chem]
                batches = needed/self.chemicals[chem]["make"]
                if needed%batches != 0:
                    print(f"Somthing went wrong, the number of batches does not add up for {chem}")
                self.ore_needed += batches*self.chemicals[chem]["components"][0][1]




## SEtup
chemicals = {}
batches = {}
with open("d14in.txt", "r") as file:
    for line in file:
        line = line.strip("\n")
        comps = line.split(" => ")
        if "," not in line:
            right_num = int(comps[1].split(" ")[0])
            right_chem = comps[1].split(" ")[1]
            left_num = int(comps[0].split(" ")[0])
            left_chem = comps[0].split(" ")[1]
            left_chem = [[left_chem, left_num]]
            chemicals[right_chem] = {"components":left_chem, "make":right_num}
        else:
            chem_list = comps[0].split(", ")
            left_side = []
            for chemical in chem_list:
                chemical = chemical.split(" ")
                left_num = int(chemical[0])
                left_chem = chemical[1]
                left_side.append([left_chem, left_num])
            right_num = int(comps[1].split(" ")[0])
            right_chem = comps[1].split(" ")[1]
            left_chem = [left_chem, left_num]
            chemicals[right_chem] = {"components": left_side, "make": right_num}


ore_in_pos = 1000000000000
f1 = factory(chemicals)
f1.refine("FUEL", 1)
f1.calc_ore()
print("Ans 1: ", end="")
print(f1.test)

min = int(ore_in_pos/f1.test)
max = min*2
min_orig = min
max_orig = max
while True:
    fmin = factory(chemicals)
    fmin.refine("FUEL", min)
    fmax = factory(chemicals)
    fmax.refine("FUEL", max)
    if fmin.test > ore_in_pos:
        max = min
        min = min_orig
        continue
    if max-min < 10:
        for i in range(min,max):
            fmax = factory(chemicals)
            fmax.refine("FUEL", i)
            if fmax.test >= ore_in_pos:
                print("Ans 2:", i-1)
                break
        break
    mid = int((max-min)/2) + min
    min = mid
