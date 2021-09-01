"""
Написать функцию get_dict_from_lists, которая принимает 2 значения - 2 списка
одинаковой длины: LIST_1 и LIST_2.

Необходимо, чтобы функция составляла и возвращала словарь, у которого ключи -
элементы LIST_1, а значения - элементы LIST_2
"""


def list_compose(list1: list, list2: list) -> list:
    result_dict = dict(zip(list1, list2))
    return result_dict


if __name__ == '__main__':
    LIST_1 = [str(i) for i in range(20)]
    LIST_2 = [i for i in range(20)]
    print(list_compose(LIST_1, LIST_2))
