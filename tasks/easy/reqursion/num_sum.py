"""
Написать рекурсивную функцию, которая будет вычислять сумму цифр целого числа

Можно пользоваться только функциями, операторами и условиями
"""


def sum_func(arg1: int, digit=0):
    if arg1 % 10:
        digit += arg1 % 10
        return sum_func(arg1 // 10, digit)
    else:
        print(digit)


if __name__ == '__main__':
    sum_func(int(input("Input some number: ")))
