with open("./Day 03/input.txt", encoding="utf-8") as f:
    directions = f.read().strip()


def count_houses(input):
    houses = {(0, 0)}
    loc = (0, 0)
    for d in input:
        if d == ">":
            loc = (loc[0] + 1, loc[1])
        elif d == "<":
            loc = (loc[0] - 1, loc[1])
        elif d == "^":
            loc = (loc[0], loc[1] + 1)
        else:
            loc = (loc[0], loc[1] - 1)
        houses.add(loc)
    return houses


print(f"""Part 1: {len(count_houses(directions))}""")
print(
    f"""Part 2: {len(count_houses(directions[::2]).union(count_houses(directions[1::2])))}"""
)
