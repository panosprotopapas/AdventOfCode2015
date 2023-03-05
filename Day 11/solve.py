import re

with open("./Day 11/input.txt", encoding="utf-8") as f:
    puzzle_input = f.read().strip()


def _decompose(number):
    "https://codereview.stackexchange.com/questions/182733/base-26-letters-and-base-10-using-recursion"
    while number:
        number, remainder = divmod(number - 1, 26)
        yield remainder


def base_10_to_alphabet(number):
    "https://codereview.stackexchange.com/questions/182733/base-26-letters-and-base-10-using-recursion"
    return "".join(chr(ord("a") + part) for part in _decompose(number))[::-1]


def base_alphabet_to_10(letters):
    "https://codereview.stackexchange.com/questions/182733/base-26-letters-and-base-10-using-recursion"
    return sum(
        (ord(letter) - ord("a") + 1) * 26**i
        for i, letter in enumerate(reversed(letters))
    )


def run(puzzle_input):
    tests = False
    while tests == False:
        puzzle_input = base_10_to_alphabet(base_alphabet_to_10(puzzle_input) + 1)
        tests = all(
            [
                len(re.findall(r"(\w)\1", puzzle_input)) > 1,
                re.fullmatch(r"([a-h]|[jkmn]|[p-z])+", puzzle_input),
                re.findall(
                    r"(abc|bcd|cde|def|efg|fgh|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz)",
                    puzzle_input,
                ),
            ]
        )
    return puzzle_input


part_1 = run(puzzle_input)
print(f"Part 1: {part_1}")
print(f"Part 2: {run(part_1)}")
