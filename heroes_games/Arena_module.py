import Team_module
import Texts_module
import random
import Fight_module
class ArenaClass():


    def __init__(self, init_player_team, init_counter_arena):
        self.player_team = init_player_team
        self.player_team.alive_team_in_arena = self.player_team.alive_team
        self.player_team.dead_team_in_arena = []
        self.fight_counter = 0
        self.counter_arena = init_counter_arena





    def create_comp_team(self):
        self.comp_team = Team_module.Team_class()
        self.comp_team.create_comp_team_for_arena()

    def display_arena_board(self):
        print(Texts_module.display_arena_board(self.player_team, self.comp_team, self.counter_arena))
        print(self.player_team.name)
        print()
        print(self.player_team.display_team_info())
        print()
        print(self.comp_team.name)
        print()
        print(self.comp_team.display_team_info())


    def player_choose_unit(self, team):
        print(team.display_team_info())

        while True:
            u_inp = input("Choose unit ---> ")

            if len(u_inp) == 0:
                print("Write smth.")
                continue

            try:
                u_inp = int(u_inp)

            except:
                print("Write integer.")
                continue

            try:
                unit = team.alive_team_in_arena[u_inp]

            except:
                print("Write correct number.")
                continue

            return unit


    def comp_choose_unit(self, team):
        while True:
            unit = random.choice(team.alive_team_in_arena)
            if unit.health_in_arena > 0:
                return unit

    def arena_fight(self):
        for team in [self.player_team, self.comp_team]:
            for unit in team.alive_team_in_arena:
                unit.health_in_arena = unit.health

        while self.player_team.check_alive() and self.comp_team.check_alive():
            self.fight_counter += 1
            print(Texts_module.choose_unit_for_fight(self.fight_counter))

            if self.fight_counter % 2 != 0:
                #хід гравця
                print("Player chooses his unit for attack")
                player_unit = self.player_choose_unit(self.player_team)
                print()
                print('Player chooses enemy unit for attack')
                comp_unit = self.player_choose_unit(self.comp_team)
                attacker, defender = player_unit, comp_unit
            else:
                print("Computer chooses his unit for attack")
                comp_unit = self.comp_choose_unit(self.comp_team)
                print('Computer chooses his player\'s unit for attack')
                player_unit = self.comp_choose_unit(self.player_team)
                attacker, defender = comp_unit, player_unit

            print(Texts_module.display_fight_board(attacker, defender, self.fight_counter))
            fight = Fight_module.FightClass(player_unit, comp_unit, self.fight_counter, self.player_team, self.comp_team)
            fight.fight()


    def display_arena_results(self):
        print(Texts_module.display_arena_results(self.counter_arena))


    def arena_results(self):
        return [self.player_team.alive_team_in_arena,
                 self.player_team.dead_team_in_arena]