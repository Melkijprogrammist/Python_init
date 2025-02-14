def mirror_three_digit_number(number):
    """
    Зеркально отображает трехзначное число.

    Args:
        number: Трехзначное число.

    Returns:
        Зеркально отображенное число.
        Возвращает None, если число не является трехзначным целым числом.
    """

    if not isinstance(number, int) or not (100 <= number <= 999):
        print("Ошибка: Введите трехзначное целое число.")
        return None

    # Вариант 1: Преобразование в строку и обратный порядок
    mirrored_number_str = str(number)[::-1]
    mirrored_number = int(mirrored_number_str)
    return mirrored_number



# Вариант 2: Арифметические операции (более эффективный)

def mirror_three_digit_number_v2(number):
    """
    Зеркально отображает трехзначное число с помощью арифметических операций.

    Args:
        number: Трехзначное число.

    Returns:
        Зеркально отображенное число.
        Возвращает None, если число не является трехзначным целым числом.
    """
    if not isinstance(number, int) or not (100 <= number <= 999):
        print("Ошибка: Введите трехзначное целое число.")
        return None

    a = number % 10 # Единицы
    b = (number // 10) % 10 # Десятки
    c = number // 100 # Сотни

    mirrored_number = a * 100 + b * 10 + c
    return mirrored_number


# Примеры использования:
number = 123
mirrored = mirror_three_digit_number(number)

if mirrored: # Проверка на None
    print(f"Зеркальное отображение числа {number}: {mirrored}")


mirrored_v2 = mirror_three_digit_number_v2(number)
if mirrored_v2: # Проверка на None
    print(f"Зеркальное отображение числа (v2) {number}: {mirrored_v2}")



# Пример с некорректным вводом:
number = 1234
mirrored = mirror_three_digit_number(number) # Вернет None и выведет сообщение об ошибке



# Пример с вводом от пользователя:
try:
    number = int(input("Введите трехзначное число: "))
    mirrored = mirror_three_digit_number(number) # Или используйте v2
    if mirrored:
        print(f"Зеркальное отображение: {mirrored}")
except ValueError:
    print("Ошибка: Введите целое число.")
