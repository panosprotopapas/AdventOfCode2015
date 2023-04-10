import itertools

with open("./Day 21/input.txt", encoding="utf-8") as f:
    boss_health = int(f.readline().strip().split(": ")[1])
    boss_damage = int(f.readline().strip().split(": ")[1])
    boss_armor = int(f.readline().strip().split(": ")[1])

class Character:
    def __init__(self, damage=0, armor=0, health=100):
        self.damage = damage
        self.armor = armor
        self.health = health
        self.cost = 0

    def equip(self, items):
        for item in items:
            self.cost += item[0]
            self.damage += item[1]
            self.armor += item[2]

    def fight(self, opponent):
        while self.health > 0:
            opponent.health -= max(self.damage - opponent.armor, 1)
            if opponent.health < 0:
                break
            self.health -= max(opponent.damage - self.armor, 1)
        if self.health > 0:
            return (True, self.cost)
        return (False, self.cost)
    
# Shop includes "buy nothing" option
shop_inventory = {
    "weapons": [(8, 4, 0), (10, 5, 0), (25, 6, 0), (40, 7, 0), (74, 8, 0)],
    "armor": [(0, 0, 0), (13, 0, 1), (31, 0, 2), (53, 0, 3), (75, 0, 4), (102, 0, 5)],
    "rings": [
        (0, 0, 0),
        (0, 0, 0),
        (25, 1, 0),
        (50, 2, 0),
        (100, 3, 0),
        (20, 0, 1),
        (40, 0, 2),
        (80, 0, 3),
    ],
}

# Part 1
min_cost = 999
for weapon in itertools.combinations(shop_inventory["weapons"], 1):
    for armor in itertools.combinations(shop_inventory["armor"], 1):
        for rings in itertools.combinations(shop_inventory["rings"], 2):
             boss = Character(damage=boss_damage, armor=boss_armor, health=boss_health)
             player = Character()
             player.equip(weapon)
             player.equip(armor)
             player.equip(rings)
             won, inventory_cost = player.fight(boss)
             if won:
                 min_cost = min(min_cost, inventory_cost)
print(f"Part 1: {min_cost}")

# Part 2

max_cost = 0
for weapon in itertools.combinations(shop_inventory["weapons"], 1):
    for armor in itertools.combinations(shop_inventory["armor"], 1):
        for rings in itertools.combinations(shop_inventory["rings"], 2):
             boss = Character(damage=boss_damage, armor=boss_armor, health=boss_health)
             player = Character()
             player.equip(weapon)
             player.equip(armor)
             player.equip(rings)
             won, inventory_cost = player.fight(boss)
             if not won:
                 max_cost = max(max_cost, inventory_cost)
print(f"Part 2: {max_cost}")
