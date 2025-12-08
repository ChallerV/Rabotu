tries = 3

while True:
    pas = input(f"Введите пароль (У вас {tries} попытки на отгадку): ")

    if pas == "admin":
        print("Доступ разрешён")
        break

    if tries == 1:
        print("Вход заблокирован")
        break

    else:
        tries = tries - 1