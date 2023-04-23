with open("./Day 23/input.txt", encoding="utf-8") as f:
    commands = [l.strip().replace(",", "").split(" ") for l in f]


def process(commands, a_val):
    registers = {"a": a_val, "b": 0}
    index = 0
    while True:
        try:
            cmd = commands[index]
            index += 1
            match cmd[0]:
                case "hlf":
                    registers[cmd[1]] //= 2
                case "tpl":
                    registers[cmd[1]] *= 3
                case "inc":
                    registers[cmd[1]] += 1
                case "jmp":
                    index = (
                        index + int(cmd[1][1:]) - 1
                        if cmd[1][0] == "+"
                        else index - int(cmd[1][1:]) - 1
                    )
                case "jie":
                    if registers[cmd[1]] % 2 == 0:
                        index = (
                            index + int(cmd[2][1:]) - 1
                            if cmd[2][0] == "+"
                            else index - int(cmd[2][1:]) - 1
                        )
                case "jio":
                    if registers[cmd[1]] == 1:
                        index = (
                            index + int(cmd[2][1:]) - 1
                            if cmd[2][0] == "+"
                            else index - int(cmd[2][1:]) - 1
                        )
        except IndexError:
            return registers["b"]


print(f"Part 1: {process(commands, 0)}")
print(f"Part 2: {process(commands, 1)}")
