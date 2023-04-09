import re

with open("./Day 19/input.txt", encoding="utf-8") as f:
    replacements = dict()
    for l in f:
        if l.strip() == "":
            l = f.readline()
            break
        if replacements.get(l.strip().split(" => ")[0]):
            replacements[l.strip().split(" => ")[0]].append(l.strip().split(" => ")[1])
        else:
            replacements[l.strip().split(" => ")[0]] = [l.strip().split(" => ")[1]]
    start = l.strip()


def replace_nth(start, replacements):
    for old, list_of_new in replacements.items():
        for n in range(1, start.count(old) + 1):
            where = [m.start() for m in re.finditer(old, start)][n - 1]
            before = start[:where]
            for new in list_of_new:
                after = start[where:].replace(old, new, 1)
                yield before + after


molecules = set()
for i in replace_nth(start=start, replacements=replacements):
    molecules.add(i)
part_1 = len(molecules)

print(f"Part 1: {part_1}")

# Crappy crappy 2nd part solution.. based on Reddit's insight that Rn = "(", Ar = ")", and Y = ","
# Probably only works for my input


with open("./Day 19/input.txt", encoding="utf-8") as f:
    for l in f:
        if l.strip() == "":
            l = f.readline()
            break
    end = l.strip()

end = end.replace("Rn", "(")
end = end.replace("Ar", ")")
end = end.replace("Y", ",")
end = end.replace("Ca", "Z")
end = end.replace("Ti", "T")


part_2 = 0

def count_replacements(string, old, new, counter):
    while True:
        if string == string.replace(old, new):
            break
        counter += 1
        string = string.replace(old, new, 1)
    return string, counter

end, part_2 = count_replacements(end, "ZZ", "Z", part_2)
end, part_2 = count_replacements(end, "TT", "T", part_2)
end, part_2 = count_replacements(end, "(BF)", "(Mg)", part_2)
end, part_2 = count_replacements(end, "TMg", "Mg", part_2)
end, part_2 = count_replacements(end, "Si(Mg)", "Z", part_2)
end, part_2 = count_replacements(end, "ZF", "F", part_2)
end, part_2 = count_replacements(end, "T(F)", "B", part_2)
end, part_2 = count_replacements(end, "Si(F,F)", "Z", part_2)
end, part_2 = count_replacements(end, "Th(F)", "Al", part_2)
end, part_2 = count_replacements(end, "Si(F)", "P", part_2)
end, part_2 = count_replacements(end, "P(F)", "Z", part_2)
end, part_2 = count_replacements(end, "BP", "T", part_2)
end, part_2 = count_replacements(end, "ZZ", "Z", part_2)
end, part_2 = count_replacements(end, "TT", "T", part_2)
end, part_2 = count_replacements(end, "TMg", "Mg", part_2)
end, part_2 = count_replacements(end, "Si(Mg)", "Z", part_2)
end, part_2 = count_replacements(end, "ZZ", "Z", part_2)
end, part_2 = count_replacements(end, "ZF", "F", part_2)
end, part_2 = count_replacements(end, "SiTh", "Z", part_2)
end, part_2 = count_replacements(end, "ZZ", "Z", part_2)
end, part_2 = count_replacements(end, "Si(F,F)", "Z", part_2)
end, part_2 = count_replacements(end, "ZZ", "Z", part_2)
end, part_2 = count_replacements(end, "ZF", "F", part_2)
end, part_2 = count_replacements(end, "PT", "P", part_2)
end, part_2 = count_replacements(end, "PB", "Z", part_2)
end, part_2 = count_replacements(end, "ZZ", "Z", part_2)
end, part_2 = count_replacements(end, "ZF", "F", part_2)
end, part_2 = count_replacements(end, "ZP", "P", part_2)
end, part_2 = count_replacements(end, "ZSi", "Si", part_2)
end, part_2 = count_replacements(end, "SiAl", "F", part_2)
end, part_2 = count_replacements(end, "PMg", "F", part_2)
end, part_2 = count_replacements(end, "Si(F,F)", "Z", part_2)
end, part_2 = count_replacements(end, "ZP", "P", part_2)
end, part_2 = count_replacements(end, "P(F)", "Z", part_2)
end, part_2 = count_replacements(end, "ZZ", "Z", part_2)
end, part_2 = count_replacements(end, "ZF", "F", part_2)
end, part_2 = count_replacements(end, "ThF", "Al", part_2)
end, part_2 = count_replacements(end, "C(F)", "N", part_2)
end, part_2 = count_replacements(end, "NAl", "e", part_2)

print(f"Part 2: {part_2}")