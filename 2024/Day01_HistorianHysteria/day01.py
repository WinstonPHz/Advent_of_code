left_list = []
right_list = []
right_list_pt2 = {}
with open("input.txt", "r") as file:
    for line in file:
        left, right = line.split("   ")
        left_list.append(int(left))
        right_list.append(int(right))
        right = int(right)
        if right in right_list_pt2.keys():
            right_list_pt2[right] += 1
        else:
            right_list_pt2[right] = 1


left_list.sort()
right_list.sort()
print(right_list_pt2)
distance = 0
similarity_score = 0
for i in range(len(left_list)):
    distance += abs(left_list[i] - right_list[i])
    if left_list[i] in right_list_pt2.keys():
        similarity_score += left_list[i] * right_list_pt2[left_list[i]]


print("answer 1: ", distance)
print("answer 2: ", similarity_score)