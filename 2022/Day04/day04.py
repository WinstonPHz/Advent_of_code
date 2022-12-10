
def is_contained(g1,g2):
    if g1[0] <= g2[0] and g2[1] <= g1[1]:
        return True
    if g2[0] <= g1[0] and g1[1] <= g2[1]:
        return True
    return False

def is_overlap(g1,g2):
    if g1[0] <= g2[0] <= g1[1]:
        return True
    if g2[0] <= g1[0] <= g2[1]:
        return True
    return False

pairs = []
with open("input.txt", "r") as file:
    for line in file:
        line = line.strip("\n")
        comp = line.split(",")
        x0, x1 = comp[0].split("-")
        y0, y1 = comp[1].split("-")
        pairs.append([[int(x0), int(x1)],[int(y0), int(y1)]])

containeds = []
overlaps = []
for pair in pairs:
    if is_contained(pair[0], pair[1]):
        containeds.append(pair)
    if is_overlap(pair[0], pair[1]):
        overlaps.append(pair)

print(len(containeds))
print(len(overlaps))
