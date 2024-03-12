stroka = ""

N = int(input("Введите количество слов: "))

for i in range(N):
    words = input("Введите слово: ")
    stroka += words + " "
print(stroka)