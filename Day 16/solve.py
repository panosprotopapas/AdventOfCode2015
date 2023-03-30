with open("./Day 16/input.txt", encoding="utf-8") as f:
    aunts = [
        {
            l.strip()
            .replace(":", "")
            .split(" ")[2]: int(
                l.strip().replace(",", "").split(" ")[3],
            ),
            l.strip()
            .replace(":", "")
            .split(" ")[4]: int(
                l.strip().replace(",", "").split(" ")[5],
            ),
            l.strip()
            .replace(":", "")
            .split(" ")[6]: int(
                l.strip().replace(",", "").split(" ")[7],
            ),
        }
        for l in f
    ]

ticker_tape = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}

for i, aunt in enumerate(aunts):
    if all(ticker_tape.get(key) == val for key, val in aunt.items()):
        print(f"Part 1: {i+1}")

for i, aunt in enumerate(aunts):
    if any(
        ticker_tape.get(key) != val
        for key, val in aunt.items()
        if key not in ["cats", "trees", "pomeranians", "goldfish"]
    ):
        continue
    if any(
        ticker_tape.get(key) >= val
        for key, val in aunt.items()
        if key in ["cats", "trees"]
    ):
        continue
    if any(
        ticker_tape.get(key) <= val
        for key, val in aunt.items()
        if key in ["pomeranians", "goldfish"]
    ):
        continue
    print(f"Part 2: {i+1}")
