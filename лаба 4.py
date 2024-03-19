def zadacha1():
    chislo = int(input("Введите число: "))

    if chislo % 3 == 0:
        print("Число", chislo ,"делится на три ")
    else:
        print("Число", chislo ,"не делится на три")

def zadacha2():
    try:
        chislo = input("Введите число:")
        chislo1 = int(chislo)

        if 100 % chislo1 == 0:
            print(100 // chislo1)
        else:
            print("100 не делится на", chislo1)

    except ValueError:
        print("Ошибка: Вы ввели не число")

    except ZeroDivisionError:
        print("Ошибка: На ноль делить нельзя")


def zadacha3():
    data = input("Введите дату в формате ДД.ММ.ГГГГ:")
    day = int(data[:2])
    month = int(data[3:5])
    year = int(data[7:])

    if day * month == year:
        print("True")
    else:
        print("False")

def zadacha4():
    ticket = input("Введите номер билета: ")
    summ1 = 0
    summ2 = 0
    if len(ticket) % 2 == 0:
        polticket = len(ticket) // 2
        pol1 = ticket[:polticket]
        pol2 = ticket[polticket:]

        for i in range(len(pol1)):
            summ1 += int(pol1[i])
        for i in range(len(pol2)):
            summ2 += int(pol2[i])

        if summ1 == summ2:
            print("Билет", ticket ,"счастливый")
        else:
            print("Билет", ticket ,"несчастливый")
    else:
        print("Билет должен состоять из четного количества элементов")
zadacha4()


