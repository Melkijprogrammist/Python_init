#Подсчитайте количество символов (частоты символов) в заданной с клавиатуры строке.
def char_frequency(input_string):
    """Подсчитывает частоту символов в строке.

    Args:
        input_string: Строка, для которой нужно подсчитать частоту символов.

    Returns:
        Словарь, где ключи - символы, а значения - их частоты.
    """


    char_counts = {}
    for char in input_string:
        char_counts[char] = char_counts.get(char, 0) + 1
    
    return char_counts


# Пример использования:

input_string = input("Введите строку: ")
frequencies = char_frequency(input_string)


for char, count in frequencies.items():
    print(f"'{char}': {count}")



# Альтернативный вариант с использованием collections.Counter (более короткий, но требует импорта)

from collections import Counter

def char_frequency_counter(input_string):
    """Подсчитывает частоту символов с помощью collections.Counter."""
    return Counter(input_string)


input_string = input("Введите строку (Counter): ")
frequencies = char_frequency_counter(input_string)

for char, count in frequencies.items():
    print(f"'{char}': {count}")
