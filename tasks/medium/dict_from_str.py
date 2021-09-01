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


def dict_from_str(list1: str):
    arg1 = list(list1)
    some_list = []
    for item in arg1:
        some_list.append(list1.count(item))
    result_dict = zip(list1, some_list)
    return dict(result_dict)


if __name__ == '__main__':
    STR_VAL = 'python is the fastest-growing major programming language'
    print(dict_from_str(STR_VAL))
