"""
Написать 2 генератора:
1) Генератор simple_number первый идет по всем простым числам
(число делится только на 1 и на само себя)
2) Генератор odd_simple, который используется значения первого и возвращает
из них нечетные
"""


def simple_number(n: int):
    f_list = []
    while n > 0:
        for i in range(2, n):
            if i == 2 or i == 3:
                yield i
            if i % 2 == 1 and i % 3 != 0:
                f_list.append(i)
                yield i
            n -= 1


def odd_simple(i):
    s_list = []
    if i % 2 != 0:
        s_list.append(i)
        yield i


if __name__ == '__main__':
    num = simple_number
    odd = odd_simple
    for x in num(20):
        print(f"first list number: {x}")
        for j in odd(x):
            print(f"second list number: {j}\n")
