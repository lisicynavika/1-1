answer = 0
mistakes = 0

while mistakes < 3:
    import random
    chislo1 = random.randint(0, 9)
    chislo2 = random.randint(0, 9)
    print(chislo1, chislo2)
    result = int(chislo1) + int(chislo2)
    summ = input("Введите сумму данных чисел:" )
    if int(summ) == int(result):
        print("Правильно!")
        answer += 1
    else:
        print("Ответ неверный")
        mistakes += 1
print("Игра окончена. Правильных ответов:",answer)

