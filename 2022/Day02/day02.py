
score = 0

with open("input.txt", "r") as file:
    for line in file:
        line = line.strip("\n")
        him, me = line.split(" ")
        if me == "X": # Me Rock
            score += 1
            if him == "A":
                score += 3
            elif him == "C":
                score += 6
        elif me == "Y": # Me paper
            score += 2
            if him == "B":
                score += 3
            elif him == "A":
                score += 6
        elif me == "Z": # Me Scisors
            score += 3
            if him == "B":
                score += 6
            elif him == "C":
                score += 3


print(score)
score = 0

# x= lose
# y= tie
# z= win
# A: rock = tie,  paper=win   scisors = loss,
# B: rock = lose, paper=tie,  scisors = win
# C: rock = win,  paper=lose, scisors = tie
   #Loss Tie Win
A = [3,4,8]
B = [1,5,9]
C = [2,6,7]
with open("input.txt", "r") as file:
    for line in file:
        line = line.strip("\n")
        him, me = line.split(" ")
        if him == "A":
            if me == "X":
                score += A[0]
            elif me == "Y":
                score += A[1]
            elif me == "Z":
                score += A[2]
        elif him == "B":
            if me == "X":
                score += B[0]
            elif me == "Y":
                score += B[1]
            elif me == "Z":
                score += B[2]
        elif him == "C":
            if me == "X":
                score += C[0]
            elif me == "Y":
                score += C[1]
            elif me == "Z":
                score += C[2]

print(score)