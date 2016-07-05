# /usr/bin/python3

# MELNIKOV ILYA

from standart_conditions import *
from units import *


class Factory:
    def create_battlefield(self):
        armies = []
        armies_num = input('Enter number of armies: ')

        if armies_num == '' or armies_num == '0':
            armies_num = standart_armies_num
        else: armies_num = int(armies_num)

        for x in range(armies_num):
            armies.append(self.create_army())
        return Battlefield(armies=armies)

    def create_army(self):
        squads = []
        squads_per_army = input('Enter number of squads per army: ')
        if squads_per_army == '' or squads_per_army == '0':
            squads_per_army = standart_squads_per_army
        else: squads_per_army = int(squads_per_army)

        strategy = input('Enter strategy of squad: ')
        if strategy != 'random' and strategy != 'weakest' and strategy != 'strongest':
            strategy = standart_strategy
        for x in range(squads_per_army):
            squads.append(self.create_squad())
        return Army(squads=squads, strategy=strategy)

    def create_squad(self):
        soldiers = []
        vehicles = []
        for x in range(standart_soldiers_num):
            soldiers.append(self.create_soldier())
        for x in range(standart_vehicles_num):
            vehicles.append(self.create_vehicle())
        return Squad(units=soldiers + vehicles)

    def create_soldier(self):
        return Soldier(health=standart_soldier_health, recharge=standart_soldier_recharge)

    def create_vehicle(self):
        operators = []
        for x in range(operators_per_veh):
            operators.append(self.create_soldier())
        health = (operators_per_veh * standart_soldier_health + standart_vehicle_health) / (operators_per_veh + 1)
        return Vehicle(operators=operators, health=health, recharge=standart_vehicle_recharge)
