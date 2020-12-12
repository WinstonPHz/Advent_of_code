file1 = open("input.txt", "r")
input = ""
for line in file1:
    input += line
Groups = input.split("\n\n")
Counts = []
Counts2 = []
for group in Groups:
    persons = group.split("\n")
    yes = []
    all = persons[0]
    alls = ""
    for person in persons:
        for answer in person:
            if not (answer in yes):
                yes.append(answer)
            if answer in all:
                alls += answer
        all = alls
        alls = ""
    Counts.append(len(yes))
    Counts2.append(len(all))
print(sum(Counts))
print(sum(Counts2))
