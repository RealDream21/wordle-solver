file = open("list.txt", "r+")
lines = file.readlines()
file.truncate(0)
file.seek(0)

for line in lines:
    x = int(line.strip("\n"))
    cx = x
    while cx > 1:
        cx //= 2
        if cx % 2 == 1 and cx != 1:
            break
    else:
        file.write(str(x) + "\n")

file.close()