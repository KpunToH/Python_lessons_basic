
__author__ = 'Горюшко Сергей Михайлович'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

number_complex = abs(int(input("Привет!Пожалуйста, введите любое целое число"))) #получаем число, на всякий случай отбрасываем отрицательную часть
while number_complex>10 : #цикл для отображения в обратном порядке. Остаток от деления на 10 показывает каждое число для десятичной системы счисления
    i = number_complex%10
    print (i)
    number_complex=number_complex//10
print(number_complex) #отбражение первого числа

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную 
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

var_1 = input("Пожалуйста, введите первое число")
var_2 = input("Пожалуйста, введите второе число")
var_3 = var_1 #кладем первое число в доп.хранилище
var_1 = var_2 # заменяем первую переменную второй
print ("Меняем местами!:",var_1 ,var_3) #Достаем первую переменную из доп.хранилища :) 

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

age = int(input ("Пожалуйста, введите, сколько вам полных лет (Пример - Если вам 17 лет и 11 месяцев - вы должны ввести 17)"))
if age>=18:
    print("Доступ разрешен!")
else:
    print("Извините, пользование данным ресурсом только с 18 лет")
