from copy import deepcopy

# Code Stolen, it works but not sure why.
file1 = open("input.txt", "r")
inputs = ""
for line in file1:
    inputs += line

def rule_match(mess, rule_check):
    if mess == '' or rule_check == []:
        return mess == '' and rule_check == []  # if both are empty, True. If only one, False.

    to_check = rules[rule_check[0]]
    if '"' in to_check:
        if mess[0] in to_check:
            return rule_match(mess[1:], rule_check[1:])  # strip first character
        else:
            return False  # wrong first character
    else:
        check = []
        for t in to_check:
            check.append(rule_match(mess, t + rule_check[1:]))
        return any(check)

comp = inputs.split("\n\n")
rules = {}
messages = comp[1].split("\n")

for rule in comp[0].split("\n"):
    key, contain = rule.split(": ")
    if '"' not in contain:
        contain = [[int(r) for r in t.split()] for t in contain.split("|")]
    rules[int(key)] = contain

print("Part 1:", sum(rule_match(message, [0]) for message in messages))
