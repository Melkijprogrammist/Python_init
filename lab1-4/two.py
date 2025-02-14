# Удалите из непустой строки каждый n-й символ, начиная с первого.
def remove_every_nth_char(input_string, n):
    """Удаляет каждый n-й символ из строки, начиная с первого.

    Args:
        input_string: Исходная строка.
        n: Шаг удаления (каждый n-й символ).

    Returns:
        Новую строку с удаленными символами.
        Возвращает исходную строку, если она пустая или n <= 0.
    """

    if not input_string or n <= 0:
        return input_string

    new_string = ""
    for i, char in enumerate(input_string):
        if (i + 1) % n != 0:
            new_string += char
    return new_string


# Вариант 2 (с использованием срезов и join, более Pythonic):

def remove_every_nth_char_slice(input_string, n):
    """Удаляет каждый n-й символ из строки с помощью срезов."""
    if not input_string or n <= 0:
        return input_string

    new_string_list = [char for i, char in enumerate(input_string) if (i+1)%n !=0]
    return "".join(new_string_list)




# Примеры использования:
string = "abcdefg"
n = 2
result = remove_every_nth_char(string, n)
print(f"Результат: {result}") # Вывод: bdfg

result_slice = remove_every_nth_char_slice(string,n)
print(f"Результат (slice): {result_slice}") # Вывод: bdfg



string = "abcdefg"
n = 1
result = remove_every_nth_char(string, n)
print(f"Результат: {result}") # Вывод: "" (пустая строка)



string = "" # Пустая строка
n = 2
result = remove_every_nth_char(string, n)
print(f"Результат: {result}") # Вывод: ""



string = "abc"
n = 0 # Некорректное значение n
result = remove_every_nth_char(string, n)
print(f"Результат: {result}") # Вывод: abc (исходная строка)


# Пример с вводом от пользователя:
input_string = input("Введите строку: ")
n = int(input("Введите n: "))

result = remove_every_nth_char_slice(input_string, n) # Или используйте первый вариант
print(f"Результат: {result}")

