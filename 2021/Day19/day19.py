class becon():
    def __init__(self, x, y, z = 0):
        self.rel_pos = [int(x), int(y), int(z)]

    def rotate_x(self):
        x, y, z = self.rel_pos
        self.rel_pos = [x, z, -y]
    def rotate_y(self):
        x, y, z = self.rel_pos
        self.rel_pos = [-z, y, x]
    def rotate_z(self):
        x, y, z = self.rel_pos
        self.rel_pos = [y, -x, z]

class scanner():
    def __init__(self, id):
        self.id = id
        self.location = [0,0,0]
        # X, Z, Y
        self.cur_rotation = [0,0]
        self.becon_list = []
        self.cur_orientation = 0
        self.locked = 0
        self.abs_becon_list = []

    def lock(self, x):
        self.location = [x[0], x[1], x[2]]
        for becon in self.becon_list:
            self.abs_becon_list.append([self.location[0] + becon.rel_pos[0],
                                        self.location[1] + becon.rel_pos[1],
                                        self.location[2] + becon.rel_pos[2]])
        self.locked = 1

    def add_becon(self, pos_array):
        self.becon_list.append(becon(pos_array[0], pos_array[1], pos_array[2]))

    def rotate_scanner(self):
        if self.locked == True:
            print("Trying to turn a locked scanners")
            return
        if self.cur_rotation == [3,5]:
            for becon in self.becon_list:
                becon.rotate_x()
                becon.rotate_y()
            self.cur_rotation = [0,0]
            return

        if self.cur_rotation[0] <= 3:
            self.cur_rotation[0] += 1
            for becon in self.becon_list:
                becon.rotate_x()

        if self.cur_rotation[0] == 4:
            self.cur_rotation[0] = 0
            if self.cur_rotation[1] <= 3:
                for becon in self.becon_list:
                    becon.rotate_z()
            if self.cur_rotation[1] == 3:
                for becon in self.becon_list:
                    becon.rotate_y()
            if self.cur_rotation[1] == 4:
                for becon in self.becon_list:
                    becon.rotate_y()
                    becon.rotate_y()
            self.cur_rotation[1] += 1

    def becon_set_matching(self, other_becon_set):
        if not locked:
            print("Trying to compare 2 unlocked sensors")
            return False, [0,0,0]
        for lbecon in self.abs_becon_list:
            for obecon in other_becon_set:
                N = []
                rel_sensor_location = [lbecon[0]-obecon.rel_pos[0],
                                       lbecon[1]-obecon.rel_pos[1],
                                       lbecon[2]-obecon.rel_pos[2]]
                shadow_becon_list = []
                for comp_becon in other_becon_set:
                    shadow_becon_list.append([rel_sensor_location[0]+comp_becon.rel_pos[0],
                                              rel_sensor_location[1]+comp_becon.rel_pos[1],
                                              rel_sensor_location[2]+comp_becon.rel_pos[2]])
                #print(self.abs_becon_list, "Shadow" ,shadow_becon_list)
                for B in shadow_becon_list:
                    if B in self.abs_becon_list:
                        N.append(B)
                    if len(N) >= 12:
                        #print(self.id)
                        #for num in N:
                            #print(num)
                        #print("Scanner Location:", rel_sensor_location)
                        return True, rel_sensor_location
        return False, [0, 0, 0]



# Reads the scanners into an array of scanner objects
scanners = []
not_locked = []
with open("input.txt","r") as puz:
    scanner_id = 0
    for line in puz:
        if "scanner" in line:
            scanner_id = int(line.split(" ")[2])
            scanners.append(scanner(scanner_id))
            not_locked.append(scanner_id)
            continue
        if "," not in line:
            continue
        loc_array = line.split(",")
        scanners[scanner_id].add_becon(loc_array)

scanners[0].lock([0,0,0])
not_locked.remove(0)
locked = [0]
print(not_locked)
print(locked)
# Scanners are rotating!
# Need to get the offset for a given scanner/becon
# Compair all becons with one another
while True:
    for nl_scaner in not_locked:
        #print("Starting work on: ", nl_scaner)
        for l_scanner in locked:
            #print("Testing it on:", l_scanner)
            worked = False
            uniq_rotations = []
            for i in range(24):
                #print("Rotation on nl:", scanners[nl_scaner].cur_rotation)
                worked, locked_location = scanners[l_scanner].becon_set_matching(scanners[nl_scaner].becon_list)
                if worked:
                    scanners[nl_scaner].lock(locked_location)
                    locked.append(nl_scaner)
                    not_locked.remove(nl_scaner)
                    break
                scanners[nl_scaner].rotate_scanner()
            if worked:
                break
        if worked:
            break
    print(locked)
    if len(locked) == len(scanners):
        break

# Get Uniq Becon List
uniq_becons = []
scaner_locals = []
for scanner in scanners:
    scaner_locals.append(scanner.location)
    print("Scanner Location",scanner.id, ":", scanner.location)
    bcn_list = scanner.abs_becon_list
    for bcn in bcn_list:
        if bcn not in uniq_becons:
            uniq_becons.append(bcn)

mand_dist = []
for i, scan_a in enumerate(scaner_locals):
    for j, scan_b in enumerate(scaner_locals):
        if i == j:
            continue
        dx = abs(scan_a[0] - scan_b[0])
        dy = abs(scan_a[1] - scan_b[1])
        dz = abs(scan_a[2] - scan_b[2])
        mand_dist.append(abs(dx+dy+dz))

print("Answer 1:", len(uniq_becons))
print("Answer 2:", max(mand_dist))
