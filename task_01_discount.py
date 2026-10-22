price = float(input("Введите цену: "))
percent = float(input("Введите скидку (%): "))


if price < 0:
    print("Ошибка: цена не может быть отрицательной.")
elif percent < 0 or percent > 100:
    print("Ошибка: скидка должна быть от 0 до 100%.")
else:
    final_price = price * (1 - percent / 100)
print(f"Цена со скидкой: {final_price:.2f} руб.")