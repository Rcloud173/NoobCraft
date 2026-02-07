import random
from characters.enemy import Enemy

def combat(player):
    enemy = Enemy("Goblin", 15, (2, 5))
    print(f"A wild {enemy.name} appears!")

    while player.is_alive() and enemy.is_alive():
        action = input("Attack or Run? ").lower()

        if action == "attack":
            damage = random.randint(1, player.strength * 2)
            enemy.take_damage(damage)
            print(f"You hit the {enemy.name} for {damage}")

            if enemy.is_alive():
                enemy_damage = enemy.attack()
                player.take_damage(enemy_damage)
                print(f"The {enemy.name} hits you for {enemy_damage}")

        elif action == "run":
            print("You escaped!")
            return

    if player.is_alive():
        print("You won the fight!")
    else:
        print("You died.")
