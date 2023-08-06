with open("input/6") as f:
    x = f.read()

# part 1

for i in range(len(x) - 4):
    seg = x[i:i+4]
    if len(set(seg)) == len(seg):
        print(i + 4)
        break

# part 2

for i in range(len(x) - 14):
    seg = x[i:i+14]
    if len(set(seg)) == len(seg):
        print(i + 14)
        break