import random

def zadacha1():
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
def zadacha2():
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
        print("Список:", chisla, "В списке нет повторяющихся элементов")

def zadacha53():
    week =('Понедельник', 'Вторник','Среда','Четверг','Пятница','Суббота','Воскресенье')
    chislo_weekends = int(input("Сколько выходных дней на неделе вы хотите:"))

    weekends = []
    workday = []

    for x in range(1,chislo_weekends + 1): #отсчет с конца недели
        weekends.append(week[-x])

    for y in week:
        if y not in weekends:
            workday.append(y)
    print("Ваши выходные дни:", weekends)

    print("Ваши рабочие дни:", workday)

def zadacha54():

    group1 =['Петров','Яковлев', 'Кукушкина', 'Гаврилова', 'Киселёва']
    group2 = ['Баранов','Иванов','Егоров','Кузьмин','Виноградов']
    sportcommanda = tuple(group1[:2] + group2[:3])

    print("Список группы 1:", group1)
    print("Список группы 2:", group2)
    print("Спортивная команда:", sportcommanda)

    print("Длина кортежа:", len(sportcommanda))

    sorted_sportcommanda = sorted(sportcommanda)
    print("Спортивная команда по алфавиту:" , sorted_sportcommanda)

    namecheck = 'Иванов'
    if namecheck in sportcommanda:
        count = sportcommanda.count(namecheck)
        print("Студент Иванов входит в спортивную команду")
    else:
        print("Студент Иванов не входит в спортивную команду")


