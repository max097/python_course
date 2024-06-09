
from .Unit_module import Unit_class
class Healer_class(Unit_class):
    name = "Healer"
    ability_value = 30
    ability = f"Heal 1 teammate by {ability_value} health points"

    def use_ability(self, defender, attacker_team, defender_team):
        for unit in attacker_team.alive_team_in_arena:
            if unit.life_status == True:
                unit.health_in_arena += self.ability_value
                if unit.health_in_arena > unit.health:
                    unit.health_in_arena = unit.health
                print(f'{self.name} heal {unit.name} by {self.ability_value} hp')