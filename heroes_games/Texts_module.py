import UNIT_CLASSES
def welcome_game_board():
    return '''
___________________________________________________________________________________________________

                    ********   GAME OF HEROES   ********
                     -- The game by Maksym Chornobuk --
___________________________________________________________________________________________________
'''

def get_player_name():
    return "Hello, Hero! What is your name? ---> "

def welcome_hero_name(player_name, all_arenas, player_gold):
    return f'''
    Welcome, my young hero {player_name}!
    Here is some money({player_gold}), you need to create your own squad and fight in {all_arenas} arenas
    Let's play the Game!
'''

def wow_you_have_a_squad(player_team):
    text = f"Wow! You have a squad from {len(player_team)} heroes!"
    for i in player_team:
        text += "\n"+ i.unit_info()
    return text

def arena_final_positive(arena_reward, arena_counter, player_gold):
    return f'''\n\n
                You get {arena_reward}gold for successful battle in Arena {arena_counter}
                Now you have {player_gold} gold!
                Are you ready to prepare for the next Arena? 
                Let's go shopping to buy new units and items
                \n\n
                Press ENTER to continue --> 
                '''

def arena_final_negative():
    return '''
    You loose in this arena. You should buy new squad.
                
        Are you ready to prepare for this Arena one more time?
        let's go shopping to buy new units and items!
                
    Press ENTER to continue -->
    '''


def arena_winner(all_arenas):
    return f'''
            --------------------------------------------------------------
            
                            ********  GAME OVER  ********
                                  You win the Game
                                  
            --------------------------------------------------------------
                            You have won in all {all_arenas} Arenas
            '''

def arena_looser():
    return '''
            --------------------------------------------------------------

                            ********  GAME OVER  ********
                                 You loose the Game
                                 
            --------------------------------------------------------------
                            You have no money to buy full squad
            '''

def display_arena_board(player_team, comp_team, counter_arena):
    return f'''
            --------------------------------------------------------------
                        ******** ARENA #{counter_arena} BOARD ********
            --------------------------------------------------------------
                                Welcome to the Arena
            {player_team.name}              VS              {comp_team.name}
    
    
    '''


def display_arena_results(counter_arena):
    return f'''
            --------------------------------------------------------------
                        ******** ARENA #{counter_arena} BOARD ********
            --------------------------------------------------------------
    '''

def choose_unit_for_fight(fight_counter):
    return f'''
            -------------------------------
            CHOOSE UNITS FOR FIGHT #{fight_counter}!
            '''

def display_fight_board(attacker, defender, fight_counter):
    return f'''
            -------------------------------
            ******** FIGHT #{fight_counter} BOARD ********
            -------------------------------
            Attacker   VS      Defender
            {attacker.name}                  {defender.name}
            
            
            Attacker - {attacker.unit_info()}
            Defender - {defender.unit_info()}
            
            LET'S THE FIGHT BEGIN
            '''

def display_fight_result_board(attacker, defender):
        return f'''
                
                {attacker.name} status - {attacker.life_status}, health:{attacker.health_in_arena}
                {defender.name} status - {defender.life_status}, health:{defender.health_in_arena}

                ---------------------------------
                '''