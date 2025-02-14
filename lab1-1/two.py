import math

def calculate_function(a, x):
  """Вычисляет значение функции y = ax + cos(2x + 1).

  Args:
    a: Значение параметра a.
    x: Значение аргумента x.

  Returns:
    Значение функции y.
  """
  y = a * x + math.cos(2 * x + 1)
  return y

# Пример использования:
a_value = 2 # Задайте значение a
x_value = 3 # Задайте значение x
y_value = calculate_function(a_value, x_value)
print(f"Значение функции при a = {a_value}, x = {x_value}: {y_value}")

# Вычисление для нескольких значений x при фиксированном a:
a_value = 2
x_values = [0, 1, 2, 3, 4, 5]
for x in x_values:
    y = calculate_function(a_value, x)
    print(f"Значение функции при a = {a_value}, x = {x}: {y}")





