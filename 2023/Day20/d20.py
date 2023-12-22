from math import lcm
class Flipflop():
    def __init__(self, mod_name, components):
        self.mod_name = mod_name
        self.type = "FF"
        self.components = components.split(", ")
        self.state = 0
        self.incomming_signal = []
        self.firing = False

    def resolve_incomming_signal(self):
        if self.firing:
            self.firing = False
            if self.state:
                return 1
            else:
                return 0
        return -1


    def add_signal(self, signal, recieved_from, buttons):
        if not signal:
            self.firing = True
            if self.state:
                self.state = 0
            else:
                self.state = 1
        self.incomming_signal = signal
class Conjunction():
    def __init__(self, mod_name, components):
        mod_type, mod_name = mod_name[0], mod_name[1:]
        self.mod_name = mod_name
        self.components = components.split(", ")
        self.incomming_signal = {}
        self.state = 0
        self.type = "C"
        self.signal_frequency = {}
        self.lcm_found = False
        self.lcm = 0


    def resolve_incomming_signal(self):
        for component, signal in self.incomming_signal.items():
            if not signal:
                return 1
        return 0

    def add_signal(self, signal, recieved_from, buttons):
        self.incomming_signal[recieved_from] = signal
        if signal:
           self.signal_frequency[recieved_from] = buttons

        if len(self.signal_frequency.keys()) == len(self.incomming_signal.keys()):
            ans = lcm(*self.signal_frequency.values())
            if "rx" in self.components:
                print("Answer 2:", ans)
                quit()

class Broadcaster():
    def __init__(self, components):
        self.components = components.split(", ")
        self.mod_name = "broadcaster"
        self.incomming_signal = []
        self.state = 0
        self.type = "B"


    def resolve_incomming_signal(self):
        to_send = 0
        return to_send

    def add_signal(self, signal, recieved_from, nothing):
        self.incomming_signal.append(signal)


class Output():
    def __init__(self):
        self.components = []
        self.incomming_signal = []
        self.state = 0
        self.type = "O"

    def resolve_incomming_signal(self):
        return -1

    def add_signal(self, signal, recieved_from, nothing=""):
        return
class d19():
    def __init__(self):
        self.modules = {}
        self.low_count = 0
        self.high_count = 0
        self.button_count = 0

    def add_module(self, line):
        mod_name, components = line.split(" -> ")
        if "%" == mod_name[0]:
            self.modules[mod_name[1:]] = Flipflop(mod_name, components)
        elif "&" == mod_name[0]:
            self.modules[mod_name[1:]] = Conjunction(mod_name, components)
        else:
            self.modules[mod_name] = Broadcaster(components)

    def initialize_modules(self):
        for mod_id, module in self.modules.items():
            for component in module.components:
                if component not in self.modules.keys():
                    self.modules[component] = Output()
                    self.initialize_modules()
                    return
                if self.modules[component].type == "C":
                    self.modules[component].add_signal(0, mod_id, 0)

    def button_press(self):
        queue = ["broadcaster"]
        self.button_count += 1
        self.low_count += 1
        while queue:
            run_mod = queue.pop(0)
            recievers = self.modules[run_mod].components
            signal_sent = self.modules[run_mod].resolve_incomming_signal()
            if signal_sent == -1:
                continue
            for reciever in recievers:
                queue.append(reciever)
                if signal_sent:
                    self.high_count += 1
                else:
                    self.low_count += 1
                self.modules[reciever].add_signal(signal_sent, run_mod, self.button_count)


puz_in = {}
obj = d19()
with open("input.txt", "r") as file:
    for j, line in enumerate(file):
        line = line.replace("\n", "")
        obj.add_module(line)
obj.initialize_modules()
for i in range(6000):
    obj.button_press()
    if i == 999:
        print("Answer 1:", obj.low_count * obj.high_count)
