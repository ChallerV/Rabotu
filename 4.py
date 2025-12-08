sum_price = 0

while True:
    number = int(input("Введите цену товара(ов) (0 для выхода из цикла): "))

    if number < 0:
        print("Ошибка цены")
        continue

    sum_price += number
    if number == 0:
        print("\nБыл выполнен выход из цикла")
        break

if sum_price > 1000:
    print(f"Сумма всех цен со скидкой равняется: {sum_price * 0.9}")
else:
    print(f"Сумма всех цен без скидки равняется: {sum_price}")