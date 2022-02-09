num = int(input('Введите целое положительное число :'))
max_digit = num % 10 #
while num > 0:

    num = num // 10
    if num % 10 > max_digit:
        max_digit = num % 10
    if max_digit == 9:
        break
print(f'Наибольшая цифра в числе равна {max_digit}')
