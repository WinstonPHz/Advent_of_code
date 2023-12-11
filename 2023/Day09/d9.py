import math
class part1():
    def __init__(self, ans_1):
        self.sequence = {}
        self.sequence[0] = ans_1
        self.to_return = 0

    def run(self):
        seq_id = 0
        while True:
            if self.sequence[seq_id] == [0]*len(self.sequence[seq_id]):
                break
            self.sequence[seq_id+1] = self.find_nodes(self.sequence[seq_id])
            seq_id += 1
        self.find_future()
        return self.sequence[0][-1]

    def find_nodes(self, seq_in):
        seq_out = []
        for i, char in enumerate(seq_in):
            if i == len(seq_in)-1:
                break
            seq_out.append(seq_in[i+1]-char)
        return seq_out

    def find_future(self):
        inverted_key_order = list(self.sequence.keys())[::-1]
        for key in inverted_key_order:
            if key == inverted_key_order[0]:
                self.sequence[key].append(0)
                continue
            self.sequence[key].append(self.sequence[key][-1] + self.sequence[key+1][-1])

    def find_past(self):
        inverted_key_order = list(self.sequence.keys())[::-1]
        for key in inverted_key_order:
            if key == inverted_key_order[0]:
                self.sequence[key].append(0)
                continue
            past_number = self.sequence[key][0] - self.sequence[key+1][0]
            self.sequence[key].insert(0, past_number)
        return self.sequence[key][0]

ans_1 = []
ans_2 = []
with open("input.txt", "r") as file:
    for line in file:
        array = []
        line = line.replace("\n", "")
        for char in line.split(" "):
            array.append(int(char))
        obj = part1(array)
        ans_1.append(obj.run())
        ans_2.append(obj.find_past())

print("Answer 1 :", sum(ans_1))
print("Answer 2 :", sum(ans_2))
