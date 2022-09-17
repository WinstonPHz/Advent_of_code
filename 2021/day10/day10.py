def get_input():
    puz = []
    for line in open("puz", "r+"):
        line = line.strip("\n")
        puz.append(line)
    return puz

def get_cor(puzzle):
    closed = ["<>", "{}", "[]", "()"]
    close_b = [">", "]", ")", "}"]
    puz = puzzle
    while True:
        old_len = len(puz)
        for cp in closed:
           puz = puz.replace(cp, "")
        if len(puz) == old_len:
            break
    for char in puz:
        if char in close_b:
            return True, char
    return False, puz


def get_score(corr_array):
    scoring = {")":3, "]":57, "}":1197, ">":25137}
    score = 0
    for char in corr_array:
        score += scoring[char]
    return score

def get_score2(corr_array):
    scoring = {"(":1, "[":2, "{":3, "<":4}
    scores = []
    for puz in corr_array:
        score = 0
        for char in puz[::-1]:
            score *= 5
            score += scoring[char]
        scores.append(score)
    scores.sort()
    true_score = scores[round(len(scores)/2)]
    return true_score

puzzle = get_input()
corrupted_char = []
incomplete = []
for puz in puzzle:
    boool, string = get_cor(puz)
    if boool:
        corrupted_char.append(string)
    else:
        incomplete.append(string)














print("Answer 1:", get_score(corrupted_char))
print("Answer 2:", get_score2(incomplete))
