true_kod = 4590

while True:

    kod = int(input("Введите пин-код: "))

    if kod == true_kod:
        print("Поздравляю вы вошли!")
        break

    print("Ошибка пробуйте ещё раз")
