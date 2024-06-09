def foo():
    print("Hello world")


foo()


#2 tyoes of function
# def foo():
#     a = 5
#     b = 7
#     x = a+b
#     print(x)
# foo()
# def foo(a,b):
#     x = int(a) + int(b)
#     print(x)
#
# x = input("Write ")
# y = input(" Write ")
# foo(x, y)


# print("-"* 100)
#
# def foo(a,b):
#     f = int(a) + int(b)
#     return f
# x = input("Write x ")
# y = input("Write y ")
#
# z = foo(x,y)
# print(z)
#
#
#
# print("-"* 100)
#
#
#
#
# def foo(x):
#     return x**2
# print(foo(5))
#
#
#
# print("-"* 100)
#
#
# def foo(x):
#     return x ** 2
# def foo2(t):
#     return t*2
# print(foo(foo2(4)))
#
# print("-"* 100)
#
# def foo():
#     print()
# print(foo())
#
#
#
#
# print("-"* 100)




def foo(a, b, c):
    f = b * c
    j = a + b
    return f, j
x, y = foo(4, 5, 6)
print(x + y)


print("-"* 100)

lst = "Hello"
def foo(x):
    for i in x:
        print(i)
    return "Merry Christmas"

lst = "Hello"
print(foo(lst))


print("-"* 100)




def foo():
    return a * 2
a = 5
print(foo())


print("-"* 100)

def foo(lst):
    mas3 = []
    for i in mas:
        if type(i) != str:
            mas3.append(i)



    return mas3
mas = [1, "nex 1", 3, 4, "nex 2", 6, "nex 3", "nex 4", 9, 10]
mas2 = foo(mas)
print(mas2)
def foo(lst):
    if type(lst) != list:
        return "Ty Baran"
    mas3 = []
    for i in mas:
        if type(i) == str:
            mas3.append(i)



    return mas3
mas = [1, 'd', 3, '5']
mas2 = foo(mas)
print(mas2)



print('-'* 25)




def si(x):
    if x == 0:
        return 0
    elif x > 0:
        return 1
    else:
        return -1
user_inp = int(input("Введи дані для функції si(x) - "))
res = si(user_inp)
print(res)


print('-'* 25)



def user_input():
    while True:
        ui = input("Введіть кількість учнів в класі ")
        try:
            ui = int(ui)
        except:
            print("Введи ціле число блян")
            continue
        return ui

def desks_in_class(st):
    if st % 2 == 0:
        p = st // 2
    else:
        p = st // 2 + 1
    return p
all_students = []
all_desks = []
for i in range(3):
    students = user_input()
    desks = desks_in_class(students)
    all_students.append(students)
    all_desks.append(desks)

total_st = sum(all_students)
total_dsk = sum(all_desks)
print(f"Для {total_st} стундентів треба купити {total_dsk} парт")














