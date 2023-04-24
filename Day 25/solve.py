from itertools import islice
from re import findall

with open("./Day 25/input.txt", encoding="utf-8") as f:
    row, col = map(int, findall("\d+", f.read()))


def code_generator():
    num = 20151125
    while True:
        yield num
        num = (num * 252533) % 33554393


max_num = sum(range(row + col - 1)) + col
print(f"Solution: {next(islice(code_generator(), max_num - 1, max_num))}")
