import random

class Enemy:
    def __init__(self, name, health, damage_range):
        self.name = name
        self.health = health
        self.damage_range = damage_range

    def attack(self):
        return random.randint(*self.damage_range)
    
    def take_damage(self, amount):
        self.health -= amount

    def is_alive(self):
        return self.health > 0