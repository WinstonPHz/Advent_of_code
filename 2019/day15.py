from intcode import computer
import copy

class graph():
    def __init__(self):
        self.c1 = computer("d15in.txt")
        self.graph_setup = {}
        self.robot_pos = [0,0]
        # Changes it so N=0 E=1 S=2 W=3
        self.direction_code = {0: 1,
                               1: 4,
                               2: 2,
                               3: 3}
        self.heading = 0
        # [X, Y] always
        self.heading_code = {0: [0, 1],   # North
                             1: [1, 0],   # East
                             2: [0, -1],  # South
                             3: [-1, 0]}  # West
        self.walls = []
        self.x_bound = [-1, 1]
        self.y_bound = [-1, 1]
        self.o2_found = False
        self.sensor_locaton = []
        self.o2_fill_list = []


    def move_robot_in_cur_heading(self):
        response = self.c1.run_computer(self.direction_code[self.heading])
        self.save_info(response)
        return response

    def turn_right(self):
        self.heading += 1
        if self.heading == 4:
            self.heading = 0

    def turn_left(self):
        self.heading -= 1
        if self.heading == -1:
            self.heading = 3

    def save_info(self, to_save):
        dx, dy = self.heading_code[self.heading]
        if to_save == 0:
            #print("Hit a wall at: ", [self.robot_pos[0]+dx, self.robot_pos[1]+dy])
            self.walls.append([self.robot_pos[0]+dx, self.robot_pos[1]+dy])
        if to_save > 0:
            self.robot_pos[0] += dx
            self.robot_pos[1] += dy
        if to_save == 2:
            self.o2_found = True
            self.sensor_locaton = copy.copy(self.robot_pos)
            print("Got the location of the o2 sensor its:", self.robot_pos[0]+dx, self.robot_pos[1]+dy)
        # This just makes the map window larger
        if self.robot_pos[0] >= self.x_bound[1]:
            self.x_bound[1] = self.robot_pos[0] + 1
        elif self.robot_pos[0] <= self.x_bound[0]:
            self.x_bound[0] = self.robot_pos[0] - 1
        if self.robot_pos[1] >= self.y_bound[1]:
            self.y_bound[1] = self.robot_pos[1] + 1
        elif self.robot_pos[1] <= self.y_bound[0]:
            self.y_bound[0] = self.robot_pos[1] - 1

    def follow_left(self):
        response = 1
        while True:
            prev_res = response
            response = self.move_robot_in_cur_heading()
            if response == 0:
                self.turn_right()
            if response == 1:
                self.turn_left()

            if self.o2_found and self.robot_pos == [0,0]:
                break
        self.plot_map()

    def plot_map(self):
        for j in range(self.y_bound[1]+5, self.y_bound[0]-5, -1):
            for i in range(self.x_bound[0]-5, self.x_bound[1]+5):
                if [i,j] in self.walls:
                    print("#", end="")
                elif [i,j] == self.robot_pos:
                    if self.heading == 0:
                        print("^", end="")
                    elif self.heading == 1:
                        print(">", end="")
                    elif self.heading == 2:
                        print("v", end="")
                    elif self.heading == 3:
                        print("<", end="")
                elif [i,j] == [0,0]:
                    print("0", end="")
                elif [i,j] == self.sensor_locaton:
                    print("S", end="")
                else:
                    print(end=".")
            print()
    def find_min(self, pos_list):
        cur_low = 10000
        for key, item in pos_list.items():
            if item < cur_low:
                cur_low = item
        for key, item in pos_list.items():
            if item == cur_low:
                return key, item
    def propigate(self, start, end):
        abs_min = {}
        cur_pos = start
        abs_min[tuple(cur_pos)] = 0
        pos_min = {}
        dist_from_origin = 0
        while True:
            x = cur_pos[0]
            y = cur_pos[1]
            connecting_nodes = [[x+1, y], [x, y+1], [x-1, y], [x, y-1]]
            for nx, ny in connecting_nodes:
                if [nx, ny] not in self.walls:
                    #Is this a wall?
                    if tuple([nx, ny]) not in pos_min.keys() and tuple([nx, ny]) not in abs_min.keys():
                        # Have we been here before? No then:
                        pos_min[tuple([nx, ny])] = dist_from_origin + 1
                    elif tuple([nx, ny]) in pos_min.keys():
                        # We have been there, is this one better?
                        if pos_min[tuple([nx, ny])] > dist_from_origin+1:
                            # This one is better lets add it to the list
                            pos_min[tuple([nx, ny])] = dist_from_origin+1
            # Now lets get our next check point
            if pos_min == {}:
                print("All points found")
                return

            cur_pos, dist_from_origin = self.find_min(pos_min)
            # Our next check point is the lowest to that point
            abs_min[cur_pos] = dist_from_origin
            self.o2_fill_list.append(dist_from_origin)
            # We dont want to come back here
            del pos_min[cur_pos]
            if cur_pos == tuple(end):
                # Found it!
                return dist_from_origin

g = graph()
g.follow_left()
min_dist = g.propigate([0,0], g.sensor_locaton)
print("Answer 1:", min_dist)
max_dist = g.propigate(g.sensor_locaton, [0,10000])
print("Answer 2:", max(g.o2_fill_list))