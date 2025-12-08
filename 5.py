balance_user = 1000

while True:
    menu = int(input("1. Узнать баланс \n2. Снять 100 рублей \n3. Положить 100 рублей \n4. Выход \n\nВыберите одну из опций: "))

    if menu == 4:
        print("\nДо свидания")
        break

    elif menu == 3:
        balance_user += 100
        print("\nНа ваш счёт зачислено 100 рублей\n")

    elif menu == 2:

        if balance_user >= 100:
            balance_user -= 100
            print("\nСнято\n")

        else:
            print("\nНедостаточно средств\n")
            continue

    elif menu == 1:
        print(f"\nВаш текущий баланс: {balance_user}\n")
        continue

    else:
        print("\nНеверная команда\n")
