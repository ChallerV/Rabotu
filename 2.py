while True:
    number1 = int(input("Введите первое число: "))

    while True:
        number2 = int(input("Введите второе число: "))
        if number2 <= number1:
            print("❌Ошибка: второе число меньше первого!")
            continue

        else:
            break

    while True:
        number3 = int(input("Введите третье число: "))
        if number3 <= number2:
            print("❌Ошибка: третье число меньше второго!")
            continue

        else:
            break

    if number1 <= number3 and number2 <= number3:
        print("Последовательность принята")
        break