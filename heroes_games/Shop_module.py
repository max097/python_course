import sqlite3
import Team_module
import UNIT_CLASSES
class Shop():
    def __init__(self, init_gold = 0, init_player_team = None):
        self.gold = init_gold
        self.player_team = init_player_team

        self.gold = 100
        self.player_team = Team_module.Team_class()
        self.player_team.create_start_team_for_player("IVAN")

    def display_variants_and_ask_answer(self, data):
        for x in range(len(data)):
            print(f"    {x}. {data[x][0]}")
        print(f"    {len(data)}. Show your team with all unit's items to analise")
        print(f"    {len(data) +1}. Return to previous stage.")

        while True:
            answer = input("Input the number here ---> ")
            try:
                answer = int(answer)
            except:
                continue

            if answer < 0 or answer > len(data) + 1:
                continue

            if answer == len(data):
                self.player_team.display_team_info_for_shop()
                continue

            return answer
    def get_data_from_db(self, text):
        db = sqlite3.connect("Db_shop.db")
        cursor = db.cursor()
        cursor.execute(text)
        data = cursor.fetchall()
        db.close()

        return data
    def unit_shop(self):
        print(f'''
            -----------------------------
                    BUY UNITS
            -----------------------------
            Gold = {self.gold}''')
        data = self.get_data_from_db("SELECT unit_name, unit_price FROM units")
        answer = self.display_variants_and_ask_answer(data)

        if answer == len(data) +1:
            self.item_categories()
        chose_name = data[answer][0]
        choice_price = data[answer][1]
        if choice_price > self.gold:
            print("You  have not enough money")
            self.item_categories()
            return

        list = [UNIT_CLASSES.Healer_class(),
                UNIT_CLASSES.Shaman_class(),
                UNIT_CLASSES.Wizard_class(),
                UNIT_CLASSES.Archer_class(),
                UNIT_CLASSES.Barbarian_class(),
                UNIT_CLASSES.Knight_class()]
        for unit in list:
            if unit.name == chose_name:
                self.player_team.alive_team.append(unit)
                print(f" You succesfully bought {unit.name} for {choice_price} gold")
                self.gold -= choice_price
                break
        self.main()

    def armor_shop(self):
        pass

    def weapon_shop(self):
        pass

    def ability_shop(self):
        pass

    def item_categories(self):
        print(f''''
            ----------------
            ITEM CATEGORIES
            ----------------
            Gold = {self.gold}''')
        data = self.get_data_from_db("SELECT item_type_name FROM item_types")
        answer = self.display_variants_and_ask_answer(data)

        if answer == len(data) +1:
            self.main()
        elif data[answer][0] == "unit":
            if len(self.player_team.alive_team) < 5:
                self.unit_shop()
            else:
                print("Your team is full")
                self.item_categories()
        elif data[answer][0] == "armor":
            self.armor_shop()
        elif data[answer][0] == "weapon":
            self.weapon_shop()
        elif data[answer][0] == "ability":
            self.ability_shop()







    def main(self):
        print(f'''
        ----------------------------------------------
                WELCOME TO THE GAME SHOP
        ----------------------------------------------
        Gold = {self.gold}
    Please, choose, what would you like to do in the shop:
        0. See all item categories to buy.
        1. See your team with all unit's items to analise
        2. Exit from the shop.''')

        answer = ""
        while answer not in ["0", "1", "2"]:
            answer = input("Input the number here ---> ")

        if answer == "2":
            print("\nSee you next time bye-bye!")
        elif answer == "1":
            self.player_team.display_team_info_for_shop()
            self.main()
        elif answer == "0":
            self.item_categories()

shop = Shop()
shop.main()