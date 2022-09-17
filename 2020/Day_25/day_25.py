from copy import deepcopy
file1 = open("input.txt", "r")
inputs = ""
for line in file1:
    inputs += line
puzzle = inputs.split("\n")

divide = 20201227
subject = 7
card_public_key = 1004920
door_public_key = 10441485


def transforms(subject_number, public_key):
    value = 1
    i = 1
    while True:
        value = value * subject_number
        value = value % divide
        if value == public_key:
            return i
        i += 1


def get_encrypt(subject_number, loop_size):
    value = 1
    i = 1
    while True:
        value = value * subject_number
        value = value % divide
        if i == loop_size:
            return value
        elif i >= loop_size:
            return 0
        i += 1

loop_size = transforms(7, card_public_key)
print("Part 1:", get_encrypt(door_public_key, loop_size))

