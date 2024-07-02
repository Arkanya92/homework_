def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
# 1. Функция с парамерами по умолчанию
print('1.')
print_params(b = 25)
print_params([1, 2, 3])
# 2. Распаковка параметров
print('2.')
values_list = [6, 'Hello', False]
value_dict = {'a': 'student', 'b': False, 'c': 24}

print_params(*values_list)
print_params(**value_dict)
# 3. Распаковка + отдельные параметры
print('3.')
values_list_2 = [13.21, 'Name']
print_params(*values_list_2, 42)