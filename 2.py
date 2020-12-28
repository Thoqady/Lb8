#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Решите следующую задачу: в основной ветке программы вызывается функция cylinder(),
#которая вычисляет площадь цилиндра. В теле cylinder() определена функция circle(),
#вычисляющая площадь круга по формуле . В теле cylinder() у пользователя
#спрашивается, хочет ли он получить только площадь боковой поверхности цилиндра,
#которая вычисляется по формуле , или полную площадь цилиндра. В последнем
#случае к площади боковой поверхности цилиндра должен добавляться удвоенный результат
#вычислений функции circle().


def circle(a):
    return 3.14 * a**2


def cylinder(a, b, c):
    circle(a)
    if c == '1':
        return 2 * 3.14 * a * b + 2 * circle(a)
    if c == '2':
        return 2 * 3.14 * a * b


if __name__ == '__main__':

    a = float(input("Введите радиус круга "))
    b = float(input("Введите высоту цилиндра "))
    c = input("Введите 1 - если хотите посчитать полную площадь цилиндра, или Введите 2 - если хотите посчитать площадь боковой поверхности ")
    s = cylinder(a, b, c)
    print(s)