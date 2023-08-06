# part 1

letters = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

with open("input/3") as f:
    data = f.read().split("\n")

count = 0

for line in data:
    center = len(line) // 2
    i = set(line[:center]) & set(line[center:])
    count += letters.index(i.pop())

print(count)

# part 2

count2 = 0

for chunk in [data[i:i + 3] for i in range(0, len(data), 3)]:
    s = set(chunk.pop())
    while chunk:
        s &= set(chunk.pop())
    count2 += letters.index(s.pop())

print(count2)