import random

d3 = "d3"
d4 = "d4"
d5 = "d5"
d6 = "d6"
d7 = "d7"
d8 = "d8"
d10 = "d10"
d12 = "d12"
d14 = "d14"
d16 = "d16"
d20 = "d20"
d24 = "d24"
d30 = "d30"

ability_modifiers = {
    k: v
    for k, v in zip(
        range(3, 19), [-3, -2, -2, -1, -1, -1, 0, 0, 0, 0, 1, 1, 1, 2, 2, 3]
    )
}


class Character:
    def __init__(self, name, alignment):
        self.name = name
        self.level = 0
        self.strength = (
            random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
        )
        self.agility = (
            random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
        )
        self.stamina = (
            random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
        )
        self.personality = (
            random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
        )
        self.intelligence = (
            random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
        )
        self.luck = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)

        self.FOR = ability_modifiers[self.strength]
        self.AGI = ability_modifiers[self.agility]
        self.STA = ability_modifiers[self.stamina]
        self.PER = ability_modifiers[self.personality]
        self.INT = ability_modifiers[self.intelligence]
        self.LUC = ability_modifiers[self.luck]
        self.hp = random.randint(1, 4) + self.STA
        self.fortitude = self.STA
        self.reflex = self.AGI
        self.willpower = self.PER
        self.cls = None
        self.xp = 0
        self.languages = ["Common"]
        self.alignment = alignment

    def __repr__(self):
        representation = f"""{self.name} is a level {self.level} character.
        HP: {self.hp}
        FOR: {self.FOR}
        AGI: {self.AGI}
        STA: {self.STA}
        PER: {self.PER}
        INT: {self.INT}
        LUC: {self.LUC}
        Fortitude: {self.fortitude}
        Reflex: {self.reflex}
        Willpower: {self.willpower}
        XP: {self.xp}
        """
        return representation

    def roll(self, die, modifier):
        """Usage: roll("d20", +1)"""
        die_size = int(die[1:])
        roll = random.randint(1, die_size)
        if roll == 1:
            result = "Fumble"
        elif roll >= 20:
            result = "Critical Hit"
        else:
            result = roll + modifier
        return f"You rolled a {result}!"

    def cast(self, die):
        """Usage: self.cast(d20)"""
        return self.roll(die, self.INT + self.level)
