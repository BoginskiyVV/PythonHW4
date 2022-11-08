# Задайте натуральное число N. Напишите программу, которая составит список 
# простых множителей числа N.

def find_div(N):
    temp = []
    dividers = []
    div = 2
    x = N
    while div * div <= N:
        if N % div == 0:
            temp.append(div)
            N //= div
        else:
            div += 1
        if N > 1:
                temp.append(N)
        else:
            break
    dividers = list(set(temp))
    print('{} = {}'.format(x, dividers))

N = int(input('Введите натуральное число: '))
find_div(N)
