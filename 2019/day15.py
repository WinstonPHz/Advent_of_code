from intcode import computer

class graph():
    def __init__(self):
        self.c1 = computer("d15in.txt")
        self.graph_setup = {}
        self.robot_pos = [0,0]
        # Changes it so N=0 E=1 S=2 W=3
        self.direction_code = {0:1, 1:4, 2:2, 3:3}
        self.heading = 0
        self.heading_code = {0: [1, 0],
                             1: [0, 1],
                             2: [-1, 0],
                             3: [0, -1]}
        self.walls = []
        self.x_bound = [-1, 1]
        self.y_bound = [-1, 1]


    def move_robot_in_cur_heading(self):
        response = self.c1.run_computer(self.direction_code[self.heading])
        self.save_info(response)
        dx, dy = self.heading_code[self.heading]
        if response > 0:
            self.robot_pos[0] += dx
            self.robot_pos[1] += dy

        if self.robot_pos[0] >= self.x_bound[1]:
            self.x_bound[1] = self.robot_pos[0] + 1
        elif self.robot_pos[0] <= self.x_bound[0]:
            self.x_bound[0] = self.robot_pos[0] - 1
        if self.robot_pos[1] >= self.y_bound[1]:
            self.y_bound[1] = self.robot_pos[1] + 1
        elif self.robot_pos[1] <= self.y_bound[0]:
            self.y_bound[0] = self.robot_pos[1] - 1

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
        if to_save == 2:
            print("Got the location of the o2 sensor its:", self.robot_pos[0]+dx, self.robot_pos[1]+dy)

    def follow_wall(self):
        response = 0
        while True:
            prev_res = response
            response = self.move_robot_in_cur_heading()
            if response == 0 and prev_res == 1:
                self.turn_right()
            if response == 0 and prev_res == 0:
                self.turn_right()
                self.turn_right()
            if response == 2:
                break
            self.plot_map()

    def plot_map(self):
        print("------------------------------------------------------------------------------")
        for j in range(self.y_bound[0], self.y_bound[1]):
            for i in range(self.x_bound[0], self.x_bound[1]):
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
                else:
                    print(end=".")
            print()

g = graph()
g.follow_wall()