def apply_all_func(int_list, *functions):
    results = {}
    for x in int_list:
        if not isinstance(x, (int, float)):
            return "Ошибка: Все элементы списка должны быть числами."

    for func in functions:
        results[func.__name__] = func(int_list)

    return results


# Примеры использования:
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))