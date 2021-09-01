"""
Написать рекурсивную функцию, которая будет красиво выводить данные в консоль.
Если строчный тип данных, то выводить в кавычках


например:

data = {'a': 123, 123: [1, 2, 3], 'asd': {'c': 654.54}}

{
    'a': 123,
    123: [1, 2, 3],
    'asd': {
        'c': 654.54,
    },
}
"""


from print_dict import pd


def req_print(x):
    pd(x)


if __name__ == '__main__':
    x = {'a': 123, 123: [1, 2, 3], 'asd': {'c': 654.54}}
    req_print(x)
