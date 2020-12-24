from copy import deepcopy
input1 = "389125467"
input2 = "583976241"

def parse(input):
    out = {}
    ranges = []
    for i, char in enumerate(input):
        ranges.append(int(char))
        if i == len(input)-1:
            out[int(char)] = int(input[0])
        else:
            out[int(char)] = int(input[i+1])
    return out, min(ranges), len(ranges)



def printpritty(cup_set):
    pritty = ""
    cur_cup = 1
    for i in range(10):
        pritty += str(cur_cup)
        cur_cup = cup_set[cur_cup]
    return pritty[:-1]

# Think of this like a chain, ever number is linked to the next, we need to cut out 3 links and move them to the desired location, the rest stay linked with one another.
def play_game(cups, min, max, itr):
    # Get first link
    cur_link = 0
    for key in cups:
        cur_link = key
        break
    # Now we can start with the rest of the itterations
    i = 0
    while i < itr:
        relink_point = cur_link - 1
        small_chain = [cups[cur_link]]
        for j in range(2):
            small_chain.append(cups[small_chain[j]])
        if relink_point < min:
            relink_point = max
        while relink_point in small_chain:
            relink_point -= 1
            if relink_point < min:
                relink_point = max
        #print(cur_link, small_chain, relink_point, cups[small_chain[-1]])
        cups[cur_link] = cups[small_chain[-1]]
        cups[small_chain[-1]] = cups[relink_point]
        cups[relink_point] = small_chain[0]
        cur_link = cups[cur_link]
        i += 1
    return cups

def answer2(deck):
    ans = 1
    for i in range(2):
        ans *= deck[ans]
    return ans

def parse2(input, itr):
    out = {}
    ranges = []
    for i, char in enumerate(input):
        ranges.append(int(char))
        if i == len(input)-1:
            out[int(char)] = len(input)+1
            break
        out[int(char)] = int(input[i + 1])
    for i in range(len(ranges)+1, itr+1):
        out[i] = i+1
    out[itr] = int(input[0])
    return out


cup_deck, min1, max1 = parse(input2)
print("Answer 1:", printpritty(play_game(cup_deck,min1, max1, 100))[1:])

size = 1000000
cup_deck2 = parse2(input2, size)
print("Answer 2:", answer2(play_game(cup_deck2, 1, size, 10000000)))
