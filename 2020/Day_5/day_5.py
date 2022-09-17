file1 = open("input.txt", "r")
input = ""
for line in file1:
    input += line
passes = input.split("\n")
seatID = []
for pas in passes:
    row = ""
    column = ""
    for bit in pas:
        if bit == "B":
            row+="1"
        if bit == "F":
            row+="0"
        if bit == "R":
            column += "1"
        if bit == "L":
            column += "0"
    seatID.append(int(row,2)*8+int(column, 2))
seatID.sort()
for seat in range(len(seatID)):
    if seat == 1:
        continue
    if seatID[seat] != seatID[seat-1]+1:
        print(seatID[seat]-1)
