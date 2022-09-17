file1 = open("input.txt", "r")
years = []
for line in file1:
    years.append(int(line))
for year1 in years:
    for year2 in years:
        for year3 in years:
            if year1+year2+year3 == 2020:
                print("part2: ", year1*year2*year3)
        if (year1 + year2) == 2020:
            print("part1: ", year1*year2)
        else:
            continue
