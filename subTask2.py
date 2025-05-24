def divide_100_by_number():
    try:
        num = float(input("Введите число для деления 100: "))
        result = 100 / num
        print(f"Результат деления: {result}")
    except ValueError:
        print("Ошибка: Введено не число!")
    except ZeroDivisionError:
        print("Ошибка: Деление на ноль!")
    except Exception as e:
        print(f"Произошла неизвестная ошибка: {e}")

divide_100_by_number()