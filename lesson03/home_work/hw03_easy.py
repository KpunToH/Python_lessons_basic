# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

    def my_round(chislo,razmer):
    chislo = str(chislo)
    last_digit = int(chislo[(razmer + 1)])
    if last_digit >= 5:
        chislo_2 = float(chislo[0:(razmer+1)]) + (0.1**(razmer-1))
		#Решаем проблему с float числами питона,для которого (0.1**2=0.0100000000002)
        chislo_2 = str(chislo_2) 
        chislo_2 = float(chislo_2[0:razmer+1])
    else:
        chislo_2 = chislo[0:(razmer + 1)]
    return chislo_2

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))




# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    a = ticket_number
    a = str(a)
    a_lenght = len(a)
    center = int(a_lenght / 2)
    sum_first = 0
    sum_second = 0
    if a_lenght % 2 == 0:
        first_numbers = list(map(int, list(a[:center])))
        second_numbers = list(map(int, list(a[center:])))
        for i in first_numbers:
            sum_first = sum_first + i
            i += 1
        for i in second_numbers:
            sum_second = sum_second + i
            i += 1
    else:
        first_numbers = list(map(int, list(a[:center])))
        second_numbers = list(map(int, list(a[center + 1:])))
        for i in first_numbers:
            sum_first = sum_first + i
            i += 1
        for i in second_numbers:
            sum_second = sum_second + i
            i += 1
    return bool(sum_first == sum_second)


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
