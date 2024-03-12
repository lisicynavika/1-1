number = int(input("Введите номер места от 0 до 54(вкл):  "))

if number % 2 == 0 and number in range(0,36):
    print("верхнее место")
elif number % 2 != 0 and number in range(0,36):
    print("нижнее место")
elif number % 2 == 0 and number in range(37,54):
    print("верхнее боковое место ")
elif number % 2 != 0 and number in range(37,54):
    print("нижнее боковое место")