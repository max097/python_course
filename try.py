# while True:
#     x = input("Print number ")
#     try:
#         y = 1/int(x)
#     except ZeroDivisionError:
#         print("Фігня")
#         continue
#     except ValueError:
#         print("NONONO")
#         continue
#     else:
#         print(y)
#     break
#
#     finally:
#         print("Finish part")
# import random
# MACTI = ["Пік", "Хреста", "Чирва", "Бубна"""]
# ZNACHENYA = ["Туз", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Валет", "Дама", "Король"]
# KOLODA = []
# score = 0
# KOLODA = list()
# value = 0
# for z in ZNACHENYA:
#     value += 1
#     for m in MACTI:
#         card = [z + " " + m, value]
#         KOLODA.append(card)
#         print(card)
# random.shuffle(KOLODA)
# card1 = KOLODA.pop(0)
# while True:
#     print("-" * 25)
#     print('\nВаші бали = ', score)
#     print('Поточна карта', card1[0])
#     while True:
#         user_input = input("Вгадай наступну карту. (Б)ільше або (М)енше ").lower()
#         if len(user_input) == 0 or user_input[0] not in "бм":
#             print("ІДІОТ, ВВЕДИ БУКВИ Б АБО М")
#             continue
#         guess = user_input[0]
#         break
#     card2 = KOLODA.pop(0)
#     print("Наступна карта -", card2[0])
#     if card1[1] == card2[1]:
#         print("ОДНАКОВО!")
#     elif (card1[1] > card2[1] and guess == "м") or \
#          (card1[1] < card2[1] and guess == "б"):
#         print("Вірно!")
#         score += 1
#     else:
#         print("Не вірно")
#         break
#     card1 = card2
# print()
# print("-" * 25)
# print("\nGAME OVER!")
# print("ФІНАЛЬНИЙ РАХУНОК:", sco





