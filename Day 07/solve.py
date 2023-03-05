with open("./Day 07/input.txt", encoding="utf-8") as f:
    operations = [
        (l.strip().split(" -> ")[1], l.strip().split(" -> ")[0].split(" ")) for l in f
    ]
operations = sorted(sorted(operations), key=lambda x: len(x[0]))
first_item = operations.pop(0)
operations.append(first_item)

def run(operations):
    wires = dict()
    for (var, op) in operations:
        try:
            match len(op):
                case 1:
                    wires[var] = int(wires.get(op[0], op[0]))
                case 2:
                    if wires.get(op[1]) is not None:
                        wires[var] = ~wires[op[1]]
                case 3:
                    val = int(wires.get(op[0], op[0]))
                    match op[1]:
                        case "AND":
                            if wires.get(op[2]) is not None:
                                wires[var] = val & wires[op[2]]
                        case "OR":
                            if wires.get(op[2]) is not None:
                                wires[var] = val | wires[op[2]]
                        case "LSHIFT":
                            wires[var] = val << int(op[2])
                        case "RSHIFT":
                            wires[var] = val >> int(op[2])
        except ValueError:
            pass
    return wires.get('a')

part_1 = run(operations.copy())
print(f"Part 1: {part_1}")

operations[0] = ("b", [part_1])
part_2 = run(operations)
print(f"Part 2: {part_2}")