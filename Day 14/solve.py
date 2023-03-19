with open("./Day 14/input.txt", encoding="utf-8") as f:
    info = [
        (
            int(l.strip().split(" ")[3]),
            int(l.strip().split(" ")[6]),
            int(l.strip().split(" ")[13]),
        )
        for l in f
    ]

flight_time = [
    min(2503 % (i[1] + i[2]), i[1]) + i[1] * (2503 // (i[1] + i[2])) for i in info
]
print(f"Part 1: {max([i[0] * ft for i, ft in zip(info, flight_time)])}")


class Reindeer:
    def __init__(self, info):
        self.speed = info[0]
        self.fly = info[1]
        self.sleep = info[2]
        self.distance = 0
        self.state = "fly"
        self.remaining = self.fly
        self.score = 0

    def advance(self):
        self.remaining -= 1

        match self.state:
            case "fly":
                self.distance += self.speed
                if self.remaining == 0:
                    self.state = "sleep"
                    self.remaining = self.sleep

            case "sleep":
                if self.remaining == 0:
                    self.state = "fly"
                    self.remaining = self.fly


group = [Reindeer(info=i) for i in info]

for _ in range(2503):
    for reindeer in group:
        reindeer.advance()
    max(group, key=lambda x: x.distance).score += 1

print(f"Part 2: {max(group, key=lambda x: x.score).score}")
