import json
from functools import cache

from copy import deepcopy
class d19():
    def __init__(self):
        self.rules = {}
        self.ans_1 = 0
        self.max = 4000


    def add_rule(self, rule):
        rule = rule.replace("{", " ").replace("}", "")
        rule = rule.replace("'", '"')
        rule_id, criteria = rule.split(" ")
        to_add = {}
        for crit in criteria.split(","):
            if ":" in crit:
                key, id = crit.split(":")
            else:
                key = crit
                id = crit
            to_add[key] = id
        self.rules[rule_id] = to_add

    def evaluate_line(self, line):
        line = line.replace("{", "").replace("}", "")
        values = {}
        for expression in line.split(","):
            ex_id, val = expression.split("=")
            values[ex_id] = int(val)
        returned_value = self.do_work(deepcopy(values), "in")
        if returned_value == "A":
            for id, val in values.items():
                self.ans_1 += val


    def do_work(self, values, evaluate):
        if len(evaluate) == 1:
            return evaluate
        eval_rules = self.rules[evaluate]
        for rule in eval_rules:
            if ">" in rule:
                expression, number = rule.split(">")
                if values[expression] > int(number):
                    return self.do_work(values, eval_rules[rule])
            elif "<" in rule:
                expression, number = rule.split("<")
                if values[expression] < int(number):
                    return self.do_work(values, eval_rules[rule])
            else:
                return self.do_work(values, eval_rules[rule])

    def do_all_work(self, values, evaluate, range):
        if len(evaluate) == 1:
            return evaluate
        eval_rules = self.rules[evaluate]
        for rule, destination in eval_rules.items():
            if ">" in rule:
                expression, number = rule.split(">")
                if values[expression] > int(number):
                    return self.do_work(values, eval_rules[rule])
            elif "<" in rule:
                expression, number = rule.split("<")
                if values[expression] < int(number):
                    return self.do_work(values, eval_rules[rule])
            else:
                return self.do_work(values, eval_rules[rule])























puz_in = {}
obj = d19()
after_rules = False
with open("input.txt", "r") as file:
    for j, line in enumerate(file):
        line = line.replace("\n", "")
        if line == "":
            after_rules = True
            continue
        if not after_rules:
            obj.add_rule(line)
        else:
            obj.evaluate_line(line)


print(obj.rules)
obj.do_reverse_work()

print("Answer 1:", obj.ans_1)


#15196