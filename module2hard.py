def get_password(n):
    used_pairs = set()
    result = ""
    for i in range (1, n):
        for j in range (i + 1, n):
                if n % (i + j) == 0:
                    pair = str(i) + str(j)
                    if pair not in used_pairs:
                        used_pairs.add(pair)
                        result += pair
    return result

flag = 0
while flag == 0:
    n = int(input('Введите число от 3 до 20: '))
    if n >= 3 and n <= 20:
        flag += 1
        password = get_password(n)
    else:
        print('Ввели неверное число, попробуйте еще раз.')
print(f'Пароль для числа {n}: {password}')