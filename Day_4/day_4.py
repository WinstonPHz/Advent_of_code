file1 = open("input.txt", "r")
input = ""
for line in file1:
    input += line
passports = input.split("\n\n")
fields = ["byr","iyr","eyr","hgt","hcl","ecl","pid","cid"]
goodFields = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
isValid = 0
isValid2 = 0


def compare(group1, group2):
    diff = []
    is_not_diff = False
    for item1 in group1:
        for item2 in group2:
            if item1 == item2:
                is_not_diff = True
        if is_not_diff == True:
            is_not_diff = False
        else:
            diff.append(item1)
    return diff

def byr(value):
    return 1920 <= int(value) <= 2002


def iyr(value):
    return 2010 <= int(value) <= 2020


def eyr(value):
    return 2020 <= int(value) <= 2030


def hgt(value):
    if value[-2:] == "cm":
        return 150 <= int(value[0:len(value) - 2]) <= 193
    elif value[-2:] == "in":
        return 59 <= int(value[0:len(value) - 2]) <= 76
    else:
        return False

def hcl(value):
    if value[0] == "#":
        return len(value[1:]) == 6
    else:
        return False

def ecl(value):
    group1 = ["amb","blu","brn","gry","grn","hzl","oth"]
    return len(compare([value], group1)) == 0


def pid(value):
    if len(value) == 9:
        for digit in value:
            try:
                int(digit)
            except:
                return False
        return True
    else:
        return False


def compare_adv(dict):
    GoodFieldsCheck = [byr(dict["byr"]),
                     iyr(dict["iyr"]),
                     eyr(dict["eyr"]),
                     hgt(dict["hgt"]),
                     hcl(dict["hcl"]),
                     ecl(dict["ecl"]),
                     pid(dict["pid"])]
    for field in GoodFieldsCheck:
        if field == True:
            continue
        else:
            return False
    return True

for passport in passports:
    lines = passport.split("\n")
    keys = []
    passFields = {}
    for line in lines:
        category = line.split(" ")
        for field in category:
            keys.append(field.split(":")[0])
            passFields[field.split(":")[0]] = field.split(":")[1]

    difference = compare(goodFields, keys)
    if len(difference) == 0:
        isValid += 1
        if compare_adv(passFields):
            isValid2 += 1

print(isValid)
print(isValid2)

