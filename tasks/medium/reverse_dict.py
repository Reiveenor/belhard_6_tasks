"""
Написать функцию reverse_dict, которая принимает словарь ключ-значение и
возвращает новый словарь, у которого ключи - значения первого, а значения -
ключи первого

Тело функции может состоять из одной строки!
"""


def reverse_dict(dict1: dict):
    k_dict = dict1.keys()
    v_dict = dict1.values()
    new_dict = zip(v_dict, k_dict)
    return dict(new_dict)


if __name__ == '__main__':
    print(reverse_dict({'e': 1, 'v': 3, 'f': 4}))
