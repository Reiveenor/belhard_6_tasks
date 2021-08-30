"""
Написать функцию common_numbers, которая принимает 2 списка, которые содержат
целые числа.

Функция должна вернуть список общих чисел, который отсортирован по убыванию
"""


def common_numbers(list1: list, list2: list):
    list1.extend(list2)
    return print(sorted(list1, reverse=True))


if __name__ == '__main__':
    common_numbers([1, 2, 5, 6, 3, 2], [5, -1, 4, 8, 10, -3])
