import random
WORDLIST = 'акула імбир лимон мандарин помідор огірок огорожа мальдіви город місто колір череп черепуха чобіт диня дах дира гора нектар вулкан пил верблюд жаба риба бабуїн макака літак пілот машина апельсин дім пес дід ром ліра автомобіль зоря пістолет автомат'.split(" ")
ALPHABET = 'АаБбВвГгҐґДдЕеЄєЖжЗзИиІіЇїЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщьЮюЯя'



def get_pics():
    a = r'''
    +---+
    |   
    |  
    | 
    ==='''
    b = r'''
    +---+
    |   0
    |  
    |  
    ==='''
    c = r'''
    +---+
    |   0
    |   |
    |  
    ==='''
    d = r'''
    +---+
    |   0
    |  /|
    |  
    ==='''
    e = r'''
    +---+
    |   0
    |  /|\
    |  
    ==='''
    f = r'''
    +---+
    |   0
    |  /|\
    |  / 
    ==='''
    g = r'''
    +---+
    |   0
    |  /|\
    |  / \
    ==='''
    lst = [a, b, c, d, e, f, g]
    return lst

def tablo(pic, mis, cor, word):
    print(pic[len(mis)])
    print("Помилкові літери - ", mis)
    print("Правильні літери - ", end= " ")
    for letter in word:
        if letter in cor:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print()
def user_input(mis, cor, alf):
    while True:
        u_inp = input("Введи букву укр. абетки - ")
        if len(u_inp) == 0:
            print("Ви нічого не ввели")
            continue
        elif len(u_inp) > 1:
            print("Введіть одну букву")
            continue
        elif u_inp not in alf:
            print("Введіть БУКВУ")
            continue
        elif u_inp in cor or u_inp in mis:
            print("Ви таку літеру вже називали")
            continue
        else:
            return u_inp

def analisys(guess,word, cor_l, mis_l, pic):
    game_continue = True
    winner = None
    #якощо гравець вгадав
    if guess in word:
        cor_l += guess
        #uhfdtwm duflfd dcs ksnthb?
        for letter in word:
            if letter not in cor_l:
                return cor_l, mis_l, game_continue, winner
        game_continue = False
        winner = "player"
        return cor_l, mis_l, game_continue,winner
    #якщо гравець не вгадав
    else:
        mis_l += guess
        #чи скінчились спрббоби?
        if len(mis_l) != len(pic):
            return cor_l, mis_l, game_continue,winner
        else:
            game_continue = False
            winner = "computer"
            return cor_l, mis_l, game_continue,winner
def checkAnotherGame():
    while True:
        print("Чи хочете ви зіграти ще раз?(Т/Н) ")
        u_inp = input().lower()
        if u_inp.startswith("т"):
            return True
        if u_inp.startswith("н"):
            return False
        else:
            print("Ви ввели якусь фігню")


def game(wlist, albt):
    correct_letters = ''
    missed_letters = ''
    pictires = get_pics()
    game_continue = True
    winner = None
    word = random.choice(wlist)
    while True:
        tablo(pictires, missed_letters,correct_letters,word)
        guess = user_input(missed_letters, correct_letters, albt)
        correct_letters, missed_letters,game_continue, winner =  analisys(guess, word, correct_letters, missed_letters, pictires)

        if game_continue == True:
            continue
        else:
            if winner == "player":
                print(f"Ви вгадали слово {word}!")
            else:
                print(f"У вас закінчились спроби!!!Ви не вгадали слово {word}!")
        if checkAnotherGame():
            game(wlist, albt)
        else:
            break







print("Шибениця")
game(WORDLIST, ALPHABET)
print("Дякуємо за гру")