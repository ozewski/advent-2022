# part 1

with open("input/2") as f:
    data = list(map(str.split, f.read().split("\n")))

key = {"A": ["Y", "X", "Z"], "B": ["Z", "Y", "X"], "C": ["X", "Z", "Y"]}
values = ["X", "Y", "Z"]
score = 0

for opponent, me in data:
    d = key[opponent]
    if me == d[0]:
        score += 6
    elif me == d[1]:
        score += 3
    score += values.index(me) + 1

print(score)

# part 2

score2 = 0

for opponent, strat in data:
    d = key[opponent]
    me = d[2 - values.index(strat)]    
    if me == d[0]:
        score2 += 6
    elif me == d[1]:
        score2 += 3
    score2 += values.index(me) + 1

print(score2)