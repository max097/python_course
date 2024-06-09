
def foo(x = 1, y = 5, z = 6):
    print(x*y*z)
foo()
#позиційні аргументи і їх передача

def foo(x = 1, y = 1, z = 1):
    print(x)
    print(y)
    print(z)
foo()
foo(x = 5, z = 6)
foo(z=6)

def foo(money = 0, cost = 0, currency = "$"):
    print(f"Було {money}{currency}, витратили {cost}{currency}, решта {money - cost}{currency}")
foo(100, 30)
foo(1000, currency="uah")

def foo(x, y, z, *args):
    print(x)
    print(y)
    print(z)
    print(args)


    for x in args:
        print(x)
foo(1,2,4,56,7,5,7,9,7,4,44)





def foo(*args):
    print(args)

foo(10, 12, 6, 10)


def foo(**kwargs):
    print(kwargs)
foo(Anya = 10, Khrystyna = 11)


def foo(x=0, y=1, *args, **kwargs):
    print(x, y, args, kwargs )
foo(54, 84, 483,343,43, a = 234, b =434)
