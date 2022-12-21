import json
class monkey_Math():
    def __init__(self):
        self.monkeys = {}
        with open("input.txt", "r") as file:
            for line in file:
                line = line.strip("\n")
                key, command = line.split(": ")
                try:
                    command = int(command)
                except:
                    command = command
                self.monkeys[key] = command
        self.current_guess = 2022
        self.root_right_side = 0
        self.inverse = {
            "*":"/",
            "/":"*",
            "+":"-",
            "-":"+"
        }
        self.my_side = ""

    def recursion(self, monkey):
        to_do = self.monkeys[monkey]
        if type(to_do) == type(0):
            return to_do
        monk_a, operator, monk_b = to_do.split(" ")
        a = self.recursion(monk_a)
        b = self.recursion(monk_b)
        return int(eval(f"{a} {operator} {b}"))

    def recursion2(self, monkey):
        to_do = self.monkeys[monkey]
        if monkey == "root":
            monk_a, monk_b = to_do.split(" + ")
            b = self.recursion(monk_b)
            self.root_right_side = int(b)
            a = self.human_side(monk_a)
            self.my_side = json.loads(a)
            return self.human_side(monk_a) == self.recursion(monk_b)


    def human_side(self, monkey):
        to_do = self.monkeys[monkey]
        if monkey == "humn":
            return '"x"'
        if type(to_do) == type(0):
            return to_do
        monk_a, operator, monk_b = to_do.split(" ")
        a = self.human_side(monk_a)
        b = self.human_side(monk_b)
        if type(a) == type(0) and type(b) == type(0):
            return int(eval(f"{a} {operator} {b}"))
        return f'[{a}, "{operator}", {b}]'

    def solve_x(self, array):
        if array == "x":
            return
        left_side = array[0]
        operator = array[1]
        right_side = array[2]
        if type(left_side) == type(0):
            if operator == "/" or operator == "-":
                self.root_right_side = eval(f"{left_side} {operator} {self.root_right_side}")
            else:
                self.root_right_side = eval(f"{self.root_right_side} {self.inverse[operator]} {left_side}")
            self.solve_x(right_side)
        if type(right_side) == type(0):
            self.root_right_side = eval(f"{self.root_right_side} {self.inverse[operator]} {right_side}")
            self.solve_x(left_side)


    def find_my_number(self):
        self.recursion2("root")
        self.solve_x(self.my_side)
        print("Answer 2:", int(self.root_right_side))





mm = monkey_Math()
answer_1 = mm.recursion("root")
print("Answer 1:", int(answer_1))
answer_2 = mm.find_my_number()
