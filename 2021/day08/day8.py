def find_numbers(ins):
    parts = {}
    out_code = {}
    parts[5] = []
    parts[6] = []
    for display in ins.split(" "):
        if len(display) == 2:
            out_code[1] = set(display)
        elif len(display) == 3:
            out_code[7] = set(display)
        elif len(display) == 4:
            out_code[4] = set(display)
        elif len(display) == 7:
            out_code[8] = set(display)
        else:
            parts[len(display)].append(list(display))
    # Find 0
    seg_1 = set(out_code[7]).symmetric_difference(out_code[1])
    g1 = out_code[1]
    g2 = out_code[4].symmetric_difference(out_code[1])
    g3 = out_code[8].symmetric_difference(out_code[4]).symmetric_difference(seg_1)
    for number in parts[6]:
        if list(g3)[0] not in list(number) or list(g3)[1] not in list(number):
            out_code[9] = set(number)
            parts[6].remove(number)
            seg_5 = set(out_code[8]).symmetric_difference(number)

    for number in parts[6]:
        if list(g2)[0] not in number or list(g2)[1] not in number:
            out_code[0] = set(number)
            parts[6].remove(number)
            out_code[6] = set(parts[6][0])

    for number in parts[5]:
        if list(seg_5)[0] in number:
            out_code[2] = number
            parts[5].remove(number)

    for number in parts[5]:
        if list(g1)[0] in number and list(g1)[1] in number:
            out_code[3] = set(number)
            parts[5].remove(number)
            out_code[5] = set(parts[5][0])
    return out_code


def get_final_number(key, output):
    return_number = ""
    for rm in output:
        for number, seq in key.items():
            if len(set(list(rm)).symmetric_difference(seq)) == 0:
                return_number += str(number)
    return int(return_number)

def get_input():
    sums = []
    incode = []
    outcode = []
    for line in open("puz", "r+"):
        line = line.strip("\n")
        if line != "":
            code = line.split(" | ")
            incode.append(code[0])
            outcode.append(code[1])
            code_key = find_numbers(code[0])
            sums.append(get_final_number(code_key, code[1].split(" ")))

    return incode, outcode, sums

ins, outs, sums = get_input()
cum_sum = 0
for out in outs:
    for puz in out.split(" "):
        if len(puz) in [2, 3, 4, 7]:
            cum_sum += 1
print("Answer 1:", cum_sum)
cum_sum = sum(sums)
print("Answer 2:", cum_sum)
