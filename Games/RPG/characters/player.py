from utils.validators import validate_name, validate_stats
from utils.display import stat_line

class Player:
    def __init__(self, name, strength, intelligence, charisma):
        name_error = validate_name(name)
        stats_error = validate_stats(strength, intelligence, charisma)

        if name_error:
            raise ValueError(name_error)
        if stats_error:
            raise ValueError(stats_error)
        

        self.name = name
        self.strength = strength
        self.intelligence = intelligence
        self.charisma = charisma

        self.max_health = 20 + strength * 2
        self.health = self.max_health
        self.inventory = []

    def is_alive(self):
        return self.health > 0
    
    def take_damage(self, amount):
        self.health = max(0, self.health - amount)

    def display_stats(self):
        return(
            f"{self.name}\n"
            f"{stat_line('STR', self.strength)}\n"
            f"{stat_line('INT', self.intelligence)}\n"
            f"{stat_line('CHA', self.charisma)}\n"
            f"HP: {self.health}/{self.max_health}"
        )