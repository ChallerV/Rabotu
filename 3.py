max_number = 0

while True:
    number = int(input("Введите число (0 для выхода из цикла): "))

    if number == 0:
        print("Был выполнен выход из цикла")
        print(f"Самое большое введённое число: {max_number}")
        break

    elif number > max_number:
        max_number = number
        continue