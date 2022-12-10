
import math
# Structure:
# { FUEL : {components:[[A, 7][E, 1]], quant : 1}}

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
            chemicals[right_chem] = {"components":left_chem, "quant":right_num}
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
            chemicals[right_chem] = {"components": left_side, "quant": right_num}

def find_root_chem(lookingFor, quant_needed = 1.0):
    A = "components"
    made_per_batch = chemicals[lookingFor]["quant"]
    batches_needed = quant_needed/made_per_batch
    if "ORE" == lookingFor:
        if "ORE" not in batches.keys():
            batches["ORE"] = 0
        batches["ORE"] += batches_needed
        return
    else:
        for chem, total in chemicals[lookingFor][A]:
            if chem not in batches.keys():
                batches[chem] =
            else:
                batches[chem] += 


print(chemicals)
