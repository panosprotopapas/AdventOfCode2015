with open("./Day 02/input.txt", encoding="utf-8") as f:
    box_sizes = [sorted(list(map(int, l.strip().split("x")))) for l in f]

part_1 = sum(3 * x * y + 2 * x * z + 2 * y * z for (x, y, z) in box_sizes)
print(f"""Part 1: {part_1}""")

part_2 = sum(2 * x + 2 * y + x * y * z for (x, y, z) in box_sizes)
print(f"""Part 2: {part_2}""")
