from pprint import pprint

with open("input/7") as f:
    inp = f.read().splitlines()

data = {"/": {}}
target = data["/"]
dirs = []
dir_sizes = {"/": 0}

for line in inp:
    d = line.split(" ")
    if d[1] == "cd":
        if d[2] == "/":
            target = data["/"]
            dirs = ["/"]
        elif d[2] == "..":
            dirs.pop()
            temp = data
            for dir in dirs:
                temp = temp[dir]
            target = temp
        else:
            name = d[2]
            target[name] = {}
            target = target[name]
            dirs.append(name)
    elif d[0] == "dir":
        target[d[1]] = {}
    elif d[1] != "ls":
        target[d[1]] = int(d[0])


def dir_sizes(dir):
    result = {}
    def inner(d):
        total = 0
        for k, v in d.items():
            if type(v) is dict:
                result[k] = result.setdefault(k, 0) + inner(v)
                total += result[k]
            else:
                total += v
        return total
    return inner(dir), result

pprint(data)
print()
sizes = dir_sizes(data)
print({k: v for k, v in sizes[1].items() if v <= 1000000})
print()
print(list(sizes[1].values()))
print(sum(sizes[1].values()))
print()
print([x for x in dir_sizes(data)[1].values() if x <= 100000])
print(sum(x for x in dir_sizes(data)[1].values() if x <= 100000))

