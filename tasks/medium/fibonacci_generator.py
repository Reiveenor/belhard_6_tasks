"""
Написать генератор fibonacci, которая принимает номер значения num_count
из чисел Фибоначчи и выводит на экран результат до заданного значения.

Номер значения нужно проверить

Пример:

fibonacci(0) -> 'Введите значение больше 1'
fibonacci(5)
1
2
3
5
8
Traceback (most recent call last):
File «C:/Python/Python3/python_generator.py», line 29, in
print(next(fib))
StopIteration
"""


def fibonacci(n: int):
    if n <= 1:
        raise ValueError("Введите значение больше 1")
    current = 1
    second = 2
    while current <= n:
        yield current
        current, second = second, current + second
        current += 1


if __name__ == '__main__':
    fib = fibonacci
    for i in fib(5):
        print(i)
