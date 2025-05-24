def is_magic_date(date_str):
    try:
        day, month, year = map(int, date_str.split('.'))
        last_two_digits = year % 100
        return day * month == last_two_digits
    except (ValueError, AttributeError, IndexError):
        return False

# Запрос даты у пользователя
user_date = input("Введите дату в формате ДД.ММ.ГГГГ: ")

# Проверка и вывод результата
if is_magic_date(user_date):
    print("Дата магическая!")
else:
    print("Дата не магическая.")