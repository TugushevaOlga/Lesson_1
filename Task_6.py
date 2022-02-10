day = 1
a = float(input('Сколько километров ты пробежал сегодня: '))  # start result
b = float(input('Твоя цель пробегать ежедневно не менее: '))  # finish_result
while a < b:
    a += a * 0.1
    day += 1

print(f'Ты добьёшся поставленной цели на {day} день!')
