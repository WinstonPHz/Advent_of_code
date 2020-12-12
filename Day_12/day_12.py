file1 = open("input.txt", "r")
from copy import deepcopy

inputs = ""
for line in file1:
    inputs += line
inputs_arr = inputs.split("\n")

Directions = ["E", "N", "W", "S"]
State = [0, 0, 0]
way = [10, 1]

def move(dir, mag):
    global State
    if dir == "F":
        if Directions[State[2]] == "N":
            State[1] += mag
            return
        if Directions[State[2]] == "E":
            State[0] += mag
            return
        if Directions[State[2]] == "S":
            State[1] -= mag
            return
        if Directions[State[2]] == "W":
            State[0] -= mag
            return
    elif dir == "R":
        State[2] -= int(mag / 90)
    elif dir == "L":
        State[2] += int(mag / 90)
    elif dir == "N":
        State[1] += mag
    elif dir == "E":
        State[0] += mag
    elif dir == "S":
        State[1] -= mag
    elif dir == "W":
       State[0] -= mag
    while True:
        if State[2] > 3:
            State[2] -= 4
        elif State[2] < 0:
            State[2] += 4
        else:
            break

def move_way(dir, mag):
    global way
    global State
    if dir == "F":
        State[0] += mag*way[0]
        State[1] += mag*way[1]
    elif dir == "R":
        for i in range(int(mag/90)):
            way = [way[1], -way[0]]
    elif dir == "L":
        for i in range(int(mag/90)):
            way = [-way[1], way[0]]
    elif dir == "N":
        way[1] += mag
    elif dir == "E":
        way[0] += mag
    elif dir == "S":
        way[1] -= mag
    elif dir == "W":
        way[0] -= mag

for i, step in enumerate(inputs_arr):
    move(step[0], int(step[1:]))
print(abs(State[0])+abs(State[1]))

State = [0, 0, 0]
way = [10, 1]
print(State, way)
for i, step in enumerate(inputs_arr):
    move_way(step[0], int(step[1:]))
print(abs(State[0])+abs(State[1]))
