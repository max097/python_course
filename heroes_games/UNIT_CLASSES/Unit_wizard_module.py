from .Unit_module import Unit_class
class Wizard_class(Unit_class):
    name = "Wizard"
    ability = "Creates shield for all alies to protect them from 1 enemy attack"

    def use_ability(self, defender, attacker_team, defender_team):
        for unit in attacker_team.alive_team_in_arena:
            unit.magic_shield = True


