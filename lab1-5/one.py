def calculate_y(a, x):
  """Вычисляет значение функции y в зависимости от x.

  Args:
    a: Параметр a.
    x: Значение x.

  Returns:
    Значение y.
  """
  if x > 2:
    y = 2 * a * x - 2
  else:
    y = 3 * a - 2 * x
  return y

# Пример использования:
a = 5  # Задайте значение a
x = 3  # Задайте значение x

y = calculate_y(a, x)
print(f"При a = {a} и x = {x}, y = {y}")

a = 5
x = 2
y = calculate_y(a, x)
print(f"При a = {a} и x = {x}, y = {y}")

a = 5
x = 1
y = calculate_y(a, x)
print(f"При a = {a} и x = {x}, y = {y}")

