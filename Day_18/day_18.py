from copy import deepcopy
file1 = open("input.txt", "r")
inputs = ""
for line in file1:
    inputs += line
puzzle = inputs.split("\n")

def nested(problem):
    while True:
        opens = []
        closes = []
        print(problem)
        j = 0
        for i, char in enumerate(problem):
            if char == "(":
                opens.append(i)
            if char == ")":
                closes.append(i)
            if len(closes) == 1:
                new = eval(problem[opens[-1]+1:closes[0]])
                problem = problem[0:opens[-1]]+str(new)+problem[closes[0]+1:]
                closes.pop(0)
                opens.pop(-1)
                break
        if len(opens) == 0:
            try:
                return eval(problem)
            except:
                continue


def eval(expression):
    evaluates = expression.split(" ")
    total = 0
    while "+" in evaluates:
        new_valuates = []
        for i, val in enumerate(evaluates):
            if val == "+":
                sums = int(evaluates[i-1])+int(evaluates[i+1])
                new_valuates.pop(-1)
                new_valuates.append(sums)
                new_valuates += evaluates[i+2:]
                break
            else:
                new_valuates.append(val)
        evaluates = deepcopy(new_valuates)

    for i, val in enumerate(evaluates):
        if i == 0:
            total = int(val)
        if val == "*":
           total *= int(evaluates[i+1])
    return total


tots = []
for puz in puzzle:
    tots.append(nested(puz))
print("Answer 1:", sum(tots))


