def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')   # Открываем файл для записи
    strings_positions = {}                          # Создается пуйто словарь
    for i in range (len(strings)):                  # Перебираеться список по элементам
        strings_positions[(i + 1, file.tell())] = strings[i]    # Добавляем в словарь ключ: строка и количество байтов
                                                                # значемние строка из списка
        file.write(f'{strings[i]}\n')               # Записываем строку в файл с переносом строки
    file.close()                                    # Закрываем файл
    return strings_positions                        # Возвращаем полученный словарь словарь

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)