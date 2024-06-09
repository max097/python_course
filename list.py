# text = "This holiday will be the best"
# text = text.split()
# res = ""
# for i in text:
#     res = i + " " + res
#
# print(res)

text = "I should run from house"
text = text.split("h")
print(text[0] + " " + text[len(text) - 1])
text = "I should run from this hooroble house "
text = text.split("h")
print(text[0] + " " + text[len(text) - 1])
print('-----------------------------')
text = "I should run from this hooroble house I should run from this hooroble house  "
index_start = 0
index_finish = 0
counter = 0
for index in range(len(text)):
    if text[index] == "h":
        counter += 1
    if counter == 3:
        index_start = index + 2
    if counter == 5:
        index_finish = index



res = text[index_start: index_finish]
print(res)
while True:
    num = input("Введіть трьохзначне число - ")
    if not num.isdigit() or len(num) != 3:
        continue
    break
word = num
sum = 0
for i in word:
    sum += int(i)
print(sum)




print('-----------------------------')

while True:
    x = input("print Number ")
    if not x.isdigit():
        continue
    break

y = 1/int(x)
print y


































































#import random
#score = print("Твій рахунок:")




































