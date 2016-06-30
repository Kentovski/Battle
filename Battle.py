# /usr/bin/python

# ILYA MELNIKOV

import random
import time


class BattleField:
    def __init__(self):
        pass

    def start(self):
        pass


class Army:
    def __init__(self, squads, strategy):
        self.squads = squads
        self.strategy = strategy

    def attack(self):
        pass


class Squad:
    def __init__(self):
        pass

    def get_power(self):
        pass


class Unit:
    def __init__(self, recharge):
        self.health = 100
        self.recharge = recharge

    def do_attack(self):
        self.moment = time.time()

    def take_damage(self, value):
        self.health -= value

    def get_recharge(self):
        return self.recharge

    def get_health(self):
        return self.health

    def get_damage(self):
        return 0


class Solder(Unit):
    def __init__(self, recharge):
        super().__init__(self, recharge)
        self.experience = 0

    def increase_exp(self):
        if self.experience <= 50:
            self.experience += 1

    def do_attack(self):
        return get_damage(self)

    def get_damage(self):
        return 0.5 * (1 + self.health / 100) * random.randint(50 + self.experience, 100) / 100

    def take_damage(self, damage):
        self.health -= damage + 0.05 + self.experience / 100


class Vehicles(Unit):
    def __init__(self, recharge, operators):
        super().__init__(self, recharge)
        self.operators = operators

    def do_attack(self):
        return 0.5 * (1 + self.health / 100) * random.randint(50 + self.experience, 100) / 100

    def take_damage(self, damage):
        self.health -= damage + 0.05 + self.experience / 100


def main():
    pass

if __name__ == "__main__":
    main()