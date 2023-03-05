import re

with open("./Day 05/input.txt", encoding="utf-8") as f:
    words = [l.strip() for l in f]


def is_good_part_1(word):
    if (
        len(re.findall(r"[aeiou]", word)) > 2
        and len(re.findall(r"(\w)\1", word))
        and not len(re.findall(r"ab|cd|pq|xy", word))
    ):
        return True
    return False


def is_good_part_2(word):
    if len(re.findall(r"(\w\w)\w*\1", word)) and len(re.findall(r"(\w)\w\1", word)):
        return True
    return False


print(f"""Part 1: {sum([is_good_part_1(word) for word in words])}""")
print(f"""Part 2: {sum([is_good_part_2(word) for word in words])}""")
