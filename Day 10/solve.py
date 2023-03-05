from re import findall

with open("./Day 10/input.txt", encoding="utf-8") as f:
    puzzle_input = f.read().strip()

def process(input):
    sequences = findall(r"(1+|2+|3+|4+|5+|6+|7+|8+|9+|0+)", input)
    occurences = [len(s) for s in sequences]
    return "".join([f"{o}{s[0]}" for o, s in zip(occurences, sequences)])

for i in range(50):
    if i == 40:
        print(f"Part 1: {len(puzzle_input)}")
    puzzle_input = process(puzzle_input)
print(f"Part 2: {len(puzzle_input)}")
