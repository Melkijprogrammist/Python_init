# Найти сумму цифр введенного четырехзначного числа
def sum_digits_four_digit_number(number):
    """Вычисляет сумму цифр четырехзначного числа.

    Args:
        number: Четырехзначное число.

    Returns:
        Сумму цифр числа.
        Возвращает None, если число не является четырехзначным целым числом.
    """

    if not isinstance(number, int) or not (1000 <= number <= 9999):
        print("Ошибка: Введите четырехзначное целое число.")
        return None

    sum_of_digits = 0
    for digit in str(number):
        sum_of_digits += int(digit)
    return sum_of_digits




# Примеры использования:
number = 1234
result = sum_digits_four_digit_number(number)
if result: # Проверка на корректность ввода
    print(f"Сумма цифр числа {number}: {result}")


number = 12345 # Не четырехзначное
result = sum_digits_four_digit_number(number) # Выведет сообщение об ошибке и вернет None

number = 123.4 # Не целое
result = sum_digits_four_digit_number(number) # Выведет сообщение об ошибке и вернет None




# Пример с вводом от пользователя:
try:
    number = int(input("Введите четырехзначное число: "))
    result = sum_digits_four_digit_number(number)

    if result:
        print(f"Сумма цифр: {result}")

except ValueError:
    print("Ошибка: Введите целое число.")



# Альтернативный вариант (без преобразования в строку):

def sum_digits_four_digit_number_v2(number):
    """Вычисляет сумму цифр четырехзначного числа (без преобразования в строку).

    Args:
        number: Четырехзначное число.

    Returns:
        Сумму цифр числа.
        Возвращает None, если число не является четырехзначным целым числом.
    """

    if not isinstance(number, int) or not (1000 <= number <= 9999):
        print("Ошибка: Введите четырехзначное целое число.")
        return None

    a = number % 10
    b = (number // 10) % 10
    c = (number // 100) % 10
    d = number // 1000

    return a + b + c + d

number = 4321
result_v2 = sum_digits_four_digit_number_v2(number)
if result_v2:
    print(f"Сумма цифр числа (v2) {number}: {result_v2}")


