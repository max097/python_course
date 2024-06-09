import random
import UNIT_CLASSES
class Team_class():
    dead_team = []
    alive_team =[]
    alive_team_in_arena = []
    dead_team_in_arena = []
    name = ""




    def create_start_team_for_player(self, player_name):
        self.alive_team = [UNIT_CLASSES.Healer_class(),
                UNIT_CLASSES.Wizard_class(),
                UNIT_CLASSES.Shaman_class(),
                UNIT_CLASSES.Archer_class()]
        self.name = f"{player_name}'s team"

    def create_comp_team_for_arena(self):
        comp_team = []

        list = [UNIT_CLASSES.Healer_class(),
                UNIT_CLASSES.Archer_class(),
                UNIT_CLASSES.Wizard_class(),
                UNIT_CLASSES.Shaman_class(),
                UNIT_CLASSES.Barbarian_class(),
                UNIT_CLASSES.Knight_class()]

        for i in range(5):
            rand_index = random.randint(0, len(list) - 1)
            rand_hero = list.pop(rand_index)
            comp_team.append(rand_hero)


        self.alive_team_in_arena = comp_team

        name_list = ["Monster's squad",
                     "Crocodiles",
                     "Supermen",
                     "WoW wariors",
                     "BlaBla squad",
                     "Pink ponys"]

        self.name = random.choice(name_list)

    def display_team_info_for_shop(self):
        x = 0

        for unit in self.alive_team:
            unit.unit_info_for_shop(x)
            x+= 1



    def display_team_info(self):
        x = 0
        for unit in self.alive_team_in_arena:
            print(f'{x}) {unit.unit_info()})')
            x += 1


    def check_alive(self):
        for unit in self.alive_team_in_arena:
            if unit.health_in_arena > 0:
                return True
        return False

    def check_dead_alive(self):
        lst = []
        for unit in self.alive_team_in_arena:
            if unit.life_status == True:
                lst.append(unit)
            else:
                self.dead_team_in_arena.append(unit)

        self.alive_team_in_arena = lst


