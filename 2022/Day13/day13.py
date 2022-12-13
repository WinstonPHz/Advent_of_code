import json
import copy

class PacketPair():
    def __init__(self):
        self.correct_order = True
        self.set = False
        self.got_first = False
        self.packet1 = []
        self.packet2 = []
        self.list = type([])
        self.int = type(0)

    def reset(self):
        self.correct_order = True
        self.set = False
        self.got_first = False
        self.packet1 = []
        self.packet2 = []

    def add_packet(self, to_add):
        if not self.got_first:
            self.packet1 = json.loads(to_add)
            self.got_first = True
        else:
            self.packet2 = json.loads(to_add)

    def compair_lists(self, l, r):
        l = copy.copy(l)
        r = copy.copy(r)
        if self.set:
            return self.correct_order
        while True:
            if l == r:
                return True
            if l == []:
                self.correct_order = True
                self.set = True
                return True
            to_compair_left = l.pop(0)
            if r == []:
                self.correct_order = False
                self.set = True
                return self.correct_order
            to_compair_right = r.pop(0)

            if not type(to_compair_left) == type(to_compair_right):
                # They are not the same type, one is a list, the other int, lets fix that
                to_compair_left, to_compair_right = self.convert_int(to_compair_left, to_compair_right)

            if type(to_compair_left) == self.list:
                # Is the left a list, if so they both are so lets compair these lists:
                self.correct_order = self.compair_lists(to_compair_left, to_compair_right)
                if self.set:
                    return self.correct_order
            else:
                # They are both integers, sweet
                if to_compair_left < to_compair_right:
                    self.correct_order = True
                    self.set = True
                    return self.correct_order
                elif to_compair_left > to_compair_right:
                    # Left is bigger than right, bits are false
                    self.correct_order = False
                    self.set = True
                    return self.correct_order

    def convert_int(self, l, r):
        if type(l) == self.int:
            l = [l]
        if type(r) == self.int:
            r = [r]
        return l, r

    def compair_packets(self):
        self.compair_lists(self.packet1, self.packet2)
        #print(self.packet1, "Compaired to", self.packet2, "returns", self.correct_order)
        return self.correct_order



packet_pairs = []
packet_list = ["[[2]]", "[[6]]"]
with open("/nfshome/gold/mbourgeo/scripts/Advent_of_code/2022/Day13/input.txt", "r") as file:
    for line in file:
        if line == "\n":
            packet_pairs.append(PacketPair())
            continue
        packet_pairs[-1].add_packet(line)
        packet_list.append(line.strip("\n"))


ans1 = 0
pair = PacketPair()



for i, pp in enumerate(packet_pairs):
    if pp.compair_packets():
        ans1 += 1+i
print("Answer 1:", ans1)

while True:
    for i in range(len(packet_list)-1):
        pb = packet_list.pop(i+1)
        pa = packet_list.pop(i)
        to_comp = PacketPair()
        to_comp.add_packet(pa)
        to_comp.add_packet(pb)
        correct_order = to_comp.compair_packets()
        if not correct_order:
            packet_list = packet_list[:i] + [pb] + [pa] + packet_list[i:]
            break
        else:
            packet_list = packet_list[:i] + [pa] + [pb] + packet_list[i:]

    if correct_order:
        break

a=0
b=0
for i, packet in enumerate(packet_list):
    if packet == "[[2]]":
        a = i+1
    if packet == "[[6]]":
        b = i+1
print("Answer 2:", a*b)
#4014 is too low
#6011 is to high