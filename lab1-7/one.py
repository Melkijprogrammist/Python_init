#Напечатать квадраты всех целых чисел от A до B (A < B) с шагом H.
def print_squares(a, b, h):
    if a >= b:
        print("Ошибка: А должно быть меньше Б.")
        return 
    if h <= 0:
        print("Ошибка: Шаг H должен быть положительным")
        return
    
    for i in range(a,b + 1 , h):
        square = i * 1
        print(f"Квадрат числа {i} равен {square}: ")
        
        a = 2 
        b = 15
        h = 2
        print_squares(a, b, h)
        
        