check_strings = []
file_strings = {}

with open("input.txt", "r") as file:
    for i, line in enumerate(file):
        file_strings[i] = line.strip("\n")

print(file_strings)