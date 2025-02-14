#Найти длину окружности L и площадь круга S заданного радиуса R: L = 2 * Pi * R, S = PI * R^2
import math 
def calculate_circle_properities(R):
    if R <= 0:
        print("Ошибка: Радиус должен быть положительным")
        return None
    
    L = 2 * math.pi * R 
    S = math.pi * R * 2
    return L, S

radius = 6
result = calculate_circle_properities(radius)

if result:
    L, S = result
    print(f"Длина окружности  с радиусом {radius}: {L}")
    print(f"Площадь круга с радиусом {radius}: {S}")