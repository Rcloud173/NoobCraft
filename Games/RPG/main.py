from characters.player import Player
from game.engine import combat

def create_player_from_input():
    while True:
        try:
            name = input("Enter character name: ")
            strength = int(input("Enter strength: "))
            intelligence = int(input("Enter intelligence: "))
            charisma = int(input("Enter charisma: "))
            return Player(name, strength, intelligence, charisma)
        except ValueError as e:
            print("Error:", e)

player = create_player_from_input()
print(player.display_stats())
combat(player)
