file1 = open("input.txt", "r")
input =  ""


def inbag(dict, big_dict):
    total = 0
    for key in dict:
        if key == "shiny gold":
            return 1
        try:
           total = inbag(big_dict[key], big_dict)
        except:
            continue
        if total == 1:
            return total
    return total

def sumInbag(dict, big_dict):
    total = 0
    for key in dict:
        if dict[key] == 0:
            total = 0
        else:
            for i in range(int(dict[key])):
                total += sumInbag(big_dict[key], big_dict)
    return total + 1

for line in file1:
    input += line
rules = input.split("\n")
colors = {}

for rule in rules:
    key = rule.split("contain")[0].split(" bag")[0]
    values = rule.split(" contain ")[1].split(", ")
    contents = {}
    for val in values:
        if val.split(" ")[0] == "no":
            contents = {"nul":0}
        else:
            comp = val.split(" ")
            contents[comp[1]+" "+comp[2]] = comp[0]
    value = contents
    colors[key] = value

tots = 0
for key in colors:
    tots += inbag(colors[key], colors)

tots2 = sumInbag(colors["shiny gold"], colors)
print("Answer 1:", tots)
print("Answer 2:", tots2-1)
