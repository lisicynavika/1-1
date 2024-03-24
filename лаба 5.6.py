import random

def zadacha51():
    from random import randint
chisla = []
for x in range(5):
    chisla.append(random.randint(1, 25))

user_chislo = int(input("Введите число:"))

if user_chislo in chisla:
    print("Список чисел:", chisla, "Поздравляю, Вы угадали число!")
else:
    print("Список чисел:", chisla, "Нет такого числа!")



import random
def zadacha52():
    from random import randint
chisla = []
for x in range(7):
    chisla.append(random.randint(1, 4))

again = []

for x in chisla:
    if chisla.count(x) > 1 and x not in again:
        again.append(x)
if len(again) > 0:
    print("Список:", chisla, "Повторяющиеся элементы списка:", again)
else:
    print( "Список:", chisla,"В списке нет повторяющихся элементов")
zadacha52()