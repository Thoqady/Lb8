#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import json

def add(trains, name, number, time):
    # Создать словарь.
    train = {
        'name': name,
        'number': number,
        'time': time,
    }

    # Добавить словарь в список.
    trains.append(train)
    # Отсортировать список в случае необходимости.
    if len(trains) > 1:
        trains.sort(key=lambda item: item.get('name', ''))


def list(trains):
    table = []
    # Заголовок таблицы.
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

    # Вывести данные о всех сотрудниках.
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

    # Инициализировать результат.
    result = []
    # Проверить сведения работников из списка.
    for train in trains:
        if period == train.get('name'):
            result.append(train)

    return result


def load(filename):
    with open(filename, 'r') as fin:
        return json.load(fin)


def save(trains, filename):
    with open(filename, 'w') as fout:
        json.dump(trains, fout)


if __name__ == '__main__':
    # Список работников.
    trains = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ")

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            # Запросить данные о рейсе.
            name = input("Пункт назначения ")
            number = input("Номер поезда ")
            time = input("Время отправления ")

            add(trains, name, number, time)

        elif command == 'list':
            print(list(trains))

        elif command.startswith('select '):
            # Разбить команду на части для выделения номера года.
            parts = command.split(maxsplit=1)
            # Получить список работников.
            selected = select(trains, parts[1])
            count = 0
            # Вывод списка работников.
            if selected:
                for idx, train in enumerate(selected, 1):
                    print(
                        '{:>4}: {}, номер поезда - {}, время отправления - {}'.format(count, train.get('name', ''),
                                                                                      train.get('number', ''),
                                                                                      train.get('time', ''))
                    )
            else:
                print("Таких пунктов назначения не найдено.")


        elif command.startswith('load '):
            # Разбить команду на части для имени файла.
            parts = command.split(maxsplit=1)
            # Загрузить данные из файла
            trains = load(parts[1])

        elif command.startswith('save '):
            # Разбить команду на части для имени файла.
            parts = command.split(maxsplit=1)
            # Сохранить данные в файл
            save(trains, parts[1])

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - Добавить данные;")
            print("list - Вывести данные;")
            print("select <Город> - Вывести всю информацию  по городу;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
