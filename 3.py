#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Решите следующую задачу: напишите функцию, которая считывает с клавиатуры числа и
#перемножает их до тех пор, пока не будет введен 0. Функция должна возвращать
#полученное произведение. Вызовите функцию и выведите на экран результат ее работы.

def ymn():
    while True:
        a = int(input("Введите а "))
        b = int(input("Введите b "))

        if a == 0 or b == 0:
            break

        proizv = a * b
        print("Произведение чисел равно", proizv)


if __name__ == '__main__':
    ymn()