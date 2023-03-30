import numpy as np

with open("./Day 15/input.txt", encoding="utf-8") as f:
    ingredients = np.array(
        [
            [
                int(l.strip().replace(",", "").split(" ")[2]),
                int(l.strip().replace(",", "").split(" ")[4]),
                int(l.strip().replace(",", "").split(" ")[6]),
                int(l.strip().replace(",", "").split(" ")[8]),
                int(l.strip().replace(",", "").split(" ")[10]),
            ]
            for l in f
        ]
    )


def cook(ingredients, part_2=False):
    max_score = 0
    ingredients = ingredients.transpose()
    for a in range(101):
        for b in range(101 - a):
            for c in range(101 - a - b):
                for d in range(101 - a - b - c):
                    individual_scores = sum(
                        (ingredients * np.array([a, b, c, d])).transpose()
                    )
                    calories = individual_scores[-1]
                    if part_2 and calories != 500:
                        continue
                    round_score = (
                        0
                        if any(i < 0 for i in individual_scores)
                        else np.prod(individual_scores) / calories
                    )
                    max_score = max(max_score, round_score)
    return int(max_score)

print(f"Part 1: {cook(ingredients=ingredients)}")
print(f"Part 2: {cook(ingredients=ingredients, part_2=True)}")
