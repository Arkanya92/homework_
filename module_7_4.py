# Использование %:
team1_num = 6
print('В команде Мастера кода участников: %d!' % (team1_num))

team1_num = 6
team2_num = 6
print('Итого сегодня в командах участников: %d и %d!' % (team1_num, team2_num))

# Использование format():
score_2 = 42
print('Команда Волшебники данных решила задач: {}!'.format(score_2))

team1_time = 1552.512
team2_time = 2153.31451
print('Волшебники данных решили задачи за {}c!'.format(team1_time))

# Использование f-строк:
score_1 = 40
score_2 = 42
print(f'Команды решили {score_1} и {score_2} задач.')

challenge_result = 'Победа команды Волшебники данных!'
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'
print(f'Результат битвы: {result}!')

tasks_total = 82
time_avg = 45.2
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')