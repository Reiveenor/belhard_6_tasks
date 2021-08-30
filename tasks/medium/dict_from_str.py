"""
Написать функцию dict_from_str, которая принимает строковое значение STR_VAL,
из которого создает и возвращает словарь, следующего вида:
{
    'буква': количество-вхождений-в-строку
}

например: {
    'p': 2,
    'y': 1,
    ...
}
"""


def dict_from_str(arg1: str):
    arg1 = list(arg1)
    print(arg1)
    result_dict = {}
    for item in arg1:
        index = arg1.index(item)
        print(index)
    return result_dict


if __name__ == '__main__':
    STR_VAL = 'python is the fastest-growing major programming language'
    print(dict_from_str(STR_VAL))
