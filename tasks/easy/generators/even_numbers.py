"""
Написать генератор get_even_number, который возвращает подряд четные числа

Например:

even_gen = get_even_number()

next(even_gen) -> 2
next(even_gen) -> 4
next(even_gen) -> 6
"""


def get_even_number():
    n = 0
    while True:
        yield n + 2
        n += 2


if __name__ == '__main__':
    even_gen = get_even_number()
    print(next(even_gen))
    print(next(even_gen))
    print(next(even_gen))
    print(next(even_gen))
