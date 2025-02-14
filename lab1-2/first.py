#Даны длины ребер a, b, c прямоугольного параллелепипеда. Найти его объем V = a * b * c и площадь поверхности S = 2* (a * b + b * c + a * c) 
def calculate_parallelepiped_properites(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        print("Ошибка: Длины ребер должны быть положительными числами. ")
        return None
    
    V = a * b * c
    S = 2 * (a * b + b * c + a * c )
    return V, S

a = 3
b = 6
c = 8

result = calculate_parallelepiped_properites(a, b, c)

if result:
    V, S = result
    print(f"Объем паралелипипеда: {V}")
    print(f"Площадь поверхности паралелипипеда {S}")