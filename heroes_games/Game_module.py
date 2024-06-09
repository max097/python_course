import UNIT_CLASSES
import Texts_module
from Arena_module import ArenaClass
import Team_module

class Game_class():
    base_reward = 100
    player_name = None
    player_gold = 1000
    arena_counter = 0
    all_arenas = 5
    win_status = None
    def game_continue(self):
        if self.arena_counter < 5:
            return True
        else:
            return False

    def calculate_reward(self):
        reward = self.base_reward
        for arena_num in range(self.arena_counter):
            reward *= 1.5
        return reward

    def play(self):
        self.arena_counter = 0
        #Познайомитись
        print(Texts_module.welcome_game_board())


        self.player_name = input(Texts_module.get_player_name())

        print(Texts_module.welcome_hero_name(self.player_name, self.all_arenas, self.player_gold))
        #Сформувати базову команду

        self.player_team = Team_module.Team_class()
        self.player_team.create_start_team_for_player(self.player_name)
        print(Texts_module.wow_you_have_a_squad(self.player_team.alive_team))

        #Основний цикл гри
        while self.game_continue():
            # Магазин Змусити докупити 5го героя
            #Створити арену, помістити туди команду гравця
            arena = ArenaClass(self.player_team, self.arena_counter)
            arena.create_comp_team()
            arena.display_arena_board()

            arena.arena_fight()
            arena.display_arena_results()
            #По закінченню арени провести аналіз
            arena_results = arena.arena_results()
            self.player_team.alive_team = arena_results[0]
            self.player_team.dead_team.append(arena_results[1])

            #rewards а закінчення арени
            if len(self.player_team.alive_team) > 0:
                arena_reward = self.calculate_reward()
                self.player_gold += self.calculate_reward()
                print(Texts_module.arena_final_positive(arena_reward, self.arena_counter, self.player_gold))
                input()
                self.arena_counter += 1
            elif self.game_continue():
                print(Texts_module.arena_final_negative())
                input()
            else:
                self.win_status = False
                break
            #Запросити в магазин
        if self.win_status == True:
            print(Texts_module.arena_winner(self.all_arenas))
        else:
            print(Texts_module.arena_looser())

        #спитати чи хочеш ще раз зіграть
        u_inp = None
        while u_inp not in ["y", "n"]:
            u_inp = input("Do you wanna play one more time (Y/N)? --> ").lower()
            if u_inp == "y":
                self.play()
            elif u_inp == "n":
                break

        #Аналіз закінчення гри
game = Game_class()
game.play()
