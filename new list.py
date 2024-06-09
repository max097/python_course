#tuple - кортеж
tpl = ()
tpl = tuple()
print(type(tpl))
print(type([]))
tpl = (1, 3.45, "Hello", [1, 2, 3], True, None)
print(tpl)


print("-"*25)


tpl = (1, 3.45, "Hello", [1, 2, 3], True, None)
lst = [1, 3.45, "Hello", [1, 2, 3], True, None]
lst[0] = "change"
print(lst)

# tpl[0] = "change"
# print(tpl)

tpl[3][0] = "change"
print(tpl)




for x in tpl:
    print(x)
print("-" * 25)









tpl += ("one", 2, "three")
print(tpl)


print("-"*100)





#set -куча
st = {}
st = set()


st = {1, 3.45, 'Hello', ('change', 2, 3), True, None,}
print(st)





st = {1,1,2,2,3,3,}
print(st)


for i in st:
    print(i)


print(1 in st)






st.add("Dodano")
print(st)
st.remove(1)
print(st)






#frozeSet
fst = frozenset()

print("-"*100)
#dictionary
dct = {}
dct = dict()

lst = ["value 1", "value 2", "value 3"]
dct = {
    "key 1": "value 1",
    "key 2": "value 2",
    "key 3": "value 3"
}

print(lst[0])
print(dct["key 1"])
print("-"*100)

dct = {
    1 : "one",
    2.3 : "float",
    "text" : 123,
    True : "sdf",
    None : "float"
}


print("-"*100)

water = ["~","~","~","~","~","~","~","~","~","~",]
field = {
    "A": water,
    "B": water,
    "C": water
}
print(field)
print("-"*100)
field["B"][1] = "X"
print(field)




print("-"*100)

dct = {
    1: "one",
    2.3: "float",
    "text": 123,
    True: "sdf",
    None: "float"
}

print(dct.keys())
print(dct.values())


print("text" in dct.keys())
print("text" in dct.values())
for i in dct.keys():
    print(i)
print("-"*1000)
for i in dct.values():
    print(i)

for x in dct.keys():
    print(f"{x} - {dct[x]}")




print("-"*100)
print(dct.items())
for x in dct.items():
    print(f"{x[0]} - {x[1]}")



print("-"*100)




dct ={}
dct['first key'] = 123
dct['second key'] = 10
print(dct)
dct['first key'] = 1
print(dct)

if not 'first key' in dct.keys():
    dct['first key'] = 1
else:
    dct["some key"] = 1
print(dct)


print("-"*100)

dct = {
    1: "one",
    2.3: "float",
    "text": 123,
    True: "sdf",
    None: "float"
}
print(dct.get("text"))

if dct.get("dfgd"):
    print("Yes")
else:
    print("NO")

print("-"*100)


dct = {
    1: "one",
    2.3: "float",
    "text": 123,
    True: "sdf",
    None: "float"
}

print(dct)
dct.pop("text")
print(dct)


print("-"*100)

dct = {
    1: "one",
    2.3: "float",
    "text": 123,
    True: "sdf",
    None: "float"
}

dct.setdefault("num", "fghf")
print(dct)






print("-"*100)


calendar = {
    "January": 31,
    "February": 28,
    "March": 31,
    "April":30,
    "May": 31,
    "June":30,
    "July":31

}
for x in calendar.items():
    print(f"{x[0]} - {x[1]}")
print("-"*100)

students ={
    "Alice": (85, 90,92),
    "Bob": (78, 85, 88,64),
    "Charlie":(90,95)
}
for  st in students.keys():
    ln = len(students[st])
    sum = 0
    for mark in students[st]:
        sum += mark
    av = sum/ln
    print(f"{st} -{av}")



print("-"*100)
orders = {
    'apple': (1,10),
    'banana': (2, 20),
    "orange":(3,15)
}
total = 0
for key in orders:
    sum = orders[key][0] * orders[key][1]
    total += sum
    print(f"{key} = {sum}")
print(f'Total = {total}')
print("-"*100)



letters = "ABCDEFGHIK"
sea = "~"
field = {}
field["A"] = []
print(field)

field["A"].append(sea)
print(field)

for letter in letters:
    field[letter] = []
    for x in range(10):
        field[letter].append(sea)

