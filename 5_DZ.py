# Задача 26: Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8


def degree(a, b):
    if b == 0:
        return 1
    elif b > 0:
        return a * degree(a, b - 1)
    else:
        return 1 / a * degree(1 / a, abs(b) - 1)             

A = int(input('Введите число: '))
B = int(input('Введите степень числа: '))
print(f'{A} в степени {B} = {degree(A, B)}')

# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# 2 2
# 4


def Sum(a, b):
    if b == 0:
        return a
    else:
        sum = Sum(a, b - 1) + 1
    return sum

def isInt(number):
    try:
        int(number)
        return True
    except ValueError:
        return False

firstNumber = input('Введите первое целое неотрицательное число > ')
secondNumber = input('Введите второе целое неотрицательное число > ')
if isInt(firstNumber) and isInt(secondNumber) and int(firstNumber) >= 0 and int(secondNumber) >= 0:
    print(Sum(int(firstNumber), int(secondNumber)))
else:
    print('Необходимо ввести ЦЕЛЫЕ НЕОТРИЦАТЕЛЬНЫЕ ЧИСЛА!' +
    ' Перезапустите программу и попробуйте ещё раз')