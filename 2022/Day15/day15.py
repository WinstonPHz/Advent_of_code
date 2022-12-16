import datetime
now = datetime.datetime.now()
def find_man(p1,p2):
    dx = abs(p2[0] - p1[0])
    dy = abs(p2[1] - p1[1])
    return dx+dy

class sensor():
    def __init__(self, start, closest):
        self.position = start
        self.closest_becon = closest
        self.manhatten = find_man(start,closest)

    def find_empty_in_row(self, row):
        x = self.position[0]
        y = self.position[1]
        dy_pos = y + self.manhatten
        dy_neg = y - self.manhatten
        if dy_neg <= row <= dy_pos:
            if row >= y:
                # Row in question is above the sensor
                width = (self.manhatten + y) - row

            elif row < y:
                # Row is below sensor
                width = abs(row - (y-self.manhatten))
            return [x-width, x+width]
        return []


debug = 0
if debug:
    puz = "input.txt"
    find_row = 10
    test_range = 20
else:
    puz = "input2.txt"
    find_row = 2000000
    test_range = 4000000

sensor_list = []
with open(puz, "r") as file:
    for line in file:
        line = line.strip("\n")
        sx, sy, bx, by = line.split(", ")
        sensor_list.append(sensor([int(sx), int(sy)], [int(bx), int(by)]))

def check_all_row(row_id):
    # Get a list of all the effected areas
    effected_zones = []
    for sensor in sensor_list:
        area = sensor.find_empty_in_row(row_id)
        if area != []:
            effected_zones.append(area)
    # Lets just get a list of all the numbers in the zones
    zone_bytes = []
    for zone in effected_zones:
        x1, x2 = zone
        if x1 not in zone_bytes:
            zone_bytes.append(x1)
        if x2 not in zone_bytes:
            zone_bytes.append(x2)
    # Sort that list so low is low and high is high
    zone_bytes.sort()
    # Make a smaller array that represents the covered zones
    compressed = [0]*len(zone_bytes)
    # If the zone is covered make the zeros in the compressed array 1 so we know that range is covered
    for zone in effected_zones:
        x1, x2 = zone
        for i in range(zone_bytes.index(x1), zone_bytes.index(x2)):
            compressed[i] = 1
    # Check the compressed values
    free_space = 0
    for i, j in enumerate(compressed):
        if j:
            free_space += zone_bytes[i+1] - zone_bytes[i]

        if j == 0 and i != len(compressed)-1:
            y = row_id
            x = zone_bytes[i]+1
            freq = x*4000000 + y
            print(zone_bytes)
            print(compressed)
            print([x,y])
            print("Answer 2:", freq)
            break

    if row_id == find_row:
        print("Answer 1:", free_space)

for r in range(find_row, test_range):
    check_all_row(r)

print("Only took: ", datetime.datetime.now() - now)