from itertools import permutations

with open("./Day 13/input.txt", encoding="utf-8") as f:
    map = {
        f'{l.strip().split(" ")[0][0]}{l.strip().split(" ")[-1][0]}': (
            int(l.strip().split(" ")[3])
            if l.strip().split(" ")[2] == "gain"
            else -int(l.strip().split(" ")[3])
        )
        for l in f
    }

# Step 1
participants = list(set([key[0] for key in map]))
max_score = 0
for perm in permutations(participants):
    adjacent = (
        [f"{first}{second}" for first, second in zip(perm, perm[1:])]
        + [f"{perm[-1]}{perm[0]}"]
        + [f"{second}{first}" for first, second in zip(perm, perm[1:])]
        + [f"{perm[0]}{perm[-1]}"]
    )
    score = sum([map[i] for i in adjacent])
    max_score = max(score, max_score)
print(f"Step 1: {max_score}")

# Step 2
map = map | {f"U{p}": 0 for p in participants} | {f"{p}U": 0 for p in participants}
participants.append("U")
max_score = 0
for perm in permutations(participants):
    adjacent = (
        [f"{first}{second}" for first, second in zip(perm, perm[1:])]
        + [f"{perm[-1]}{perm[0]}"]
        + [f"{second}{first}" for first, second in zip(perm, perm[1:])]
        + [f"{perm[0]}{perm[-1]}"]
    )
    score = sum([map[i] for i in adjacent])
    max_score = max(score, max_score)
print(f"Step 2: {max_score}")
