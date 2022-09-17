from copy import deepcopy
file1 = open("input.txt", "r")
inputs = ""
for line in file1:
    inputs += line
puzzle = inputs.split("\n\n")
##### Part 1
fields = {}
col_fields = {}
absolutes = {}
catagories = puzzle[0].split("\n")
# Split the puzzle into keys and dicts that I will use later
for i, cat in enumerate(catagories):
    key = cat.split(":")[0]
    ranges = cat.split(": ")[1].split(" or ")
    lows = []
    for range in ranges:
        lows.append(range.split("-"))
    fields[key] = lows
    col_fields[key] = []
    absolutes[key] = []


my_ticket = puzzle[1].split("\n")[1].split(",")
for key in fields:
    for item in my_ticket:
        col_fields[key].append(0)
other_tickets_l = puzzle[2].split("\n")
other_tickets = []

for i, ticket in enumerate(other_tickets_l):
    if i == 0:
        continue
    else:
        other_tickets.append(ticket.split(","))
error = []
bad = []
good_tickets = deepcopy(other_tickets)
for i, ticket in enumerate(other_tickets):
    for k, value in enumerate(ticket):
        v_good = False
        for key in fields:
            for j, ran in enumerate(fields[key]):
                if int(ran[0])<=int(value)<=int(ran[1]):
                    v_good = True
                    break
        if v_good == False:
            error.append(int(value))
            bad.append(i)
print("Answer 1:", sum(error))
for id in reversed(bad):
    good_tickets.pop(id)
# makes a dict that counts each tickets valids in a given row.
for i, ticket in enumerate(good_tickets):
    for j, value in enumerate(ticket):
        for key in fields:
            for k, ran in enumerate(fields[key]):
                if int(ran[0]) <= int(value) <= int(ran[1]):
                    col_fields[key][j] += 1

taken = []
# Looks for the remaining one for which the values are in the range for all tickets
for leng in col_fields:
    for key in col_fields:
        # if there is a key that is taken, maxes will be set to 0 removing them from the known goods
        for id in taken:
            col_fields[key][id] = 0
        max_count = 0

        for i, max in enumerate(col_fields[key]):
            if max == len(good_tickets):
                max_count += 1
                row = i
        if max_count == 1:
            taken.append(row)
            absolutes[key] = row


wants = ["departure location",
         "departure station",
         "departure platform",
         "departure track",
         "departure date",
         "departure time"]
tots = 1

for want in wants:
    tots *= int(my_ticket[absolutes[want]])
print("Answer 2:", tots)
