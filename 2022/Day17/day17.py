from copy import copy
class tetris():
    def __init__(self):
        self.tiles = {}
        self.width = 7
        self.current_tile = 0
        # Adding the tiles to tiles [X,Y]
        self.tiles[0] = [[0,0], [1,0],[2,0],[3,0]]           # _
        self.tiles[1] = [[0,1], [1,1], [2,1], [1,0], [1,2]]   # +
        self.tiles[2] = [[0,0], [1,0],[2,0],[2,1],[2,2]]     # L
        self.tiles[3] = [[0,0], [0,1],[0,2],[0,3]]     # |
        self.tiles[4] = [[0,0], [1,0], [1,1], [0,1]]         # Box
        self.cur_start_height = 4 # 3 units above the floor right now
        self.insctuctions = []
        with open("input.txt") as file:
            for line in file:
                line = line.strip("\n")
                for char in line:
                    self.insctuctions.append(char)
        self.cur_instruction = 0
        self.graph = [[1,1,1,1,1,1,1]]
        for i in range(self.cur_start_height+10):
            self.graph.append([0]*7)
        self.box_pos = []
        self.p2found = False
        self.boulders_dropped = 0
        self.height_part_2 = 0
        self.steps_left_p2 = 1000000000000

    def get_instruction(self):
        inst = self.insctuctions[self.cur_instruction]
        self.cur_instruction += 1
        if self.cur_instruction >= len(self.insctuctions):
            self.cur_instruction = 0
        if inst == ">": # Right is True, Left if False
            return True
        else:
            return False

    def collision_wall(self, tile_local):
        for bx, by in tile_local:
            if -1 < bx < self.width:
                if self.graph[by][bx]:
                    return True
                continue
            else:
                return True
        return False

    def collision_bottom(self, tile_local):
        for bx, by in tile_local:
            if self.graph[by][bx]:
                return True
        return False

    def getblock_points(self, tx, ty, tile_points):
        bp = tile_points
        to_return = []
        for bx, by in bp:
            to_return.append([tx + bx, ty + by])
        return to_return

    def adjust_max_heights(self, tile_local):
        for bx, by in tile_local:
            self.graph[by][bx] = 1
            highest_y = by
            if highest_y+4 > self.cur_start_height:
                self.cur_start_height = highest_y+4
                for i in range(len(self.graph), self.cur_start_height+10):
                    self.graph.append([0]*7)
        return

    def sim_block_falling(self):
        block_points = self.tiles[self.current_tile]
        self.current_tile += 1
        if self.current_tile > 4:
            self.current_tile = 0
        tile_x = 2
        tile_y = self.cur_start_height
        old_pos = self.getblock_points(tile_x, tile_y, block_points)

        while True:
            # set the tile in space
            #self.display(old_pos)
            instruction = self.get_instruction()
            if instruction:
                tile_x += 1
            else:
                tile_x -= 1
            new_pos = self.getblock_points(tile_x, tile_y, block_points)
            if self.collision_wall(new_pos):
                # Collided with the wall, undo the hard work
                if instruction:
                    tile_x -= 1
                else:
                    tile_x += 1
            # Done with Left Right movement
            # starting Down Movement
            old_pos = self.getblock_points(tile_x, tile_y, block_points)
            tile_y -= 1
            new_pos = self.getblock_points(tile_x, tile_y, block_points)
            if self.collision_bottom(new_pos):
                # We Hit something
                self.boulders_dropped += 1
                new_pos = old_pos
                self.adjust_max_heights(new_pos)
                if self.current_tile == 0:
                    self.box_pos.append([tile_x, tile_y, self.boulders_dropped, self.cur_start_height-4, self.cur_instruction])
                break
            old_pos = new_pos

    def display(self, tile_local = []):
        print()
        for j in range(self.cur_start_height,0,-1):
            print(end = "|")
            for i in range(7):
                if [i, j] in tile_local:
                    print(end="@")
                elif self.graph[j][i]:
                    print(end = "#")
                else:
                    print(end = " ")
            print("|")

        print("---------")
        print("-0123456-")

    def check_repeat(self):
        if game.cur_start_height < 20:
            return
        if self.current_tile != 0:
            # There are 5 tiles, 1000000000000%5 = 0 only need to check if a repeat occured on the box block
            return
        if self.p2found:
            return
        deltas = {}
        b1x, b1y, num_dropped, actual_height, ci = self.box_pos[-1]
        for b2x, b2y, num_dropped2, actual_height2, ci2 in self.box_pos:
            if [b1x, b1y] == [b2x, b2y]:
                continue
            if b1x == b2x and ci == ci2:
                deltas[b1y-b2y] = num_dropped - num_dropped2

        for delta in deltas.keys():
            self.p2found = True
            print(f"Actual Repeat every {delta} heights")
            start_height = actual_height - delta
            print(f"starting at a height of {start_height}")
            print(f"After every {deltas[delta]} rocks")
            first = num_dropped - deltas[delta]
            print(f"First before repeated rock is {first}")
            left_to_do = 1000000000000 - first
            steps_left_p2 = left_to_do%deltas[delta]
            # Will be a multiple of 5, now we just need to check up from our start find the detla then call it
            dy = 0
            for bx, by, cur, ach, ci in self.box_pos:
                if cur == first + steps_left_p2:
                    dy = ach-start_height
                    break
            to_repeat = int(left_to_do/deltas[delta])
            print(f"Repeating {delta} a total of {to_repeat} times")
            big_jump = delta*int(left_to_do/deltas[delta])
            print(f"Height added in {left_to_do} steps is {big_jump}")
            print(f"Height added in {steps_left_p2} steps is {dy}")
            self.height_part_2 = start_height + big_jump + dy
            # add one for the height of the block
            print(f"Height is {self.height_part_2}")


    def go_til_repeat(self):
        i = 0
        ans1 = 0
        while True:
            self.sim_block_falling()
            self.check_repeat()
            if i == 2021:
                ans1 = self.cur_start_height -4
            i += 1
            if i > 2021 and self.p2found:
                break
        print("Answer 1:", ans1)
        print("Answer 2:", self.height_part_2)

game = tetris()
game.go_til_repeat()

