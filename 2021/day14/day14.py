def get_input():
    first = True
    formula = {}
    for line in open("/puz", "r+"):
        line = line.strip("\n")
        if first:
            starting_string = line
            first = False
        else:
            if line != "\n":
                line_comp = line.split(" -> ")
                formula[line_comp[0]] = line_comp[1]

    return starting_string, formula

def polymerize(s_string, codes):
    pairs = {}
    empty_pairs = {}
    for key in codes.keys():
        pairs[key] = s_string.count(key) if key in s_string else 0
        empty_pairs[key] = 0
    for i in range(40):
        new_pairs = empty_pairs.copy()
        for pair, count in pairs.items():
            if count > 0:
                new_pairs[pair[0]+codes[pair]] += count
                new_pairs[codes[pair]+pair[1]] += count
        pairs = new_pairs.copy()
        if i == 9: print("Ans1:", round(count_lib(pairs, s_string)))
    return pairs

def count_lib(string_lib, start_string):
    char_count = {}
    for key, item in string_lib.items():
        if key[0] != key[1]:
            for i in range(2):
                if key[i] not in char_count.keys():
                    char_count[key[i]] = item
                else:
                    char_count[key[i]] += item
        else:
            if key[0] not in char_count.keys():
                char_count[key[0]] = item*2
            else:
                char_count[key[0]] += item*2
    act_count = {}
    for key, item in char_count.items():
        if key in [start_string[0], start_string[-1]]:
            item += 1
        act_count[key] = item/2
    numbers = []
    for char, num in act_count.items():
        numbers.append(num)
    return (max(numbers) - min(numbers))


s_string, poly_template = get_input()
pair_count = polymerize(s_string, poly_template)
print("Ans2:", round(count_lib(pair_count, s_string)))







