def get_multiplied_digits(number):
    str_number = str(number)    # Преобразование целого числа в строку
    first = int(str_number[0])  # Запись первого символа
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:])) # Умножение первой цифры числа на результат функции
    else:                                                         # без первой цифры
        return first

result = get_multiplied_digits(40203)
print(result)