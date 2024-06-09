


class FirstClass():
    pass


first = FirstClass()
second = FirstClass()

print(type(first))
print(type(second))

print("-"*25)

#Параметри класа

class TestClass():
    var_x = 100


object1 = TestClass()
object2 = TestClass()

print(object1.var_x)
print(object2.var_x)


print("-"*25)
# Методи\Фунції в клас

class Test():
    var_x = 100
    var_y = 200

    def print_me(self):
        print("Hello")

    def calc_x(self, z = 1, t = 20):
        return self.var_x**2 + z*t

test1 = Test()

print(test1.var_x)
print(test1.var_y)
test1.print_me()
print(test1.calc_x(5, 8 ))
print(test1.calc_x())

print("-"*25)

class Hello():
    name = "Bob"
    age = 75

    def say_hello(self):
        print(f"Hello, my name is {self.name}, I'm {self.age} years old")

person = Hello()
person.say_hello()

person2 = Hello()
person2.name = "Adolf"
person2.age = 2
person2.say_hello()

print('-'*25)

# Спадковість

class Car():
    wheels = 4
    name = "car"

    def hello_car(self):
        print(f"Hello, my name is {self.name}, I have {self.wheels} wheels")

car = Car()
car.hello_car()

# class CarSedan():
#     wheels = 4
#     name = "car"
#     color = "red"
#
#     def hello_car(self):
#         print(f"Hello, my name is {self.name}, I have {self.wheels} wheels")
#
#     def hello_color(self):
#         print(f"My color is {self.color}")
#
# sedan = CarSedan()
# sedan.hello_car()
# sedan.hello_color()

class CarSedan(Car):
    color = "Red"
    name = "sedan"

    def hello_color(self):
        print(f"My color is {self.color}")

sedan = CarSedan()
sedan.hello_car()
sedan.hello_color()

print('-'*25)

# Магічний метод __init__

class Car():
    name = None
    wheels = None
    color = None

    def __init__(self, init_name = "car", init_wheels = 4, init_color = "black"):
        self.name = init_name
        self.wheels = init_wheels
        self.color = init_color

    def hello_car(self):
        print(f"Hello, my name is {self.name}, I have {self.wheels} wheels")

    def hello_color(self):
            print(f"My color is {self.color}")

car = Car("sedan", 4, "blue")
# car.name = 'sedan'
# car.wheels = 4
# car.color = "red"
car.hello_car()
car.hello_color()

car2 = Car()
car2.hello_car()
car2.hello_color()
bus = Car("bus", 8, "yellow")
bus.hello_car()
bus.hello_color()

print('-'*25)

print((dir(bus)))

print('-'*25)
# ІНКАПСУЛЯЦІЯ

class InkapClass():
    varX = 100 # public
    _varY = 200 # private
    __varZ = 500 # protected



test_obj = InkapClass()
print(test_obj.varX)
print(test_obj._varY)


test_obj.varX = 400
print(test_obj.varX)

print('-'*25)

class Car():
    fuel = None
    __l_100km = 8
    distance = None

    def __init__(self, init_fuel):
        self.fuel = init_fuel
        self.distance = self.__distance()
    def __distance(self):
        dist = (self.fuel / self.__l_100km) *100
        return dist

car = Car(100)
print(car.fuel)
print(car.distance)

# print(car.__l_100km)