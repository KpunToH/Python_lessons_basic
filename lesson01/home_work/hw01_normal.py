
__author__ = 'Горюшко Сергей Михайлович'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

number_complex =(int(input("Привет!Пожалуйста, введите любое целое число"))) #получаем число
i_max = 0 #хранилище для наибольшего числа
while number_complex>10 : #цикл для отображения в обратном порядке. Остаток от деления на 10 показывает каждое число для десятичной системы счисления
    i = number_complex%10
    if i>i_max: #Проверка, больше ли новое число уже известных
        i_max=i
    number_complex=number_complex//10
print(i_max) 



# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.
var_1 = input("Пожалуйста, введите первое число")
var_2 = input("Пожалуйста, введите второе число")
var_1, var_2 = var_2, var_1 #кортеж! Я так и не понял его синтаксис, если честно.Пытался через создание вроде a= tupple (var_1,var_2), но выдает ошибки
print (var_1,var_2)


# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4
import math

a = int(input("Пожайлуйста, введите первый коэффициент уравнения"))
b = int(input("Пожайлуйста, введите второй коэффициент уравнения"))
c = int(input("Пожайлуйста, введите третий коэффициент уравнения"))
d = b**2-4*a*c #дискриминант

if d>=0:
    x1 = (-1*b + math.sqrt(d))/(2*a)
    x2 = (-1*b - math.sqrt(d))/(2*a)
    print("Корни уравнения:", x1, x2) #Прощай, бесполезное школьное прорешивание квадратных уравнений!.
else:
 print("Нет вещественных решений")
