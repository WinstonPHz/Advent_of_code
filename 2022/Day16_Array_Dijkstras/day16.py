class tunnel_system():
    def __init__(self, extra_person = False):
        self.valves = {}
        self.flow_rates = {}
        with open("input.txt", "r") as file:
            for line in file:
                line = line.strip("\n")
                components = line.split(", ")
                valve = components.pop(0)
                flow = int(components.pop(0))
                leads_to = components
                self.valves[valve] = leads_to
                self.flow_rates[valve] = flow
        self.min_left = 30
        self.cur_flow_rate = 0
        self.magmaflowed = 0
        self.open_valves = []
        self.current_pos_me = "AA"
        self.cur_best_open_me = ""
        self.next_move_me = ""
        self.help = extra_person
        if extra_person == True:
            self.current_pos_e = "AA"
            self.cur_best_open_e = ""
            self.nex_move_e = ""
            self.min_left = 26

    def find_min(self, pos_list):
        cur_low = 500
        for key, dist in pos_list.items():
            if len(dist) < cur_low:
                cur_low = len(dist)
        for key, dist in pos_list.items():
            if len(dist) == cur_low:
                return key, dist

    def propigate(self, cur_pos):
        # From current node, how long will it take to get to every other node?
        abs_min = {}
        cur_pos = cur_pos
        abs_min[cur_pos] = []
        pos_min = {}
        dist_from_origin = []
        while True:
            connecting_nodes = self.valves[cur_pos]
            for tun in connecting_nodes:
                if tun not in pos_min.keys() and tun not in abs_min.keys():
                    # Have we been here before? No then:
                    pos_min[tun] = dist_from_origin + [tun]
                elif tun in pos_min.keys():
                    # We have been there, is this one better?
                    if pos_min[tun] > dist_from_origin + [tun]:
                        # This one is better lets add it to the list
                        pos_min[tun] = dist_from_origin + [tun]
            # Now lets get our next check point
            if pos_min == {}:
                return abs_min
            cur_pos, dist_from_origin = self.find_min(pos_min)
            # Our next check point is the lowest to that point
            abs_min[cur_pos] = dist_from_origin
            # We dont want to come back here
            del pos_min[cur_pos]

    def calc_next_open(self):
        min_dist = self.propigate(self.current_pos_me)
        best_gain_me = 0
        next_move_me = ""
        flow_ratios = {}
        best_dist_me = []
        for key, path in min_dist.items():
            # Get the best one to go to, then do that one
            if self.help:
                if key == self.cur_best_open_e:
                    # Don't repeat effort
                    continue
            dist = len(path) + 1 # The plus one is the valve time, actually really important
            flow = self.flow_rates[key]/dist
            flow_ratios[key] = flow
            if best_gain_me < flow:
                best_gain_me = flow
                next_move_me = key
                best_dist_me = path
        self.cur_best_open_me = next_move_me
        if best_dist_me == []:
            self.next_move_me = self.current_pos_me
        else:
            self.next_move_me = best_dist_me[0]
        # return next_move_me, cur_best_option
        # Now time to do the elephant in the room
        if self.help:
            min_dist_el = self.propigate(self.current_pos_e)
            best_gain_e = 0
            next_move_e = ""
            flow_ratios = {}
            best_dist_e = []
            for key, path in min_dist_el.items():
                if key == self.cur_best_open_me:
                    continue
                dist = len(path) + 1
                if dist == 0:
                    dist = 1
                if dist != 0:
                    flow = self.flow_rates[key] / dist
                    flow_ratios[key] = flow
                    if best_gain_e < flow:
                        best_gain_e = flow
                        next_move_e = key
                        best_dist_e = path
            self.cur_best_open_e = next_move_e
            if best_dist_e == []:
                self.nex_move_e = self.current_pos_e
            else:
                self.nex_move_e = best_dist_e[0]
        return

    def move_to(self):
        self.increment_time()
        if self.cur_best_open_me == self.current_pos_me:
            self.open_valve(self.cur_best_open_me)
        else:
            self.current_pos_me = self.next_move_me

        if self.help:
            if self.cur_best_open_e == self.current_pos_e:
                self.open_valve(self.cur_best_open_e)
            else:
                self.current_pos_e = self.nex_move_e

        return

    def open_valve(self, valve_to_open):
        self.cur_flow_rate += self.flow_rates[valve_to_open]
        self.flow_rates[valve_to_open] = 0
        self.open_valves.append(valve_to_open)

    def increment_time(self):
        # Do this to add a min then do the flow rate things, is done before vales are open
        self.min_left -= 1
        self.magmaflowed += self.cur_flow_rate
        return

    def run_arround(self):
        while self.min_left > 0:
            self.calc_next_open() # I know where to go next and so does the elephant
            self.move_to() # Move us, or if we are were we need to go open the valve
        if self.help:
            print("Answer 2:", self.magmaflowed)
        else:
            print("Answer 1:", self.magmaflowed)

ts = tunnel_system()
ts.run_arround()
tse = tunnel_system(True)
tse.run_arround()


