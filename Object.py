class Car():
    fuel = property()

    def __init__(self, init_fuel = 0):
        self.__fuel = init_fuel

    @fuel.getter
    def fuel(self):
        return self.__fuel

    @fuel.setter
    def fuel(self, value):
        self.__fuel = value



car = Car(30)
car.fuel = 20
print(car.fuel)

print("-"*20)


class Party():

    def __init__(self, init_user):
        self.user = init_user

    def decor_party(func_to_decor):
        def wrapper(*args, **kwargs):
            print("Ми закупили їжу та напої,а також замовили діджея")
            res = func_to_decor(*args, **kwargs)
            print("Треба забрати їжу та напої, викунити сміття, заплатити діджею")

        return wrapper

    @decor_party
    def party(self):
        print(f"Нашу тусу приймає в себе дома {self.user}")

    @decor_party
    def no_party(self):
        print(f"У {self.user} повернулись батьки, туса відміняється!")


user_name = input("Hапиши до кого йдемо на тусу - ")
user_party = Party(user_name)
u_input = input(f"Напиши Так/Ні чи буде туса у {user_party.user}? - ")

if u_input.lower()[0] == "т":
    user_party.party()
else:
    user_party.no_party()




print("-"*20)



import time
import random
class Car():
    __slots= "__speed", "speed", "__max_speed"
    speed = property()

    __maks_speed = 200

    def __init__(self, init_speed = 0):
        self.__speed = init_speed

    @speed.getter
    def speed(self):
        if self.__speed < 100:
            print("піддай газку")
        return self.__speed

    @speed.setter
    def speed(self, value):
        if value > self.__maks_speed:
            print("скинь швидкість")
        self.__speed = value

    def time_it(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            time.sleep(random.randint(1, 10))
            end_time = time.time()
            print(f"Ride time {end_time - start_time} seconds")
            return result
        return wrapper

    @time_it
    def drive(self):
        print("drive")

car1 = Car(60)
print(car1.speed)
car1.speed = 280
print(car1.speed)
car1.drive()














class Person():

    def __init__(self, init_name):
        self.name = init_name

    # def __repr__(self):
    #     return f"Hello, my name is {self.name}"

    def __str__(self):
        return "i'm trying to be converted to string"

p1 = Person("YEVGEN")
print(p1.name)

print(p1)




























