"""
Написать функцию to_set, которая принимает список, а возвращает множество,
созданное из этого списка и длину этого множества
"""


def to_set(some_list: list):
    return print(set(some_list)), print(len(set(some_list)))


if __name__ == '__main__':
    to_set([1, 2, 3, 4, 5, 5, 2, 3])
