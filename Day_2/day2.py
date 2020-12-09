file1 = open("input.txt", "r")
passwords = []
tots1 = 0
tots2 = 0
lines = 0
for line in file1:
    passwords.append(line.split("\n")[0])
for password in passwords:
    lines += 1
    comp = password.split(" ")
    range = comp[0].split("-")
    min = int(range[0])
    max = int(range[1])
    key = comp[1][0]
    pword = comp[2]
    sum = 0
    for letter in pword:
        if letter == key:
            sum += 1
    if (min <= sum) and (sum <= max):
        tots1 += 1

    if pword[min-1] == key or pword[max-1] == key:
        if pword[min-1] != pword[max-1]:
            tots2 += 1

print("Total 1:", tots1)
print("Total 2:", tots2)