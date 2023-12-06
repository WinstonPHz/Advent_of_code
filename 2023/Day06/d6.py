puz_in = {}
with open("input.txt", "r") as file:
    for line in file:
        line = line.replace("\n", "")
        key, values = line.split(":")
        temp = []
        for val in values.split(" "):
            if val == "":
                continue
            temp.append(int(val))
        puz_in[key] = temp

class part1():
    def __init__(self, input):
        self.input = input
        self.part1_ans = 1
        self.part2_locations = []
        self.part2_ans = []

    def race(self, hold_count, total_time):
        remainder = total_time - hold_count
        return remainder*hold_count

    def run(self):
        for i, time in enumerate(self.input["Time"]):
            win_count = 0
            for mil_hold in range(1,time):
                if self.race(mil_hold, time) > self.input["Distance"][i]:
                    win_count += 1
            self.part1_ans *= win_count
        win_count = 0
        for mil_hold in range(1, 60808676):
            if self.race(mil_hold, 60808676) > 601116315591300:
                win_count += 1
        self.part2_ans = win_count



a = part1(puz_in)
a.run()

print("Answer 1 :", a.part1_ans)
print("Answer 2 :", a.part2_ans)
