
rules = {}
updates = []

with open("input.txt", "r") as file:
    for line in file:
        if "|" in line:
            key, value = line.strip("\n").split("|")
            key  = int(key)
            value = int(value)
            if key not in rules.keys():
                rules[key] = [value]
            else:
                rules[key].append(value)

        elif "," in line:
            levels = [int(level) for level in line.split(",")]
            updates.append(levels)

def check_rules(pages):
    pages = pages.copy()
    old_pages = []
    while len(pages) > 0:
        page = pages.pop(0)
        old_pages.append(page)
        #print(page, old_pages)
        if page not in rules.keys():
            continue
        page_rule = rules[page]
        #print(page_rule)

        for rule in page_rule:
            if rule in old_pages:
               return False
    return True

def fix_update(pages):
    pages = pages.copy()
    old_pages = []
    while not check_rules(old_pages+pages):
        page = pages.pop(0)
        old_pages.append(page)
        if page not in rules.keys():
            continue
        page_rule = rules[page]
        for rule in page_rule:
            if rule in old_pages:
                old_pages.remove(rule)
                pages.append(rule)
    new_list = old_pages + pages
    return new_list[int(len(new_list)/2)]

answer_1 = 0
answer_2 = 0
for update in updates:
    if check_rules(update):
        answer_1 += update[int(len(update)/2)]
    else:
        answer_2 += fix_update(update)

print("Answer 1:", answer_1)
print("Answer 2:", answer_2)