# Задача 1. Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа
# N. 60 -> 2, 2, 3, 5

# n = int(input("Введите натуральное число N: "))
# a = n
# list_n = []
#
# for i in range(2, 10):
#     while n % i == 0:
#         n = int(n / i)
#         list_n.append(i)
# print(f"Cписок простых множителей числа {a}")
# print(list_n)

# Задача 3. Выведите число π с заданной точностью. Точность выводится в виде десятичной дроби.
# 0.001 -> 3.142
# 0.00001 -> 3.14159
import math
precision = int(input("Введите необходимую точность: "))
if precision > 15:
    print("Введенная степень слишком высока, результат будет отображен только до 15 разряда")
output = 1 / math.pow(10, precision)
print(f"π с заданной точностью {output} -> {round(math.pi, precision)}")