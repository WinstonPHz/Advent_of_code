from copy import deepcopy
file1 = open("input.txt", "r")
inputs = ""
for line in file1:
    inputs += line

def build_deck(deck):
    hand = []
    for card in deck.split("\n"):
        if "P" not in card:
            hand.append(int(card))
    return hand

def play_game1(d1, d2):
    while True:
        if d1 == [] or d2 == []:
            if p1_hand == []:
                return d2
            else:
                return d1
        else:
            p1c = d1[0]
            p2c = d2[0]
            d1.pop(0)
            d2.pop(0)
            if p1c>p2c:
                d1.append(p1c)
                d1.append(p2c)
            elif p2c > p1c:
                d2.append(p2c)
                d2.append(p1c)

def play_game2(d1, d2):
    Played = []
    round = 0
    while True:
        if [d1, d2] in Played:
            return True, d1
        Played.append(deepcopy([d1, d2]))
        round += 1
        if d1 == [] or d2 == []:
            if d1 == []:
                return False, d2
            else:
                return True, d1
        else:
            p1c = d1[0]
            p2c = d2[0]
            d1.pop(0)
            d2.pop(0)

            # Actual Game Play
            if p1c <= len(d1) and p2c <= len(d2):
                Win, dump = play_game2(d1[:p1c], d2[:p2c])
            elif p1c>p2c:
                Win, dump = True, d1
            else:
                Win, dump = False, d2

            if Win:
                d1.append(p1c)
                d1.append(p2c)
            else:
                d2.append(p2c)
                d2.append(p1c)

def score1(w_hand):
    total = 0
    for i, card in enumerate(reversed(w_hand)):
        total += (i+1)*card
    print(f"Answer 1:", total)

def score2(win, w_hand):
    print("Player Won?", win)
    total = 0
    for i, card in enumerate(reversed(w_hand)):
        total += (i+1)*card
    print(f"Answer 2:", total)
p1, p2 = inputs.split("\n\n")
p1_hand = build_deck(p1)
p2_hand = build_deck(p2)

score1(play_game1(p1_hand.copy(),p2_hand.copy()))
winner, deck = play_game2(p1_hand,p2_hand)
score2(winner, deck)

