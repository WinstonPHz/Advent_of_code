from copy import deepcopy

class d19():
    def __init__(self):
        self.rules = {}
        self.ans_2 = 0
        self.inv_ans_2 = 0

    def addRule(self, line):
        line = line.replace("{", " ").replace("}", "")
        rule_id, rules = line.split()
        containers = rules.split(",")
        temp = {}
        for container in containers:
            if ":" in container:
                key, value = container.split(":")
            else:
                key = value = container
            temp[key] = value
        self.rules[rule_id] = temp

    def get_permutations(self, values):
        perms = 1
        for key, number in values.items():
            number = (number[1] - number[0]) + 1
            perms *= number
        return perms

    def go_deeper(self, values, evaluate):
        print(values, evaluate)
        values = deepcopy(values)
        if evaluate == "A":
            self.ans_2 += self.get_permutations(values)
            return
        elif evaluate == "R":
            self.inv_ans_2 += self.get_permutations(values)
            return
        eval_rules = self.rules[evaluate]
        for rule, destination in eval_rules.items():
            if ">" in rule:
                char, number = rule.split(">")
                number = int(number)
                deep_values = deepcopy(values)
                deep_values[char][0] = number + 1
                self.go_deeper(deep_values, destination)
                values[char][1] = number
            elif "<" in rule:
                char, number = rule.split("<")
                number = int(number)
                deep_values = deepcopy(values)
                deep_values[char][1] = number - 1
                self.go_deeper(deep_values, destination)
                values[char][0] = number
            else:
                self.go_deeper(deepcopy(values), destination)

    def solve_pt2(self):
        values = {}
        for char in "x,m,a,s".split(","):
            values[char] = [1,4000]
        self.go_deeper(values, "in")

puz_in = {}
obj = d19()
instructions = False
with open("input.txt", "r") as file:
    for j, line in enumerate(file):
        line = line.replace("\n", "")
        if line == "":
            instructions = True
            continue
        if not instructions:
            obj.addRule(line)
obj.solve_pt2()
print("Answer 2:", obj.ans_2)

# LOW 129468689690629
#15196