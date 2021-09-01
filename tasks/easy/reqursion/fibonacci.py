"""
Написать рекурсивную функцию fibonacci, которая будет возвращать n-ый элемент
"""


def fibonacci(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    print(fibonacci(int(input("Input some number: "))))
