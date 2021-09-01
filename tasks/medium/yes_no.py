"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
проходит по нему и выводит Yes, если число уже встречалось и No, если нет
"""


def yes_or_no(list1: list):
    some_set = set()

    for i in list1:
        if i in some_set:
            print("Yes")
        else:
            some_set.add(i)
            print("No")


if __name__ == '__main__':
    yes_or_no([1, 2, 2, 5, 6, 3, 1, 8, 3])
