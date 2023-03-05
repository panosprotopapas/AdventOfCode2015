import numpy
import re

with open("./Day 06/input.txt", encoding="utf-8") as f:
    coords = [
        (
            re.search(r"[\sa-z]+[a-z]", l.strip()).group(),
            list(map(int, re.findall("\d+", l.strip()))),
        )
        for l in f
    ]

part_1 = numpy.zeros(shape=(1000, 1000), dtype=numpy.int8)
for c in coords:
    (x0, y0, x1, y1) = c[1]
    match c[0]:
        case "turn on":
            part_1[y0 : y1 + 1, x0 : x1 + 1] = 1
        case "turn off":
            part_1[y0 : y1 + 1, x0 : x1 + 1] = 0
        case "toggle":
            part_1[y0 : y1 + 1, x0 : x1 + 1] += 1
part_1 %= 2

part_2 = numpy.zeros(shape=(1000, 1000), dtype=numpy.int8)
for c in coords:
    (x0, y0, x1, y1) = c[1]
    match c[0]:
        case "turn on":
            part_2[y0 : y1 + 1, x0 : x1 + 1] += 1
        case "turn off":
            part_2[y0 : y1 + 1, x0 : x1 + 1] -= 1
            part_2 = numpy.where(part_1 < 0, 0, part_2)
        case "toggle":
            part_2[y0 : y1 + 1, x0 : x1 + 1] += 2

print(f"Part 1: {numpy.sum(part_1)}\nPart 2: {numpy.sum(part_2)}")
