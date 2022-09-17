def get_input():
    puz = []
    for line in open("puz", "r+"):
        line = line.strip("\n")
        puz.append(line.split("-"))
    connections = {}
    for a, b, in puz:
        if a not in connections.keys():
            connections[a] = []
        if b not in connections.keys():
            connections[b] = []
        if b not in connections[a]:
            connections[a].append(b)
        if a not in connections[b]:
            connections[b].append(a)
    return connections

overall_path = []

def rec_find_all(conections, entered, beens = ["start"], cur_path = ""):
    cur_path += entered + ","
    if entered == "end":
        overall_path.append(cur_path[:-1])
        return ""
    if entered == entered.lower() and entered not in beens:
        beens.append(entered)
    for next_room in conections[entered]:
        if next_room not in beens:
            rec_find_all(conections, next_room, beens.copy(), cur_path)
    return ""


overall_path2 = []
def rec_find_all2(conections, entered, beens = [], cur_path = "", flag = False):
    cur_path += entered + ","
    if entered == "end":
        if cur_path[:-1] not in overall_path2:
            overall_path2.append(cur_path[:-1])
        return ""
    conections[entered].sort()
    if entered == entered.lower():
        if entered not in beens:
            beens.append(entered)
    for next_room in conections[entered]:
        if next_room == "start":
            continue
        if next_room == next_room.lower():
            if next_room in beens and flag == False and entered != "start":
                flag = True
                rec_find_all2(conections, next_room, beens.copy(), cur_path, flag)
                flag = False
        if next_room not in beens:
            rec_find_all2(conections, next_room, beens.copy(), cur_path, flag)
    return ""

caves = get_input()
#all_paths = rec_find_all(caves, "start")
print(len(overall_path))
print(caves)
all_paths2 = rec_find_all2(caves, "start")
print("Answer 2:", len(overall_path2))
