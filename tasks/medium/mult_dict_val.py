"""
Написать функцию multiply_dict_values, которая принимает словарь SOME_DICT,
у которого ключи - строки, а значения - целые числа.

Необходимо, чтобы функция вернула результат умножения всех значений из словаря
"""
SOME_DICT = {str(val): val for val in range(1, 50, 3)}
print(SOME_DICT)


def multiply_dict_values(list1: dict):
    x = 1
    for key in list1:
        x *= list1[key]
    return x


if __name__ == '__main__':
    print(multiply_dict_values(SOME_DICT))
