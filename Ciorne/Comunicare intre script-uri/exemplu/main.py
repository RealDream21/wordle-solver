import subprocess

cmd = "python sub.py"
file = open("list.txt", "r+")
file.truncate(0)
file.seek(0)

for x in range(10):
    if x % 2 == 0:
        file.write(str(x) + "\n")

file.close()

p = subprocess.Popen(cmd, shell=True)
out, err = p.communicate()
print(err)
print(out)

file = open("list.txt", "r+")
lines = file.readlines()
for line in lines:
    x = int(line.strip("\n"))
    print(x)

