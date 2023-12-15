import math
from copy import deepcopy
class d14():
    def __init__(self, hash_map):
        self.hashes = hash_map
        self.ans_1 = 0
        self.ans_2 = 0

    def run(self):
        for hash in self.hashes:
            cur_val = 0
            for char in hash:
                cur_val += ord(char)
                cur_val *= 17
                cur_val = cur_val%256
            self.ans_1 += cur_val

    def get_box(self, chars):
        cur_val = 0
        for char in chars:
            cur_val += ord(char)
            cur_val *= 17
            cur_val = cur_val % 256
        return cur_val

    def get_ans(self):
        for box_id, contents in self.boxes.items():
            for i, slot in enumerate(contents):
                self.ans_2 += (box_id+1)*(i+1)*int(contents[slot])

    def run2(self):
        self.boxes = {}
        self.boxes[0] = {}
        for hash in self.hashes:
            if "=" in hash:
               lens_id, focal_length = hash.split("=")
               operator = 1
            elif "-" in hash:
                lens_id = hash.replace("-", "")
                operator = 0
            cur_box = self.get_box(lens_id)
            if cur_box not in self.boxes.keys():
                self.boxes[cur_box] = {}
            if operator:
                # in = space
                self.boxes[cur_box][lens_id] = focal_length
            else:
                if lens_id in self.boxes[cur_box].keys():
                    del self.boxes[cur_box][lens_id]
        self.get_ans()

with open("input.txt", "r") as file:
    for j, line in enumerate(file):
        line = line.replace("\n", "")
        hashes = line.split(",")
obj = d14(hashes)
obj.run()
obj.run2()

print("Ansewr 1:", obj.ans_1)
print("Ansewr 1:", obj.ans_2)
