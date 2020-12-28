#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Решите следующую задачу: напишите программу, в которой определены следующие четыре
#функции:
#1. Функция getInput() не имеет параметров, запрашивает ввод с клавиатуры и возвращает
#в основную программу полученную строку.
#2. Функция testInput() имеет один параметр. В теле она проверяет, можно ли переданное
#ей значение преобразовать к целому числу. Если можно, возвращает логическое True.
#Если нельзя – False.
#3. Функция strToInt() имеет один параметр. В теле преобразовывает переданное значение
#к целочисленному типу. Возвращает полученное число.
#4. Функция printInt() имеет один параметр. Она выводит переданное значение на экран и
#ничего не возвращает.
#В основной ветке программы вызовите первую функцию. То, что она вернула, передайте во
#вторую функцию. Если вторая функция вернула True, то те же данные (из первой функции)
#передайте в третью функцию, а возвращенное третьей функцией значение – в четвертую.

def getInput():
    return float(input("Введите число "))


def testInput(a):
    if a == int(a):
        return True
    else:
        return False


def strToInt(b):
    if b == int(b):
        return int(b)


def printInt(c):
    print(c)


if __name__ == '__main__':
    d = getInput()
    if testInput(d) is True:
        d1 = strToInt(d)
        printInt(d1)