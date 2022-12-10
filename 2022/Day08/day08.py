import copy
debug = 1
trees = []
score = []
with open("input.txt", "r") as file:
    for line in file:
        line = line.strip("\n")
        tree_line = []
        for char in line:
            tree_line.append(int(char))
        trees.append(tree_line)

#make a nxm array
n = len(trees)
m = len(trees[0])
sceen = []
for i in range(n):
    sceen.append(copy.copy([1]+[0]*(m-2)+[1]))
    score.append(copy.copy([1]*m))
for i in range(len(sceen[0])):
    sceen[0][i] = 1
    sceen[n-1][i] = 1


def test_left():
    for i in range(n): # Row
        for j in range(m): # Col
            cur_tree_height = trees[i][j]
            dist_to_L_edge = j
            view_score = 0
            score_stop = True
            is_sceen = True
            # Go left:
            for x in range(1, dist_to_L_edge+1):
                test_tree = trees[i][j-x]
                view_score += 1
                if test_tree >= cur_tree_height:
                    is_sceen = False
                    break
            score[i][j] *= view_score
            if is_sceen == True:
                sceen[i][j] = 1
                continue


def test_right():
    for i in range(n):  # Row
        for j in range(m):  # Col
            cur_tree_height = trees[i][j]
            dist_to_R_edge = n - j
            view_score = 0
            is_sceen = True
            # Go Right:
            for x in range(1, dist_to_R_edge):
                test_tree = trees[i][j+x]
                view_score += 1
                if test_tree >= cur_tree_height:
                    is_sceen = False
                    break
            score[i][j] *= view_score
            if is_sceen == True:
                sceen[i][j] = 1
                continue

def test_up():
    for i in range(n):  # Row
        for j in range(m):  # Col
            cur_tree_height = trees[i][j]
            view_score = 0
            dist_to_top = i
            is_sceen = True
            # Go Up
            for x in range(1, dist_to_top+1):
                test_tree = trees[i-x][j]
                view_score += 1
                if test_tree >= cur_tree_height:
                    is_sceen = False
                    break
            score[i][j] *= view_score
            if is_sceen == True:
                sceen[i][j] = 1
                continue
def test_down():
    for i in range(n):  # Row
        for j in range(m):  # Col
            cur_tree_height = trees[i][j]
            view_score = 0
            dist_to_bot = m - i
            is_sceen = True
            # Go Down
            for x in range(1, dist_to_bot):
                test_tree = trees[i+x][j]
                view_score += 1
                if test_tree >= cur_tree_height:
                    is_sceen = False
                    break
            score[i][j] *= view_score
            if is_sceen == True:
                sceen[i][j] = 1
                continue

test_up()
test_down()
test_right()
test_left()


total_sceen = 0
for i in sceen:
    for j in i:
        if j:
            total_sceen += 1
max_score = 0
for i in score:
    if max(i) > max_score:
        max_score = max(i)

print("Ans1:", total_sceen)
print("Ans2:", max_score)