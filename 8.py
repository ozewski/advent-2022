# from pprint import pprint
from collections import defaultdict
from math import prod

with open("input/8") as f:
    data = [[*map(int, list(line))] for line in f.read().splitlines()]

view_distances = defaultdict(list)

def visible(data, backwards=False, transform=lambda x,y: (x,y)):
    r = set()
    for y in range(len(data)):    # \/ - value, position
        tallest, obstruction = -1, [-1, 1]
        row = data[y][::-1] if backwards else data[y]
        l = len(row)
        for x in range(l):
            n = row[x]
            coordinate = transform(x, y)]
            if n <= obstruction[0]:
                obstruction[1] = x
            obstruction[0] = n
            view_distances[coordinate].append(x - obstruction[1] + 1)]
            if n > tallest:
                tallest = n
                r.add(coordinate)
    return r

l = len(data) - 1
flipped = list(zip(*data))
total = visible(data) \
| visible(data, backwards=True, transform=lambda x,y: (l-x,y)) \
| visible(flipped, transform=lambda x,y: (y,x)) \
| visible(flipped, backwards=True, transform=lambda x,y: (y,l-x))

print(len(total))
print(max(map(prod, view_distances.values())))

_ = data.copy()
for (x, y), n in view_distances.items():
    _[y][x] = n
#pprint(_)

for c, i in view_distances.items():
    a = prod(i)
    if a > 100:
        print(c, i)
        print(a)