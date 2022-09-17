def get_input():
    jellies = {}
    i = 0
    jellies[-1] = ["."]*12
    for line in open("puz", "r+"):
        jellies[i] = ["."]
        line = line.strip("\n")
        for digit in list(line):
            jellies[i].append(int(digit))
        jellies[i].append(".")
        i += 1
    jellies[i] = ["."]*12
    return jellies

def printpritty(array):
    for key, value in sorted(array.items()):
        print(key, value)

def take_step(array, n):
    flashes = 0
    for step in range(n):
        # Step 1
        have_flashed = []
        for i in range(10):
            for j in range(1,11):
                array[i][j] += 1
        #Step 2
        while True:
            before_length = len(have_flashed)
            for i in range(10):
                for j in range(1,11):
                    around = [[i+1, j+1], [i+1, j], [i+1, j-1],[i, j+1], [i,j-1],[i-1, j+1], [i-1, j],[i-1, j-1]]
                    if array[i][j] > 9 and [i, j] not in have_flashed:
                        have_flashed.append([i, j])
                        for x, y in around:
                            if array[x][y] != ".":
                                array[x][y] += 1
            if len(have_flashed) == before_length:
                break
        #Step 3
        all_flash = 0
        for i in range(10):
            for j in range(1, 11):
                if array[i][j] > 9:
                    array[i][j] = 0
                    flashes += 1
                    all_flash += 1
        if all_flash == 100:
            print("ans 2:", step+1)
            break
        if step == 99:
            print("ans 1:", flashes)


jelly = get_input()
take_step(jelly, 1000)

