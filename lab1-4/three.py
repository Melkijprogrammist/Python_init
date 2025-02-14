def swap_first_last(text):
  """
  Меняет местами первый и последний символы в строке.

  Args:
    text: Исходная строка.

  Returns:
    Новая строка с поменянными первым и последним символами.
    Если строка пустая или состоит из одного символа, возвращает исходную строку.
  """
  if len(text) <= 1:
    return text  # Нет необходимости менять, если строка пустая или состоит из одного символа

  first_char = text[0]
  last_char = text[-1]
  middle_chars = text[1:-1]  # Все символы между первым и последним

  return last_char + middle_chars + first_char

# Пример использования:
string1 = "HAPPY"
new_string1 = swap_first_last(string1)
print(f"Исходная строка: {string1}, Новая строка: {new_string1}")  # Вывод: Исходная строка: hello, Новая строка: oellh

string2 = "ULIANA"
new_string2 = swap_first_last(string2)
print(f"Исходная строка: {string2}, Новая строка: {new_string2}")  # Вывод: Исходная строка: Python, Новая строка: nythoP

string3 = "G"
new_string3 = swap_first_last(string3)
print(f"Исходная строка: {string3}, Новая строка: {new_string3}")  # Вывод: Исходная строка: a, Новая строка: a

string4 = ""
new_string4 = swap_first_last(string4)
print(f"Исходная строка: {string4}, Новая строка: {new_string4}")  # Вывод: Исходная строка: , Новая строка:

