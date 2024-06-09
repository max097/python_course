from .Unit_module import Unit_class
class Barbarian_class(Unit_class):
    name = "Barbarian"
    ability = "Stun all enemy units for the next move"

    def use_ability(self, defender, attacker_team, defender_team):
        for unit in defender_team.alive_team_in_arena:
            if not self.has_magic_shield(unit):
                unit.stunned = True
                print(f"{self.name} give {unit.name} magic shield for 1 defence")