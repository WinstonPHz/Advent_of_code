from copy import deepcopy
file1 = open("input.txt", "r")
inputs = ""
for line in file1:
    inputs += line

dishes = inputs.split("\n")
alergines = {}
ingredients = {}
meals = {}
all_meals = []
for i, dish in enumerate(dishes):
    ingred = dish.split(" (contains ")
    alerg = ingred[1][:-1].split(", ")
    all_meals.append(set(ingred[0].split(" ")))
    for alergy in alerg:
        if alergy in meals:
            meals[alergy].append(set(ingred[0].split(" ")))
        else:
            meals[alergy] = [set(ingred[0].split(" "))]
# Split them up into what each could be
cur_list = {}
for aleg in meals:
    for i, dish in enumerate(meals[aleg]):
        if i == 0:
            cur_list[aleg] = dish.copy()
        else:
            cur_list[aleg] = cur_list[aleg].intersection(dish)

for i in range(len(cur_list)):
    for aleg in cur_list:
        if len(cur_list[aleg]) == 1:
            for rem_aleg in cur_list:
                if aleg != rem_aleg:
                    to_remove = cur_list[aleg].pop()
                    cur_list[rem_aleg].discard(to_remove)
                    cur_list[aleg].add(to_remove)

def part1():
    new_meals = deepcopy(all_meals)
    for key1 in cur_list:
        to_remove = cur_list[key1].pop()
        cur_list[key1].add(to_remove)
        for cur_meal in new_meals:
            cur_meal.discard(to_remove)
    tots = 0
    for cur_meal in new_meals:
        tots += len(cur_meal)
    print("Answer 1:", tots)

def part2():
    all_keys = []
    for key in cur_list:
        all_keys.append(key)
    all_keys.sort()
    answer = ""
    for key in all_keys:
        answer += str(cur_list[key])[2:-2]+","
    print("Answer 2:", answer[:-1])
part1()
part2()