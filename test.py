def positive():
    print("Положительное")


def negative():
    print("Отрицательное")


def test(a):
    if a >= 0:
        positive()
    else:
        negative()


if __name__ == '__main__':
    a = int(input("Введите целое число "))
    test(a)