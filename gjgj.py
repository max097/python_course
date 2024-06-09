def foo(a):
    if type(a) != list:
        print("Введи масив ")
    mas = []
    for i in lst:
        if type(i) == int:
            mas.append(i)



    return mas






lst = [1, 2, "text", 3, 4, True, "text2", None, "text3"]
lst2 = foo(lst)
print(lst2)



print("-"* 20)




def foo1(a, b):
    mas =[]
    for i in a:
        if i in b:
            mas.append(i)
    return mas
def foo2(a, b):
    mas = set()
    for i in a:
        if not i in b:
            mas.add(i)
    return list(mas)




x = [1, 0, 9, 8, 5, 6, 3, 8, 5, 7]
y = [9, 8, 3, 5, 7, 9, 3 , 4, 4, 5, 0, 2, 0, 3, 8, 7, 5]
task1 = foo1(x, y)
task2 = foo2(x, y)
task3 = foo2(y, x)
print(f"Однакові числа = {task1}")
print(f"Унікальні  числа для 1 списка = {task2}")
print(f"Унікальні  числа для 2 списка = {task3}")










print("-"* 20)


