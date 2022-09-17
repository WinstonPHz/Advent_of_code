file1 = open("input.txt", "r")
inputs = ""
for line in file1:
    inputs += line
commands = inputs.split("\n")
signal = []
amount = []
for command in commands:
    signal.append(command.split(" ")[0])
    amount.append(command.split(" ")[1])
out = False
master = signal.copy()
for test in range(len(signal)):
    signal = master.copy()
    acum = 0
    cur_signal = 0
    used_signals = []
    if signal[test] == "nop":
        signal[test] = "jmp"
    elif signal[test] == "jmp":
        signal[test] = "nop"
    elif signal[test] == "acc":
        continue
    while True:
        if cur_signal in used_signals:
            break
        used_signals.append(cur_signal)
        if cur_signal == len(signal):
            out = True
            print("Answer 2:", acum)
            break
        if signal[cur_signal] == "nop":
            cur_signal += 1
        elif signal[cur_signal] == "acc":
            acum += int(amount[cur_signal])
            cur_signal += 1
        elif signal[cur_signal] == "jmp":
            cur_signal += int(amount[cur_signal])
    if out:
        break
