with open("./Day 01/input.txt", encoding="utf-8") as f:
    input = f.read().strip()

print(f"""Part 1: {input.count("(") - input.count(")")}""")

for i in range(len(input) + 1):
    if input[:i].count("(") - input[:i].count(")") == -1:
        break

print(f"""Part 2: {i}""")
