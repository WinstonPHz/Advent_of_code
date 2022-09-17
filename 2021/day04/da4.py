def rows(number_array):
    out_row = {}
    for i in range(5):
        out_row[i] = number_array[i*5:i*5+5]
    return out_row

def columns(numer_array):
    out_col = {}
    for i in range(5):
        out_col[i] = []
        for j in range(5):
            out_col[i].append(numer_array[i+j*5])
    return out_col

def get_bingo_cards():
    board_count = -1
    first = 1
    boards = []
    for line in open("puz1", "r+"):
        line = line.strip("\n")
        if first:
            number_list = line.split(",")
            first = 0
        else:
            if line == "":
                board_count += 1
                boards.append([])
            else:
                for i, data in enumerate(line.split(" ")):
                    if data != "":
                        boards[board_count].append(data)
    winning_strips = {}
    for i in range(board_count+1):
        winning_strips[i] = {}
        winning_strips[i]["row"] = rows(boards[i])
        winning_strips[i]["col"] = columns(boards[i])
    return number_list, winning_strips

def remove_winners(winning_numbers, strips):
    for remove_number in winning_numbers:
        for key, board in strips.items():
            for item, list in board.items():
                for index, numbers in list.items():
                    if remove_number in numbers:
                        numbers.remove(remove_number)
                        if len(numbers) == 0:
                            return key, item, index, remove_number

list, boards = get_bingo_cards()
number_of_boards = len(boards)
board, sub, win, last_call = remove_winners(list, boards)
ans_1 = 0
winning_boards = [board]
for key, lists in boards[board][sub].items():
    for number in lists:
        ans_1 += int(number)
print("Answer 1:", ans_1*int(last_call))
print(board, sub, win, last_call)
for i in range(number_of_boards*25):
    board, sub, win, last_call = remove_winners(list, boards)
    if board not in winning_boards:
        winning_boards.append(board)
    if len(winning_boards) == 100:
        break
cum_sum = 0
for key, lists in boards[board][sub].items():
    for number in lists:
        cum_sum += int(number)
print("Answer 2:", cum_sum*int(last_call))