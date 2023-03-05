from re import findall
from itertools import permutations

with open("./Day 09/input.txt", encoding="utf-8") as f:
    routes = [findall(r"(\w+)\sto\s(\w+)\s=\s(\d+)", l.strip())[0] for l in f]

distance_matrix = dict()
for triplet in routes:
    if distance_matrix.get(triplet[0]) is None:
        distance_matrix[triplet[0]] = dict()
    if distance_matrix.get(triplet[1]) is None:
        distance_matrix[triplet[1]] = dict()
    distance_matrix[triplet[0]][triplet[1]] = int(triplet[2])
    distance_matrix[triplet[1]][triplet[0]] = int(triplet[2])

route_lengths = [
    sum([distance_matrix[permutation[i]][permutation[i + 1]] for i in range(7)])
    for permutation in permutations(distance_matrix.keys())
]

print(f"Part 1: {min(route_lengths)}")
print(f"Part 2: {max(route_lengths)}")
