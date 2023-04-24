from itertools import combinations
from math import prod

with open("./Day 24/input.txt", encoding="utf-8") as f:
    weights = sorted([int(l.strip()) for l in f], reverse=True)

def balance(weights, compartments):
    group_weight = sum(weights) / compartments
    for start_n in range(len(weights)):
        if sum(weights[:start_n]) >= group_weight:
            break

    for choice_size in range(start_n, len(weights)):
        possibilities = [
            comb for comb in combinations(weights, choice_size) if sum(comb) == group_weight
        ]
        if len(possibilities) > 0:
            break

    minimum_qe = prod(min(possibilities, key=lambda x: prod(x)))
    return minimum_qe

print(f"Part 1: {balance(weights=weights, compartments=3)}")
print(f"Part 2: {balance(weights=weights, compartments=4)}")