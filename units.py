# /usr/bin/python3

# MELNIKOV ILYA

import time
import random


class Unit:
    def __init__(self, **kwargs):
        self.health = kwargs['health']
        self.recharge = kwargs['recharge']
        self.status = True

    def do_attack(self):
        pass

    def take_damage(self, value):  # получить урон
        self.health -= value
        if self.health <= 0:
            self.status = False

    def get_recharge(self):
        pass

    def get_health(self):
        return self.health


class Soldier(Unit):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.experience = 0

    def increase_exp(self):
        if self.experience <= 50:
            self.experience += 1

    def get_success_attack(self):
        return (0.5 * (1 + self.health / 100) *
                random.randint(50 + self.experience, 100) / 100)

    def get_damage(self):  # сколько урона может нанести
        return 0.05 + self.experience / 100


class Vehicles(Unit):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.operators = kwargs['operators']

    def get_success_attack(self):
        pass

    def get_damage(self):
        pass


class Squad:
    def __init__(self, **kwargs):
        self.units = kwargs['units']

    def get_power(self):
        pass


class Army:
    def __init__(self, **kwargs):
        self.squads = kwargs['squads']
        self.strategy = kwargs['strategy']

    def attack(self, enemy):
        pass


class BattleField:
    def __init__(self, **kwargs):
        self.armies = kwargs['armies']

    def start(self):
        pass
