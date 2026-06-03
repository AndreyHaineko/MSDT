"""
ИСХОДНЫЙ КОД (до добавления логирования) — лабораторная 4.

Текстовая RPG «Dungeon Explorer»: игрок исследует подземелье,
сражается с монстрами, подбирает предметы. Логирования нет — только print.

Финальная версия с logging: LR4.py
Описание точек логирования: CHANGES.md
"""

import random


class Character:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0

    def heal(self, amount):
        self.hp += amount
        if self.hp > 100:
            self.hp = 100


class Player(Character):
    def __init__(self, name):
        super().__init__(name, 100, 10)
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)

    def show_inventory(self):
        return self.inventory


class Monster(Character):
    def __init__(self, name, hp, attack):
        super().__init__(name, hp, attack)


def create_monster():
    names = ["Goblin", "Orc", "Troll"]
    name = random.choice(names)
    hp = random.randint(20, 50)
    attack = random.randint(5, 15)
    return Monster(name, hp, attack)


def battle(player, monster):
    print(f"A wild {monster.name} appears!")
    while player.is_alive() and monster.is_alive():
        action = input("Do you want to (a)ttack or (r)un? ")
        if action == "a":
            monster.take_damage(player.attack)
            print(f"{player.name} attacks for {player.attack} damage!")
            if monster.is_alive():
                player.take_damage(monster.attack)
                print(f"{monster.name} attacks for {monster.attack} damage!")
        elif action == "r":
            print(f"{player.name} ran away.")
            break
        else:
            print("Invalid action!")


def explore(player):
    while player.is_alive():
        encounter = random.choice(["monster", "item", "nothing"])
        if encounter == "monster":
            monster = create_monster()
            battle(player, monster)
        elif encounter == "item":
            item = "Health Potion"
            print(f"You found a {item}!")
            take_item = input("Do you want to take it? (y/n) ")
            if take_item == "y":
                player.add_item(item)
        else:
            print("You found nothing.")


def main():
    print("Welcome to the Dungeon Explorer!")
    player_name = input("Enter your character's name: ")
    player = Player(player_name)
    while player.is_alive():
        action = input("Do you want to (e)xplore or (i)nventory? ")
        if action == "e":
            explore(player)
        elif action == "i":
            print("Inventory:", player.show_inventory())
        else:
            print("Invalid action!")
    print("Game Over!")


if __name__ == "__main__":
    main()
