
class encryption():
    def __init__(self, key = 1, do_times = 1):
        self.main_array = []
        with open("input.txt", "r") as file:
            for line in file:
                line = line.strip("\n")
                self.main_array.append(int(line)*key)
        self.reference_array =[]
        for i in range(len(self.main_array)):
            self.reference_array.append(i)
        self.itterations = do_times
        self.run()

    def mixer(self):
        for k in range(self.itterations):
            for i in range(len(self.main_array)):
                index = self.reference_array.index(i)
                removed = self.reference_array.pop(index)
                new_index = (index + self.main_array[i]) % len(self.reference_array)
                self.reference_array.insert(new_index, removed)

    def find_answer(self):
        zero_index_main = self.main_array.index(0)
        zero_index_ref = self.reference_array.index(zero_index_main)
        find = [1000, 2000, 3000]
        answer = 0
        for f in find:
            answer += self.main_array[self.reference_array[(zero_index_ref+f) % len(self.reference_array)]]
        print("Answer", answer)

    def run(self):
        self.mixer()
        self.find_answer()

p1 = encryption()
p2 = encryption(811589153, 10)

"""
Answer 7225
Answer 548634267428
"""




