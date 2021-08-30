"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
проходит по нему и выводит Yes, если число уже встречалось и No, если нет
"""


def yes_or_no(list1: list):
    for i in range(len(list1) - 1):
        x = list1.count(list1[i])
        i += 1
        if x == 2:
            print("Yes")
        else:
            print("No")


if __name__ == '__main__':
    yes_or_no([1, 2, 2, 5, 6, 3, 1, 8, 3])
