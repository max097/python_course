from abc import ABC, abstractmethod

from heroes_games import Armor_module
class Unit_class(ABC):
        name = ""
        health = 100
        health_in_arena = 0
        attack = 20
        defence = 5
        life_status = True
        ability = ""
        ability_value = 0
        ability_cooldown = 0

        helmet = Armor_module.Helmet()
        bodyarmor = Armor_module.Bodyarmor()
        boots = Armor_module.Boots()
        shield = Armor_module.Shield()

        magic_shield = False
        stunned = False
        poisoned_moves = 0
        poison_value = 0
        def hit_power(self):
                hit_power = self.attack
                return hit_power
        def defence_power(self):
                defence_power = self.defence + self.helmet.value + self.bodyarmor.value + self.boots.value + self.shield.value
                return defence_power

        def unit_info_for_shop(self, x):
                armor = ""
                for type in [self.helmet, self.bodyarmor, self.boots, self.shield]:
                        if type.value > 0:
                                armor += f"{type.name} ({type.value})"

                print(f"   {x}. {self.name}, armor - {armor}, weapon - , ability - ")

        def unit_info(self):
                return f"{self.name}, health - {self.health}, attack - {self.attack}, defence - {self.defence}, magic shield - {self.magic_shield}, stunned - {self.stunned}, poisoned(moves) - {self.poisoned_moves}"

        @abstractmethod
        def use_ability(self, defender, attacker_team, defender_team):
                pass

        def is_stunned(self):
                if self.stunned == True:
                        self.stunned = False
                        print(f'{self.name} is stunned and cannot make a move')
                        return True
                else:
                        return  False


        def has_magic_shield(self, enemy):

                if enemy.magic_shield == False:
                        print(f'{enemy.name} has magic shield. {self.name} is not able to hurt {enemy.name}')
                        enemy.magic_shield = False
                        return True
                else:
                        return False



        def hit(self, enemy):

                if  not self.has_magic_shield(enemy):

                        if enemy.defence_power() < self.hit_power():
                                enemy.health_in_arena = enemy.health_in_arena + enemy.defence_power() - self.hit_power()
                                print(f"{self.name} hit {enemy.name} by {self.hit_power() - enemy.defence_power()} points")

                        if self.defence_power() < enemy.hit_power():
                                self.health_in_arena = self.health_in_arena + self.defence_power() - enemy.hit_power()
                                print(f"{enemy.name} hit {self.name} by {enemy.hit_power() - self.defence_power} points")







        def check_poison(self):
                if self.poisoned_moves > 0:
                        self.health_in_arena -= self.poison_value
                        self.poisoned_moves -= 1
                        print(f"{self.name} has been damaged by poisoning for {self.poison_value} hp")