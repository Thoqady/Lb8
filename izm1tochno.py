#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Решить индивидуальное задание лабораторной работы 6, оформив каждую команду в виде
#отдельной функции

#  Использовать словарь, содержащий следующие ключи: название пункта назначения; номер
# поезда; время отправления. Написать программу, выполняющую следующие действия: ввод
# с клавиатуры данных в список, состоящий из словарей заданной структуры; записи должны
# быть упорядочены по времени отправления поезда; вывод на экран информации о поездах,
# направляющихся в пункт, название которого введено с клавиатуры; если таких поездов нет,
# выдать на дисплей соответствующее сообщение.

import sys


def add(trains, name, number, time):
    train = {
        'name': name,
        'number': number,
        'time': time,
    }

    trains.append(train)
    if len(trains) > 1:
        trains.sort(key=lambda item: item.get('name', ''))


def list(trains):
    table = []
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20,
        '-' * 17
    )
    table.append(line)
    table.append(
        '| {:^4} | {:^30} | {:^20} | {:^17} |'.format(
            "№",
            "Пункт назначения",
            "Номер поезда",
            "Время отправления"
        )
    )
    table.append(line)

    for idx, train in enumerate(trains, 1):
        table.append(
            '| {:>4} | {:<30} | {:<20} | {:>17} |'.format(
                idx,
                train.get('name', ''),
                train.get('number', ''),
                train.get('time', 0)
            )
        )

    table.append(line)

    return '\n'.join(table)


def select(trains, period):

    result = []
    for train in trains:
        if period == train.get('name'):
            result.append(train)

    return result


if __name__ == '__main__':
    trains = []

    while True:
        command = input(">>> ")

        if command == 'exit':
            break

        elif command == 'add':
            name = input("Пункт назначения ")
            number = input("Номер поезда ")
            time = input("Время отправления ")

            add(trains, name, number, time)

        elif command == 'list':
            print(list(trains))

        elif command.startswith('select '):
            parts = command.split(maxsplit=1)
            selected = select(trains, parts[1])
            count = 0
            if selected:
                for idx, train in enumerate(selected, 1):
                    print(
                        '{:>4}: {}, номер поезда - {}, время отправления - {}'.format(count, train.get('name', ''),
                                                                                      train.get('number', ''),
                                                                                      train.get('time', ''))
                    )
            else:
                print("Таких пунктов назначения не найдено.")

        elif command == 'help':
            print("Список команд:\n")
            print("add - Добавить данные;")
            print("list - Вывести данные;")
            print("select <Город> - Вывести всю информацию  по городу;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
