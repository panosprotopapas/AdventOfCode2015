import numpy as np

with open("./Day 20/input.txt", encoding="utf-8") as f:
    input = int(f.read().strip())

# Part 1

highest_elf = round(input / 10) + 1
output = np.zeros(highest_elf)

for elf in range(1, highest_elf):
    houses = np.arange(elf, highest_elf, elf)
    output[houses] += elf
    if output[elf] > input / 10:
        break

part_1 = next(house for house, presents in enumerate(output) if presents > input / 10)
print(f"Part 1: {part_1}")


# Part 2

highest_elf = round(input / 11) + 1
output = np.zeros(highest_elf)

for elf in range(1, highest_elf):
    houses = np.arange(elf, min(highest_elf, 50 * elf), elf)
    output[houses] += elf
    if output[elf] > input / 11:
        break

part_2 = next(house for house, presents in enumerate(output) if presents > input / 11)
print(f"Part 2: {part_2}")
