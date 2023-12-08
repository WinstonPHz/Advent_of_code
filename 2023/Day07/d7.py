
class part1():
    def __init__(self):
        self.input = input
        self.part1_ans = 0
        self.part2_ans = 0
        self.order =        "A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2".split(", ")
        self.order_2 =      "A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J".split(", ")
        self.replace_with = "A, B, C, D, E, F, G, H, I, K, L, M, N".split(", ")
        self.hand_order = ["5ook", "4ook", "full_house", "3ook", "2pair", "2ook", "high"]
        self.hands = {}
        self.hands2 = {}
        self.bins = {}
        self.bins2 = {}

        self.bins["5ook"] = []
        self.bins["4ook"] = []
        self.bins["full_house"] = []
        self.bins["3ook"] = []
        self.bins["2pair"] = []
        self.bins["2ook"] = []
        self.bins["high"] = []

        self.bins2["5ook"] = []
        self.bins2["4ook"] = []
        self.bins2["full_house"] = []
        self.bins2["3ook"] = []
        self.bins2["2pair"] = []
        self.bins2["2ook"] = []
        self.bins2["high"] = []


    def add_hand_1(self, line):
        hand, value = line.split(" ")
        for i, rp in enumerate(self.replace_with):
            hand = hand.replace(self.order[i], rp)
        self.hands[hand] = value
        hand_lib = {}
        for card in hand:
            if card not in hand_lib.keys():
                hand_lib[card] = 1
            else:
                hand_lib[card] += 1
        cc_array = []
        for key, value in hand_lib.items():
            cc_array.append(value)
        cc_array.sort()
        if 5 in cc_array:
            self.bins["5ook"].append(hand)
        elif 4 in cc_array:
            self.bins["4ook"].append(hand)
        elif 3 in cc_array and 2 in cc_array:
            self.bins["full_house"].append(hand)
        elif [1,2,2] == cc_array:
            self.bins["2pair"].append(hand)
        elif 3 in cc_array:
            self.bins["3ook"].append(hand)
        elif 2 in cc_array:
            self.bins["2ook"].append(hand)
        else:
            self.bins["high"].append(hand)

    def count_total_p1(self):
        rank = 1
        for hand_value in self.hand_order[::-1]:
            temp = self.bins[hand_value]
            temp.sort()
            for hand in temp[::-1]:
                self.part1_ans += rank*int(self.hands[hand])
                rank += 1

    def add_hand_2(self, line):
        hand, value = line.split(" ")
        for i, rp in enumerate(self.replace_with):
            hand = hand.replace(self.order_2[i], rp)
        self.hands2[hand] = value
        hand_lib = {}
        jokes = 0
        for card in hand:
            if card not in hand_lib.keys():
                hand_lib[card] = 1
            else:
                hand_lib[card] += 1
        if "N" in hand_lib.keys():
            jokes = hand_lib["N"]
            hand_lib["N"] = 0

        cc_array = []
        for key, value in hand_lib.items():
            cc_array.append(value)
        cc_array.sort()
        if jokes == 0:
            if 5 in cc_array:
                self.bins2["5ook"].append(hand)
            elif 4 in cc_array:
                self.bins2["4ook"].append(hand)
            elif 3 in cc_array and 2 in cc_array:
                self.bins2["full_house"].append(hand)
            elif [1, 2, 2] == cc_array:
                self.bins2["2pair"].append(hand)
            elif 3 in cc_array:
                self.bins2["3ook"].append(hand)
            elif 2 in cc_array:
                self.bins2["2ook"].append(hand)
            else:
                self.bins2["high"].append(hand)
        elif jokes == 1:
            if 4 in cc_array:
                self.bins2["5ook"].append(hand)
            elif 3 in cc_array:
                self.bins2["4ook"].append(hand)
            elif [0, 2, 2] == cc_array:
                self.bins2["full_house"].append(hand)
            elif [0, 1, 1, 2] == cc_array:
                self.bins2["3ook"].append(hand)
            else:
                self.bins2["2ook"].append(hand)
        elif jokes == 2:
            if 3 in cc_array:
                self.bins2["5ook"].append(hand)
            elif 2 in cc_array:
                self.bins2["4ook"].append(hand)
            else:
                self.bins2["3ook"].append(hand)
        elif jokes == 3:
            if 2 in cc_array:
                self.bins2["5ook"].append(hand)
            else:
                self.bins2["4ook"].append(hand)
        else:
            self.bins2["5ook"].append(hand)

    def count_total_p2(self):
        rank = 1
        for hand_value in self.hand_order[::-1]:
            temp = self.bins2[hand_value]
            temp.sort()
            for hand in temp[::-1]:
                self.part2_ans += rank*int(self.hands2[hand])
                rank += 1



puz_in = {}
a = part1()
with open("input.txt", "r") as file:
    for line in file:
        line = line.replace("\n", "")
        a.add_hand_1(line)
        a.add_hand_2(line)
a.count_total_p1()
a.count_total_p2()
print("Answer 1 :", a.part1_ans)
print("Answer 2 :", a.part2_ans)
