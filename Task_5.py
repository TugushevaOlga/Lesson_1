revenue = float(input('Введите сумму выручки: '))
costs = float(input('Введите значение расходов: '))
employers = int(input('Введите количество сотрудников: '))
result = revenue - costs
profit = result/revenue*100
if result > 0:
    print(f'Прибыль составляет:{result:.2f}')
    print( f'Рентабельность:{profit:.1f} %')
    print(f'Прибыль фирмы на одного сотрудника составляет: {result/employers:.2f}')
elif result<0:
    print(f'Убыток составляет: {result:.2f}')
else:
    print('Нулевой результат')