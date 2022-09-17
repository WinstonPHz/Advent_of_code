def get_list():
    number_list = []
    for line in open("puz1", "r+"):
        number_list.append(line.strip("\n"))
    return number_list

def get_lsb_string(list):
    gamma_zero = []
    gamma_one = []
    first = 1
    for line in list:
        if first:
            for bit in line:
                gamma_zero.append(0)
                gamma_one.append(0)
            first = 0
        for i, bit in enumerate(line):
            if bit == "1": gamma_one[i] += 1
            if bit == "0": gamma_zero[i] += 1
    gamma_string = ""
    epsilon_string = ""
    for i, bit in enumerate(gamma_one):
        if gamma_one[i] >= gamma_zero[i]:
            gamma_string += "1"
            epsilon_string += "0"
        else:
            gamma_string += "0"
            epsilon_string += "1"
    return gamma_string, epsilon_string

def rating(msb_string, list, ms):
    kept = []
    for i in range(len(msb_string)+1):
        for number in list:
            if number[i] not in msb_string[i]:
                if number not in kept:
                    kept.append(number)
        list = kept.copy()
        msb_string = get_lsb_string(list)[0] if ms == 1 else get_lsb_string(list)[1]
        if len(kept) == 1 : return kept[0]
        kept = []

gstring, estring = get_lsb_string(get_list())
print("answer 1:", int(gstring,2)*int(estring,2))

number_list = get_list()
power = int(rating(gstring, number_list, 1), 2)*int(rating(estring, number_list, 0), 2)
print("answer 2:",power)
