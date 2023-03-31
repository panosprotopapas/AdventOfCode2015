import numpy as np

with open("./Day 18/input.txt", encoding="utf-8") as f:
    state = np.array([[0 if char == "." else 1 for char in l.strip()] for l in f])


def add_border(state, part_2):
    h_zeros = np.zeros(len(state[0]))
    v_zeros = np.zeros(len(state) + 2)
    state = np.c_[v_zeros, np.vstack([h_zeros, state, h_zeros]), v_zeros]
    if part_2:
        state[1, 1] = state[-2, -2] = state[1, -2] = state[-2, 1] = 1
    return state


def neighborhood_sum(state, x, y):
    return np.sum(state[y - 1 : y + 2, x - 1 : x + 2])


def next_status(state, x, y):
    match state[y, x]:
        case 1:
            return 1 if neighborhood_sum(state, x, y) in [3, 4] else 0
        case 0:
            return 1 if neighborhood_sum(state, x, y) == 3 else 0


def next_state(state, part_2):
    state = np.array(
        [
            [next_status(state, x, y) for x in range(1, state.shape[0] - 1)]
            for y in range(1, state.shape[1] - 1)
        ]
    )
    return add_border(state, part_2)


def state_n(state, n, part_2):
    for _ in range(n):
        state = next_state(state, part_2)
    return state


def lights_n(state, n, part_2=False):
    return np.sum(state_n(state, n, part_2))


state = add_border(state, part_2=False)
part_1 = lights_n(state, n=100)
part_2 = lights_n(state, n=100, part_2=True)

print(f"Part 1: {int(part_1)}")
print(f"Part 2: {int(part_2)}")
