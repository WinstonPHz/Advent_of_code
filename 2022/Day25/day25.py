class snafu():
    def __init__(self):
        self.total = 0

    def add_num(self, snafu_num):
        for i, char in enumerate(snafu_num[::-1]):
            if char == "=":
                self.total -= 2*(5**i)
                continue
            if char == "-":
                self.total -= 1*(5**i)
                continue
            self.total += int(char)*(5**i)

    def root5(self):
        to_return = ""
        i = 0
        while True:
            if i == 0:
                dec0 = self.total%5
                if dec0 > 2:
                    if dec0 == 3:
                        to_return = "="
                        next_dec = 2
                    if dec0 == 4:
                        to_return = "-"
                        next_dec = 1
                    self.total += dec0
                    continue
                else:
                    to_return = str(self.total%5) + to_return
                    self.total -= self.total%5
            else:
                next_dec = int(self.total/(5**i))%5
                if next_dec > 2:
                    if next_dec == 3:
                        to_return = "=" + to_return
                        next_dec = 2
                    if next_dec == 4:
                        to_return = "-" + to_return
                        next_dec = 1
                    self.total += next_dec*5**i
                else:
                    to_return = str(next_dec) + to_return
                    self.total -= next_dec*5**i
            if self.total == 0: break
            i += 1
        return to_return




sn = snafu()

with open("input.txt", "r") as file:
    for line in file:
        line = line.strip("\n")
        sn.add_num(line)

print(sn.total)
print(sn.root5())