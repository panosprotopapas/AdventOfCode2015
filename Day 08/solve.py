from json import dumps

with open("./Day 08/input.txt", encoding="utf-8") as f:
    raw = [l.strip() for l in f]

a = sum([len(i) for i in raw])
b = sum([len(eval(i)) for i in raw])
c = sum([len(dumps(i)) for i in raw])

print(f"Part 1: {a - b}")
print(f"Part 2: {c - a}")
