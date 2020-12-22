from copy import deepcopy

#Gets close to the right answer, adds slightly more than needed. 11 that is.
#aaaabbaaaabbaaa <--- this one specifically in the testing.
file1 = open("input.txt", "r")
inputs = ""
for line in file1:
    inputs += line

def rule_match(mess, rule_check):
    if mess == "": # added in part 2
        print(mess, rule_check)
        return mess, True
    new_mess = mess
    for i, rule_group in enumerate(rules[rule_check]):
        check = []
        for j, rule in enumerate(rule_group):
            if rules[rule] == "a" or rules[rule] == "b":
                if rules[rule] == new_mess[0]:
                    new_mess = new_mess[1:]
                    check.append(True)
                else:
                    new_mess = mess
                    break
            else:
                new_mess, checker = rule_match(new_mess, rule)
                if checker == True:
                    check.append(checker)
                    continue
                else:
                    new_mess = mess
                    break
        if len(check) == len(rule_group):
            good = True
            return new_mess, good
        else:
            good = False
    return new_mess, good

comp = inputs.split("\n\n")
rules = {}
messages = comp[1].split("\n")

for rule in comp[0].split("\n"):
    key = rule.split(": ")[0]
    contain = rule.split(": ")[1].split(" | ")
    inside = []
    if contain[0][0] == '"':
        contain = contain[0][1]
    else:
        for i, a in enumerate(contain):
            inside.append(a.split(" "))
        contain = inside
    rules[key] = contain
tots = 0
for message in messages:
    check, good = rule_match(message, "0")
    if len(check) == 0 and good:
        tots += 1
        print(message)
print("Answer 2:", tots)