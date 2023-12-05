cards = {}
with open("input.txt", "r") as file:
    for line in file:
        line = line.strip('\n')
        line = line.replace("  ", " ").replace("  ", " ").replace("Card ", "").replace(":", " |")
        id, winners, ours = line.split(" | ")
        winners = winners.split(" ")
        ours = ours.split(" ")
        cards[id] = {}
        cards[id]["wins"] = winners
        cards[id]["ours"] = ours

class part1():
    def __init__(self, input):
        self.input = input
        self.current_id = 1
        self.part1_ans = 0
        self.part2_ans = 0
        self.winnings = {}
        self.card_counter = {}

    def search(self, winners, ours, id):
        counter = 0
        points = 0
        for win in winners:
            if win in ours:
                counter += 1
        if counter == 1:
            points = 1
        elif counter > 1:
            points = 1
            for i in range(counter-1):
                points *= 2
        self.winnings[id] = counter
        self.part1_ans += points

    def run(self):
        for id, sets in self.input.items():
            self.search(sets["wins"], sets["ours"], id)

    def run2(self):
        self.card_counter[1] = 0
        print(self.winnings)
        for id in range(1, len(self.winnings.keys()) + 1):
            self.card_counter[id] = 1
        for id in range(1, len(self.winnings.keys())+1):
            win_count = self.winnings[str(id)]
            for i in range(id, id + win_count):
                if i+1 not in self.card_counter.keys():
                    self.card_counter[i+1] = 1 * self.card_counter[id]
                else:
                    self.card_counter[i+1] += 1 * self.card_counter[id]
        for id, count in self.card_counter.items():
            self.part2_ans += count






a = part1(cards)
a.run()
a.run2()
print("Answer 1 :", a.part1_ans)
print("Answer 2 :", a.part2_ans)