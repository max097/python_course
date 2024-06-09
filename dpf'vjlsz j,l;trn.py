class Point():

    x = property()
    y = property()

    def __init__(self, init_x = 0, init_y = 0):
        self.__x = init_x
        self.__y = init_y

    @x.getter
    def x(self):
        return self.__x

    @y.getter
    def y(self):
        return self.__y

    def __str__(self):
        return f"Point: x = {self.__x}, y = {self.__y}"






class Line():
    lenght = property()

    def __init__(self, init_p1, init_p2):
        self.__p1 = init_p1
        self.__p2 = init_p2

    @lenght.getter
    def lenght(self):
        x = self.__p2.x - self.__p1.x
        y = self.__p2.y - self.__p1.y
        z = (x**2 + y**2) ** 0.5
        return round(z,1)

    def __str__(self):
        return f"Line with points ({self.__p1.x},{self.__p1.y})({self.__p2.x},{self.__p2.y}), lenght = {self.lenght}"

p1 = Point(3, 5)
p2 = Point(1,1)


line = Line(p1, p2)
print(line)



class Triangle():
    area = property()

    def check_double(self):
        if (self.__p1.x == self.__p2.x and self.__p1.y == self.__p2.y) or \
                (self.__p1.x == self.__p2.x and self.__p1.y == self.__p2.y) or \
                (self.__p1.x == self.__p2.x and self.__p1.y == self.__p2.y):
            return True
        else:
            return False


    def __init__(self, init_p1, init_p2, init_p3):
        self.__p1 = init_p1
        self.__p2 = init_p2
        self.__p3 = init_p3

    @area.getter
    def area(self):


        ar = 0.5 * ((self.__p1.x * self.__p2.y + self.__p2.x * self.__p3.y + self.__p3.x * self.__p1.y)\
                    - (self.__p1.y * self.__p2.x + self.__p2.y * self.__p3.x + self.__p3.y * self.__p1.x))
        return abs(round(ar,1))

    def __str__(self):
        if self.check_double():
            return("НЕ ВВОДЬ ОДНАКОВЕ")

        return f'''Triangle with points: 
        A({self.__p1.x},{self.__p1.y}); 
        B({self.__p2.x},{self.__p2.y}); 
        C({self.__p3.x},{self.__p3.y});
        TRIANGLE AREA  = {self.area}'''

p1 = Point(1, 1)
p2 = Point(1,1)
p3 = Point(7,9)

print(p1)
print(p2)
print(p3)

tr = Triangle(p1, p2, p3)
print(tr)


print("-" * 25)

class Unit():
    name = property()
    defence = property()
    health = property()
    attack = property()

    def __init__(self, init_name = "bob", init_defence = 100, init_health = 100, init_attack = 5):
        self.__name = init_name
        self.__defence = init_defence
        self.__health = init_health
        self.__attack = init_attack

    @name.getter
    def name(self):
        return self.__name


    @defence.getter
    def defence(self):
        return self.__defence

    @health.getter
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        self.__health = value

    @attack.getter
    def attack(self, value):
        self.__attack = value

    def hit(self, enemy):
        enemy.health = enemy.health - (self.__attack - enemy.defence)
        print(f'''
HERO: {self.__name} hits {enemy.name} by {self.__attack - enemy.defence}''')

    def __str__(self):
        return f'''HERO: {self.__name}
ЗДОРОВЯ: {self.__health}
ЗАХИСТ: {self.__defence}
АТАКА: {self.__attack}
                    '''

player = Unit("Ілля", 2, 105,15 )
player2 = Unit("Konor, McGregor", 20, 200,100)


print(player)
print(player2)



while player2.health > 0 and player.health > 0:
    player2.hit(player)
    player.hit(player2)

if player2.health > 0:
    print(f"{player2.name} win")
else:
    print(f"{player.name} win")