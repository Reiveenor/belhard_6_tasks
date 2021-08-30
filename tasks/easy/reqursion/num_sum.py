"""
Написать рекурсивную функцию, которая будет вычислять сумму цифр целого числа

Можно пользоваться только функциями, операторами и условиями
"""

# def sum_func(arg1: int):
#     arg1 = list(arg1)
#     count_len = len(arg1)
#     x = 0
#     while count_len != 0:
#         x = x + int(arg1[count_len - 1])
#         count_len = count_len - 1
#     print(x)


def sum_func(arg1: int, digit=0):
    if arg1 % 10:
        digit += arg1 % 10
        return sum_func(arg1 // 10, digit)
    else:
        print(digit)


if __name__ == '__main__':
    sum_func(int(input("Input some number: ")))
