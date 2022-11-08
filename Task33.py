# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k. Пример: k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0

import random

k = int(input('Введите значение k = '))
list_coef = [random.randint(-100, 100) for i in range(k+1)]
print(list_coef)

def calc(k):
    if k != 1:
        polynom = str(list_coef[0])+'x^' + str(k) + ' '
        count = k - 1
        while count > 1:
            if list_coef[k - count] != 0:
                polynom += '+ ' + \
                    str(list_coef[k - count]) + 'x^' + str(count) + ' '
            count -= 1
            if count == 1:
                polynom += '+ ' + \
            str(list_coef[k - count]) + 'x + ' + \
            str(list_coef[k - count + 1]) + ' = 0'
            elif k == 1:
                polynom = str(list_coef[0]) + \
                    'x + ' + str(list_coef[1]) + ' = 0'
    print(polynom)
    with open('task33.txt', 'w') as f:
        f.write(polynom)
        f.close()

calc(k)
    