
import Texts_module
class FightClass():
    def __init__(self, init_player_unit, init_comp_unit, init_fight_counter, init_player_team, init_comp_team):
        self.player_unit = init_player_unit
        self.comp_unit = init_comp_unit
        self.fight_counter = init_fight_counter
        self.player_team = init_player_team
        self.comp_team = init_comp_team

    def check_ability_computer(self):
        if self.player_unit.ability_cooldown == 0:
            self.comp_unit.ability_cooldown = 3
            return True
        else:
            self.comp_unit.ability_cooldown -= 1
            return False

    def check_ability_player(self):
        if self.player_unit.ability_cooldown == 0:
            print(f"{self.player_unit.name} is ready to use his ability ({self.player_unit.ability})")

            u_inp = ""
            while len(u_inp) == 0 or u_inp[0].lower() not in ["y", "n"]:
                u_inp = input("Do you wanna use ability? (Y/N) ---> ")

            if u_inp[0].lower() == "y":
                self.player_unit.ability_cooldown = 3
                return True
            elif u_inp[0].lower() == "n":
                self.player_unit.ability_cooldown = 0
                return False

        else:
            self.player_unit.ability_cooldown -= 1
            return False





    def fight(self):
        if self.fight_counter % 2 != 0 and not self.player_unit.is_stunned():
            if self.check_ability_player():

                self.player_unit.use_ability(defender = self.comp_unit,
                                             attacker_team = self.player_team,
                                             defender_team = self.comp_team)
            else:
                self.player_unit.hit(self.comp_unit)
            attacker = self.player_unit
            defender = self.comp_unit

        elif self.fight_counter % 2 == 0 and not self.comp_unit.is_stunned():
            if self.check_ability_computer():
                self.comp_unit.use_ability(defender = self.player_unit,
                                           attacker_team = self.comp_team,
                                           defender_team = self.player_team)
            else:
                self.comp_unit.hit(self.player_unit)
            attacker = self.comp_unit
            defender = self.player_unit

        print()
        for team in [self.player_team, self.comp_team]:
            print(f"{team.name}")
            for unit in team.alive_team_in_arena:
                unit.check_poison()
            print()


        print(Texts_module.display_fight_result_board(attacker, defender))

        for team in [self.player_team, self.comp_team]:
            team.check_dead_alive()