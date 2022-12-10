import copy
import json

direct = {}
current_folder = ""
cur_command = ""
sums = []
sizes = {}
with open("input.txt", "r") as file:
    for line in file:
        line = line.strip("\n")
        if "$" in line:
            cur_command = line.split(" ")[1]
            if "ls" in cur_command:
                continue
        if "cd" in cur_command:
            change_to = line.split("cd ")[1]
            if change_to == "/":
                current_folder = "/"
                direct[current_folder] = []
            elif change_to == "..":
                folder_components = current_folder.split("/")
                current_folder = "/"
                for i in range(1, len(folder_components)-2):
                    current_folder += folder_components[i] + "/"
                continue
            else:
                current_folder += change_to +"/"
                direct[current_folder] = []
        if "ls" == cur_command:
            direct[current_folder].append(line)

def folder_recon(folder):
    folder_size = 0
    for obj in direct[folder]:
        if "dir" in obj:
            new_folder_id = obj.split(" ")[1]
            new_folder_id = folder + new_folder_id + "/"
            folder_size += folder_recon(new_folder_id)
        else:
            file_size = int(obj.split(" ")[0])
            folder_size += file_size
    sizes[folder] = folder_size
    return folder_size

total_size = folder_recon("/")
ans1 = 0
for key in sizes:
    if sizes[key] <= 100000:
        ans1 += sizes[key]
print("Ans 1:", ans1)

Total_disk = 70000000
Total_free = Total_disk - sizes["/"]
Total_need = 30000000 - Total_free
to_delete = []
for key in sizes:
    if sizes[key] >= Total_need:
        to_delete.append(sizes[key])

print("Ans 2:", min(to_delete))
