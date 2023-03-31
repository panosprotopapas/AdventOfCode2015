from itertools import combinations

from numpy import cumsum

with open("./Day 17/input.txt", encoding="utf-8") as f:
    sizes = sorted([int(l.strip()) for l in f])

max_choice = next(i for i, v in enumerate(list(cumsum(sizes))) if v > 150)
min_choice = next(i + 1 for i, v in enumerate(list(cumsum(sizes[::-1]))) if v > 150)


def process(size_list, choose):
    count = 0
    for comb in combinations(size_list, choose):
        if sum(comb) == 150:
            count += 1
    return count


part_1 = sum(
    [process(size_list=sizes, choose=c) for c in range(min_choice, max_choice + 1)]
)
print(f"Part 1: {part_1}")

# Guess there might be cases where no combinations are found for min choice. Then increase min choice (assumes a combination exists).
part_2 = 0
while part_2 == 0:
    part_2 = process(size_list=sizes, choose=min_choice)
    min_choice += 1
print(f"Part 2: {part_2}")
