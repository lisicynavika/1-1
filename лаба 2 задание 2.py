stroka = ""

while True:
    words = input("Введите слово: ")
    if words == "stop":
        break
    stroka += words + " "
print(stroka)
