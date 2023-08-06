import re, copy

# part 1

with open("input/5") as f:
    x = f.read()
    crates, instructions = x.split("\n\n")
    crates = [[*filter(lambda y: y != ".", x[::-1])] for x in zip(*crates.replace("]", "").replace("[", "").replace("    ", ".").replace(" ", "").split("\n")[:-1])]

crates2 = copy.deepcopy(crates)

for x in map(lambda x: re.findall("move (\d+) from (\d+) to (\d+)", x)[0], instructions.split("\n")):
    crate, target = crates[int(x[1]) - 1], crates[int(x[2]) - 1]
    for _ in range(int(x[0])):
        target.append(crate.pop())

print("".join(x[-1] for x in crates))

# part 2

for x in map(lambda x: re.findall("move (\d+) from (\d+) to (\d+)", x)[0], instructions.split("\n")):
    crate, target = crates2[int(x[1]) - 1], crates2[int(x[2]) - 1]
    target.extend(crate[-int(x[0]):])
    del crate[-int(x[0]):]

print("".join(x[-1] for x in crates2))