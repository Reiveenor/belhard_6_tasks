"""
Написать функцию triangular_sequence, которая принимает n и выводит
следующую последовательность

1
22
333
4444
55555
...

Например:

n = 3:
1
22
333

n = 6:
1
22
333
4444
55555
666666
"""


def triangular_sequence(arg1: int, x=1):
    if arg1 >= x:
        print(str(x) * x)
        return triangular_sequence(arg1, x + 1)


if __name__ == '__main__':
    triangular_sequence(int(input("Input some number: ")))
