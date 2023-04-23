from copy import copy
from json import dumps

with open("./Day 22/input.txt", encoding="utf-8") as f:
    boss_health = int(f.readline().strip().split(": ")[1])
    boss_damage = int(f.readline().strip().split(": ")[1])


class State:
    def __init__(
        self,
        boss_health,
        boss_damage,
        spells=dict(),
        health=50,
        mana=500,
        mana_spent=0,
        initial_round=False,
        round=0,
        hard=False,
    ):
        self.spells = spells
        self.boss_health = boss_health
        self.boss_damage = boss_damage
        self.health = health
        self.mana = mana
        self.mana_spent = mana_spent
        self.initial_round = initial_round
        self.new_states = list()
        self.shield = 0
        self.round = round
        self.game_over = False
        self.hard = hard

    def advance_state(self):
        if not self.initial_round:
            if self.hard:
                self.health -= 1
            self.cast_spells()
            self.boss_attacks()
            if self.hard:
                self.health -= 1
            self.cast_spells()
        self.create_new_states()
        self.game_over_check()

    def create_new_states(self):
        if not self.game_over:
            if self.boss_health > 30:
                available_spells = [
                    ("shield", 6, 113),
                    ("poison", 6, 173),
                    ("recharge", 5, 229),
                ]
            else:
                available_spells = [
                    ("missile", 1, 53),
                    ("drain", 1, 73),
                    ("shield", 6, 113),
                    ("poison", 6, 173),
                    ("recharge", 5, 229),
                ]
            for s in available_spells:
                if self.spells.get(s[0]) is None and self.mana >= s[2]:
                    spells_copy = copy(self.spells)
                    spells_copy[s[0]] = s[1]
                    new_state = State(
                        boss_health=self.boss_health,
                        boss_damage=self.boss_damage,
                        spells=spells_copy,
                        health=self.health,
                        mana=self.mana - s[2],
                        mana_spent=self.mana_spent + s[2],
                        round=self.round + 1,
                        hard=self.hard,
                    )
                    self.new_states.append(new_state)

    def cast_spells(self):
        if not self.game_over:
            for key in list(self.spells):
                val = self.spells.pop(key)
                if val > 1:
                    self.spells[key] = val - 1
                match key:
                    case "missile":
                        self.boss_health -= 4
                    case "drain":
                        self.health += 2
                        self.boss_health -= 2
                    case "shield":
                        self.shield = 7
                    case "poison":
                        self.boss_health -= 3
                    case "recharge":
                        self.mana += 101
            if self.boss_health < 1:
                self.game_over_check()

    def boss_attacks(self):
        if not self.game_over:
            damage_received = max(self.boss_damage - self.shield, 1)
            self.health -= damage_received
            if self.health < 1:
                self.game_over_check()

    def game_over_check(self):
        self.game_over = True

    def __repr__(self):
        r = {
            "Round": self.round,
            "Health": self.health,
            "Mana": self.mana,
            "Boss Health": self.boss_health,
            "Mana Spent": self.mana_spent,
            "Active Spells": self.spells,
        }
        return dumps(r, indent=4)

def run(boss_health, boss_damage, hard=False):
    states_to_check = [
        State(boss_health=boss_health, boss_damage=boss_damage, initial_round=True, hard=hard)
    ]
    minimum_cost = 99999
    while len(states_to_check):
        state = states_to_check.pop()
        state.advance_state()
        if state.game_over == True and state.boss_health < 1:
            minimum_cost = min(minimum_cost, state.mana_spent)
        states_to_check.extend(state.new_states)
    return minimum_cost

print(f"Part 1: {run(boss_health, boss_damage)}")
print(f"Part 2: {run(boss_health, boss_damage, hard=True)}")