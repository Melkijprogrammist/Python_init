import math

def calculate_function(x):
  """Вычисляет значение функции y = 3x + sin(x + 2).

  Args:
    x: Значение аргумента x.

  Returns:
    Значение функции y.
  """
  y = 3 * x + math.sin(x + 2)
  return y

# Пример использования:
x_value = 2 # Задайте значение x
y_value = calculate_function(x_value)
print(f"Значение функции при x = {x_value}: {y_value}")


# Вычисление для нескольких значений x:
x_values = [0, 1, 2, 3, 4, 5]
for x in x_values:
    y = calculate_function(x)
    print(f"Значение функции при x = {x}: {y}")