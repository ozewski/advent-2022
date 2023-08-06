# part 1

with open("input/4") as f:
    data = map(lambda x: x.split(","), f.read().split("\n"))

count = 0
count2 = 0

for pair in data:
    t = []
    for x in pair:
        r = x.split("-")
        t.append(range(*map(int, r)))
    if len(t[0]) > len(t[1]):
        longer, shorter = t
    else:
        shorter, longer = t
    if (longer.stop - shorter.stop >= 0) and (shorter.start - longer.start >= 0):
        count += 1
    if (set(range(shorter.start, shorter.stop + 1)) & set(range(longer.start, longer.stop + 1))):
        count2 += 1

print(count)
print(count2)