"""
Написать функцию set_diff, которая принимает 4 аргумента: 3 множества и параметр
symmetric, который по умолчанию должен быть False.

Функция должна возвращать либо разность, либо симметричную разность
в зависимости от значения параметра symmetric
"""


def set_diff(set1: set, set2: set, set3: set, symmetric=False):
    if symmetric:
        x = set1 - set2 - set3
    else:
        x = set1 ^ set2 ^ set3
    return print(x)


if __name__ == '__main__':
    set_diff({1, 3, 5, 2, 8, 4}, {10, 3, 5, 2}, {11, 15, 3, 7, 8, 4, 1})
    set_diff({1, 3, 5, 2, 8, 4}, {10, 3, 5, 2}, {11, 15, 3, 7, 8, 4, 1}, symmetric=True)
