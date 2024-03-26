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

def zadacha61():
    dictionary = {"Россия":"Москва", "Китай":"Пекин", "Турция":"Анкара", "Германия":"Берлин","Италия":"Рим"}
    print(dictionary)

    print(dictionary["Италия"])

    list_keys = list(dictionary.keys())
    list.keys.sort()
    for i in list_keys:
        print(i,':',dictionary[i])

def zadacha62():
    alfavit = {}
    alfavit = dict.fromkeys(['А','В','Е','И','Н','О','Р','С','Т'], 1)
    alfavit.update(dict.fromkeys(['Д', 'К', 'Л', 'М', 'П', 'У'], 2))
    alfavit.update(dict.fromkeys(['Б','Г','Ё','Ь','Я'], 3))
    alfavit.update(dict.fromkeys(['Й','Ы'], 4))
    alfavit.update(dict.fromkeys(['Ж','З','Х','Ц','Ч'], 5))
    alfavit.update(dict.fromkeys(['Ш','Э','Ю'], 8))
    alfavit.update(dict.fromkeys(['Ф','Щ','Ъ'], 10))
    print(alfavit)

    word = input("Введите слово: ").upper() #принимает любой регистр
    ball = sum(alfavit.get(key) for key in word)
    print("Слово",word,"стоит", ball, "баллов")

def zadacha63():

    ivanov = {'Английский','Японский'}
    sverdlov = {'Китайский','Английский','Финский'}
    kuznecov = {'Английский','Немецкий','Китайский'}
    baranov = {'Китайский'}
    kamnev = {'Английский','Немецкий'}

    A = ivanov.union(sverdlov)
    B = A.union(kuznecov)
    C = B.union(baranov)
    D = C.union(kamnev)
    sorted_D = sorted(D)
    print(sorted_D)

    a = set()
    if 'Китайский' in ivanov:
        a.add('ivanov')
    if 'Китайский' in sverdlov:
        a.add('sverdlov')
    if 'Китайский' in kuznecov:
        a.add('kuznecov')
    if 'Китайский' in baranov:
        a.add('baranov')
    if 'Китайский' in kamnev:
        a.add('kamnev')
    a_sorted = sorted(a)
    print("Студенты, изучающие китайский:",a_sorted)
