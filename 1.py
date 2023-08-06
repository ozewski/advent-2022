# part 1

with open("input/1") as f:
    data = f.read().split("\n\n")

nums = [sum(map(int, x.split("\n"))) for x in data]
print(max(nums))

# part 2

print(sum(sorted(nums, reverse=True)[:3]))