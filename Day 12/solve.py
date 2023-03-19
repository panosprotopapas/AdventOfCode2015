import json
import re

with open("./Day 12/input.txt", encoding="utf-8") as f:
    document = f.read().strip()

# Part 1
def count_digits(doc):
    r1 = re.findall(r"-?\d+", doc)
    r2 = map(int, r1)
    return sum(r2)


part_1 = count_digits(document)
print(f"Part 1: {part_1}")


# Part 2
def check_object(object):
    match type(object).__name__:

        case "list":
            done = [
                entry
                for entry in object
                if not isinstance(entry, dict) and not isinstance(entry, list)
            ]
            remaining = [
                entry
                for entry in object
                if isinstance(entry, dict) or isinstance(entry, list)
            ]

        case "dict":
            if "red" in object.values():
                return list(), list()
            done = [
                val
                for val in object.values()
                if val != "red"
                and not isinstance(val, dict)
                and not isinstance(val, list)
            ]
            remaining = [
                val
                for val in object.values()
                if val != "red" and (isinstance(val, dict) or isinstance(val, list))
            ]

        case other:
            print(type(object))
            done, remaining = list(), list()

    return done, remaining


remaining = [json.loads(document)]
part_2 = 0
while True:
    try:
        item = remaining.pop()
    except IndexError:
        break
    done, more_remaining = check_object(item)
    part_2 += count_digits(json.dumps(done))
    remaining.extend(more_remaining)


print(f"Part 2: {part_2}")
