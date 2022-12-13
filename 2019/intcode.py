debug = 0
class computer():
    def __init__(self, file_name = ""):
        code = []

        with open(file_name) as file:
            for line in file:
                if line == "\n":
                    break
                components = line.split(",")
                for value in components:
                    code.append(int(value))
        self.input = code
        self.itr = 0

        self.relative_base = 0
        self.address = {}

        for i, value in enumerate(self.input):
            self.address[i] = value

    def change_address(self, addr, change_to):
        self.input[addr] = change_to
        self.address[addr] = change_to
    def run_computer(self, into = 0):
        # Example computer([1,255], 0)
        # test = 3,9,8,9,10,9,4,9,99,-1,8
        while self.address[self.itr] != 99:
            code = self.address[self.itr] % 100
            temp = str(int((self.address[self.itr]-code) / 100))
            while len(temp) < 3:
                temp = "0" + temp
            A_mode = int(temp[2])
            B_mode = int(temp[1])
            C_mode = int(temp[0])

            if code == 1:
                a = self.get_index(1, A_mode)
                b = self.get_index(2, B_mode)
                c = self.save_index(3, C_mode)
                if debug: print(f"Adding: {a} to {b} saving at {c}")
                self.address[c] = a + b
                self.itr += 4
            elif code == 2:
                a = self.get_index(1, A_mode)
                b = self.get_index(2, B_mode)
                c = self.save_index(3, C_mode)
                if debug: print(f"multiplying: {a} to {b} saving at {c}")
                self.address[c] = a * b
                self.itr += 4
            elif code == 3:
                a = self.save_index(1, A_mode)
                self.address[a] = into
                self.itr += 2
            elif code == 4:
                a = self.get_index(1, A_mode)
                self.itr += 2
                return a
            elif code == 5:
                a = self.get_index(1, A_mode)
                b = self.get_index(2, B_mode)
                if a != 0:
                    self.itr = b
                else:
                    self.itr += 3
            elif code == 6:
                a = self.get_index(1, A_mode)
                b = self.get_index(2, B_mode)
                if a == 0:
                    self.itr = b
                else:
                    self.itr += 3
            elif code == 7:
                a = self.get_index(1, A_mode)
                b = self.get_index(2, B_mode)
                c = self.save_index(3, C_mode)
                self.address[c] = 0
                if a < b:
                    self.address[c] = 1
                self.itr += 4
            elif code == 8:
                a = self.get_index(1, A_mode)
                b = self.get_index(2, B_mode)
                c = self.save_index(3, C_mode)
                self.address[c] = 0
                if a == b:
                    self.address[c] = 1
                self.itr += 4
            elif code == 9:
                a = self.get_index(1, A_mode)
                self.relative_base += a
                if debug: print("Chaning RB:" , self.relative_base)
                self.itr += 2
        return 99

    def get_index(self, step, mode):
        if mode == 1:
            ref_address = self.itr + step
        elif mode == 2:
            ref_address = self.relative_base + self.address[self.itr+step]
        elif mode == 0:
            ref_address = self.address[self.itr+step]
        if ref_address not in self.address.keys():
            self.address[ref_address] = 0
        a = self.address[ref_address]
        if debug: print(f"{step} is {a} for mode {mode}, itr {self.itr}, rb {self.relative_base}, ref {ref_address}, address {self.address[self.itr + 1]}")
        return a

    def save_index(self, step, mode):
        if mode == 1:
            ref_address = self.itr + step
        elif mode == 2:
            ref_address = self.relative_base + self.address[self.itr+step]
        elif mode == 0:
            ref_address = self.address[self.itr+step]
        #if ref_address not in self.address.keys():
        #    self.address[ref_address] = 0
        return ref_address

    



    def get_zero(self):
        print(self.address[0])