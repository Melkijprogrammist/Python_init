#Составить программу, которая после введенного с клавиатуры числа (в диапазоне
#от 1 до 999), обозначающего денежную величину, дописывает слово «рубль» в пра-
#вильной форме. Например, 5 рублей, 21 рубль, 173 рубля.
def format_rubles(amount):
    if not 1 <= amount <= 999:
        return "Некорректный ввод: число должно быть от 1 до 999"
    
    last_digit = amount % 10
    last_two_digit = amount % 100
    
    if 11 <= last_two_digit <= 19:
        ruble_form = "Рублей"
    elif last_digit == 1:
        ruble_form = "Рубль"
    elif 2 <= last_two_digit:
        ruble_form = "Рубля"
    else:
        ruble_form = "Рублей"
        return f"{amount} {ruble_form}"
    
    try:
        amount = int(input("Введите денежную величину (от 1 до 999):"))
        result = format_rubles(amount)
        print(result)
    except ValueError:
        print("Некорректный ввод: введите целое число.")